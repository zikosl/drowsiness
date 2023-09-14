# drowsiness

First Part : Import DataSet
We use cv2 to get picture from training video

after this we pre trained model 68 landsmark to detect faces from frames & we use face_utile for get eye marks from model
 

We use this marks (6 for left eye / 6 for right ) to calculate the EAR
 
 
Then if ear<tresh ( random int <1) in this study we use 0,25
Then the system detect that it’s drowsy and save this image in the output 
Els
Save image in the folder name alert
 
Seconde Part 
we use the tensorflow Hub /image_classifier to create graph model with the collected data set 


then w use this graph to extract feature from the training data from CNN module and save it as sequence of matrix to use it as Input from LTSM
  
After this we run the  train.py to get the final predictions for the test sequence of data and the alarm will sound if the model predicts the sequence to be in a drowsy state.

 
For training Data / Testing Data
 
We use the production vector to get if the driver drowsy or no and play alarm
 

The Parametre :
 

