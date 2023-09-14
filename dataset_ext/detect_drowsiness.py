
from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import cv2
import sys

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

thresh = 0.25
frame_check = 20
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")# Dat file is the crux of the code

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
cap=cv2.VideoCapture(sys.argv[2])
flag=0
f1=0
f2=0
while True:
    ret, frame=cap.read()
    frame = imutils.resize(frame, width=450)
    if(int(sys.argv[1])<4):
        frame = cv2.rotate(frame, cv2.cv2.ROTATE_90_CLOCKWISE) 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    subjects = detect(gray, 0)
    for subject in subjects:
        shape = predict(gray, subject)

        #left
        ex=shape.part(36).x
        ew=shape.part(39).x

        ey=shape.part(37).y
        eh=shape.part(40).y

        #right
        ex1=shape.part(42).x
        ew1=shape.part(45).x

        ey1=shape.part(44).y
        eh1=shape.part(47).y

        shape = face_utils.shape_to_np(shape)#converting to NumPy Array
        
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0
        (x, y, w, h) = face_utils.rect_to_bb(subject)
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        frame[ey+eh:ey, ex:ex1+ew1]
        #cv2.rectangle(frame,(ex-20,ey-20),(ew1+20,eh1+20),(0,0,255),0)

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        #cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        #cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        roi_color = frame[y:y+h, x:x+w]
        croppedImg = frame[ey1-20:eh1+20, ex-20:ew1+20]
        if ear < thresh:
            flag += 1
            9- (flag)
            if flag >= frame_check:
                if(f1<=2000):
                    output_name = sys.argv[4]+"drowsy/"+str(f1)+".jpg"
                    cv2.putText(frame, "****************ALERT!****************", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    cv2.putText(frame, "****************ALERT!****************", (10,325),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    cv2.imwrite(output_name, croppedImg)
                    f1+=1
                #print ("Drowsy")
            
        else:
            if(f2<=2000):
                output_name = sys.argv[4]+"alert/"+str(f2)+".jpg"
                cv2.imwrite(output_name, croppedImg)
                flag = 0
                f2+=1
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cv2.destroyAllWindows()
cap.stop()