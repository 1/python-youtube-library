python-youtube-library
======================

An user-friendly python library for getting data from YouTube API.

Video Class:
Instantiate a video by providing a video ID to the Video constructor. The video ID of a video is an alphanumeric string of length 11. You can find the video ID of a particular YouTube video by examining the query string of the video's URL; the ID is value value of the v parameter. 

For example, the ID of the video at featured at 

    http://www.youtube.com/watch?v=7CYXy9J4Aao&feature=relmfu

is is 7CYXy9J4Aao.



    >>>> from video import Video
    >>>> video = Video('7CYXy9J4Aao')
