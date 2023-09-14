

i=1
mkdir Output


while [ $i -le 4 ]
do
  mkdir Output/$i
  mkdir Output/$i/Alert

  echo "Alert $i"
  python3 eyedetection.py 1 /media/zakaria/GSP1RMCULXF/drowsy/$i/1.mp4 ./ Output/$i/Alert/
  i=$(($i + 1))
done

i=5

while [ $i -le 8 ]
do
  mkdir Output/$i/Drowsy
  echo "Drowsy $i"
  python3 eyedetection.py 1 /media/zakaria/GSP1RMCULXF/drowsy/$i/1.mp4 ./ Output/$i/Drowsy/


  i=$(($i + 1))
done
