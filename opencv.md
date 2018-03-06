- collect negative imgs
- collect positive imgs
- annotate positive imgs with OpenCV integrated annotation tool

      opencv_annotation --annotations=/path/to/annotations/file.txt --images=/path/to/image/folder/
      /home/cshe6391/Tools/opencv-3.3.0/build/bin/opencv_annotation --annotations=./info.dat --images=positive/

- generate vex file from positive imgs

      //from existing photo collection
      opencv_createsamples -info -num -vec
      /home/cshe6391/Tools/opencv-3.3.0/build/bin/opencv_createsamples -info ./info.dat -num 5 -vec ./positive.vex

      //from one picture
      opencv_createsamples -img -bg -num -vec
      /home/cshe6391/Tools/opencv-3.3.0/build/bin/opencv_createsamples -img ./img.jpg -bg ./bg.txt -num 20 -vec ./positive.vex


- train cascade model

      opencv_traincascade -data
      /home/cshe6391/Tools/opencv-3.3.0/build/bin/opencv_traincascade -data ./trained -vec ./positive.vex -bg ./negative
