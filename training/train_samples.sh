opencv_traincascade -data data \
-vec ../positive/positives.vex -bg ../negative/bg_train.txt \
-numPos 800 -numNeg 400 -numStages 10 -w 20 -h 20