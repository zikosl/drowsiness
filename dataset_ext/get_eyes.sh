

i=1
mkdir Output


while [ $i -le 8 ]
do
  mkdir Output/$i
  mkdir Output/$i/alert
  mkdir Output/$i/drowsy




  python3 detect_drowsiness.py $i /media/zakaria/GSP1RMCULXF/drowsy/$i/1.mp4 ./ Output/$i/
  i=$(($i + 1))
done
