import os


def resize():
    """
    Create a script which can resize the BBB
    video into 4 differents video resolution.
    """

    #Cut the video
    cut = "ffmpeg -i bbb.mp4 -ss 00:00:00 -t 00:00:30 BBB.mp4"

    r1 = "ffmpeg -i BBB.mp4 -s hd720 -c:a copy bbb_720p.mp4"
    r2 = "ffmpeg -i BBB.mp4 -s hd480 -c:a copy bbb_480p.mp4"
    r3 = "ffmpeg -i BBB.mp4 -s 360x240 -c:a copy bbb_360x240.mp4"
    r4 = "ffmpeg -i BBB.mp4 -s 160x120 -c:a copy bbb_160x120.mp4"

    os.system(cut)
    os.system(r1)
    os.system(r2)
    os.system(r3)
    os.system(r4)

"""
    Convert them into VP8, VP9, h265 & AV1. You
    can use the script that allows you to transform, or
    create a new script. If not, you can do it manually
    """
#1MBit/s on average
def VP8(inputfile):
    match inputfile:
        case "bbb_720p.mp4":
            c = "ffmpeg -i bbb_720p.mp4 -c:v libvpx -b:v 1M vp8_720p.webm"
        case "bbb_480p.mp4":
            c = "ffmpeg -i bbb_480p.mp4 -c:v libvpx -b:v 1M vp8_480p.webm"
        case "bbb_360x240.mp4":
            c = "ffmpeg -i bbb_360x240.mp4 -c:v libvpx -b:v 1M vp8_360x240.webm"
        case "bbb_160x120.mp4":
            c = "ffmpeg -i bbb_160x120.mp4 -c:v libvpx -b:v 1M vp8_160x120.webm"
    os.system(c)

def VP9(inputfile):
    match inputfile:
        case "bbb_720p.mp4":
            c = "ffmpeg -i bbb_720p.mp4 -c:v libvpx-vp9 -b:v 1M vp9_720p.webm"
        case "bbb_480p.mp4":
            c = "ffmpeg -i bbb_480p.mp4 -c:v libvpx-vp9 -b:v 1M vp9_480p.webm"
        case "bbb_360x240.mp4":
            c = "ffmpeg -i bbb_360x240.mp4 -c:v libvpx-vp9 -b:v 1M vp9_360x240.webm"
        case "bbb_160x120.mp4":
            c = "ffmpeg -i bbb_160x120.mp4 -c:v libvpx-vp9 -b:v 1M vp9_160x120.webm"
    os.system(c)

def h265(inputfile):
    match inputfile:
        case "bbb_720p.mp4":
            c = "ffmpeg -i bbb_720p.mp4 -c:v libx265 -b:v 1M -c:a copy h265_720p.mp4"
        case "bbb_480p.mp4":
            c = "ffmpeg -i bbb_480p.mp4 -c:v libx265 -b:v 1M -c:a copy h265_480p.mp4"
        case "bbb_360x240.mp4":
            c = "ffmpeg -i bbb_360x240.mp4 -c:v libx265 -b:v 1M -c:a copy h265_360x240.mp4"
        case "bbb_160x120.mp4":
            c = "ffmpeg -i bbb_160x120.mp4 -c:v libx265 -b:v 1M -c:a copy h265_160x120.mp4"
    os.system(c)


def av1(inputfile):
    match inputfile:
        case "bbb_720p.mp4":
            c = "ffmpeg -i bbb_720p.mp4 -c:v libaom-av1 -b:v 1M av1_720p.mkv"
        case "bbb_480p.mp4":
            c = "ffmpeg -i bbb_480p.mp4 -c:v libaom-av1 -b:v 1M av1_480p.mkv"
        case "bbb_360x240.mp4":
            c = "ffmpeg -i bbb_360x240.mp4 -c:v libaom-av1 -b:v 1M av1_360x240.mkv"
        case "bbb_160x120.mp4":
            c= "ffmpeg -i bbb_160x120.mp4 -c:v libaom-av1 -b:v 1M av1_160x120.mkv"
    os.system(c)


def mandanga(option):
    match option:
        case 1:
            f1 = "vp8_160x120.webm"; f2 = "vp9_160x120.webm"; f3 = "h265_160x120.mp4"; f4 = "av1_160x120.mp4"
            filename = "mandanga_160x120.mkv"
        case 2:
            f1 = "vp8_360x240.webm"; f2 = "vp9_360x240.webm"; f3 = "h265_360x240.mp4"; f4 = "av1_360x240.mp4"
            filename = "mandanga_360x240.mkv"
        case 3:
            f1 = "vp8_480p.webm"; f2 = "vp9_480p.webm"; f3 = "h265_480p.mp4"; f4 = "av1_480p.mp4"
            filename = "mandanga_480p.mkv"
        case 4:
            f1 = "vp8_720p.webm"; f2 = "vp9_720p.webm"; f3 = "h265_720p.mp4"; f4 = "av1_720p.mp4"
            filename = "mandanga_720p.mkv"

    c = 'ffmpeg -i {0} -i {1} -i {2} -i {3} -filter_complex "nullsrc=size=1280x720 [base]; ' \
    '[0:v] setpts=PTS-STARTPTS, scale=640x360 [upperleft];' \
    '[1:v] setpts=PTS-STARTPTS, scale=640x360 [upperright]; ' \
    '[2:v] setpts=PTS-STARTPTS, scale=640x360 [lowerleft]; ' \
    '[3:v] setpts=PTS-STARTPTS, scale=640x360 [lowerright]; ' \
    '[base][upperleft] overlay=shortest=1 [tmp1]; ' \
    '[tmp1][upperright] overlay=shortest=1:x=640 [tmp2]; ' \
    '[tmp2][lowerleft] overlay=shortest=1:y=360 [tmp3]; ' \
    '[tmp3][lowerright] overlay=shortest=1:x=640:y=360' \
    '" ' \
    '-c:v libx264 {4}'.format(f1,f2,f3,f4, filename)

    os.system(c)



'''
------------------------------------------------------------------
If you don'have the 'mandanga' uncomment the following lines and remember to name bbb.mp4 the 10 minutes video.
'''
#resize()
#VP8("bbb_720p.mp4"); VP8("bbb_480p.mp4"); VP8("bbb_360x240.mp4"); VP8("bbb_160x120.mp4");
#VP9("bbb_720p.mp4"); VP9("bbb_480p.mp4"); VP9("bbb_360x240.mp4"); VP9("bbb_160x120.mp4");
#h265("bbb_720p.mp4"); h265("bbb_480p.mp4"); h265("bbb_360x240.mp4"); h265("bbb_160x120.mp4");
#av1("bbb_720p.mp4"); av1("bbb_480p.mp4"); av1("bbb_360x240.mp4"); av1("bbb_160x120.mp4");

'''
------------------------------------------------------------------
'''

mandanga(4) #choose resolution 1-2-3-4