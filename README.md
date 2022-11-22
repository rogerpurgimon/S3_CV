# S3_CV

## Task1 
If you already have all the 'mandanga' run the task1.py script with the following file name's configuration: `<codec>_<resolution>.<format>`(example h265_360x240.mp4)

  - codec: vp8, vp9, h265, av1
  - resolution: 720p, 480p, 360x240, 160x120
  - format: webm (vp8 and vp9), mp4 (h265), mkv(av1)
 
  And remember to put all the videos in the same directory as the scripts.
  When you run the script press `y` to execute the exercise. Then you can choose between 4 resolutions. Press `1/2/3/4`.
  The resulting output is the four-in-one video that compare the 4 codecs in your desired resolution.
  
If you want to run the application from the BBB 10 minute video (full process), name this file bbb.mp4 and uncomment the indicated lines in the script.

## Task2
This exercise aims to be a video converter.
First, when you run the task2.py file, the program will ask to execute the exercise 1. If you have already executed the first task just press `ǹ`.
Eventually, when the interface is shown on your screen, first, select the video resolution and then click on the codec you wish to convert your video.

## Results comments:
If we stop the video at 0:19, which coincides with a scene with multiple objects and have a lot of detail, we will notice some differences, for exemple, between VP8 and VP9, the sharpness of the reflected light on the rocks. In general all codecs outperforms the VP8 in terms of quality, even though, av1 encoding is so slow...



  
  
  
