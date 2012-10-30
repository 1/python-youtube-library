python-youtube-library
======================

An user-friendly python library for getting data from YouTube API.

Video Class:
============

Instantiate a video by providing a video ID to the Video constructor. The video ID of a video is an alphanumeric string of length 11. You can find the ID of a particular YouTube video by examining the query string of the video's URL; the ID is the value of the v parameter. For example, the ID of the video featured at 

    http://www.youtube.com/watch?v=7CYXy9J4Aao&feature=relmfu

is 7CYXy9J4Aao. Usage:

    >>>> import yt
    >>>> video = yt.Video('7CYXy9J4Aao')
    >>>> video.id
    '7CYXy9J4Aao'
    >>>> video.title
    '1. Introduction and Probability Review'
    >>>> video.duration
    '4587' # this is measured in seconds

Along with id, title, and duration, a video as the following properties: keywords, rating, thumbnails, num_raters, and summary.

Playlist Class:
===============

A playlist on YouTube is an ordered set of videos. Instantiate a playlist by providing a playlist ID to the Playlist constructor. The playlist ID of a playlist is an alphanumeric string of length 18. You can find the ID of a particular YouTube playlist by examining the query string of the playlist's URL; the ID is the value of the list parameter. For example, the ID of the playlist featured at

    http://www.youtube.com/watch?v=K-8nCXY-iSI&feature=edu&list=PL74058E54264993C8

is PL74058E54264993C8. Usage:

    >>>> import yt
    >>>> playlist = yt.Playlist('PL74058E54264993C8')
    >>>> playlist.id
    'PL74058E54264993C8'
    >>>> p.title
    'Electromagnetic Fields & Energy, Textbook Components w Video'
    >>>> p.user
    'MIT'
    >>>> p.videos 
    [Video(video_id="K-8nCXY-iSI"), Video(video_id="N46RKNbKf2s"), ... , Video(video_id="fz-jJahvwt8")]
    # a list of video objects

User Class:
===========

This class is used to represent a YouTube user. Every YouTube user has a unique ID (the account the user logs into). A user's page can be visited at the following URL:

    http://www.youtube.com/user/USER_ID
    
For example, MIT has a user account on YouTube; unsurprisingly, MIT's user ID is MIT. Thus, MIT's user page is:

    http://www.youtube.com/user/MIT
    
The User class is used to extract playlists uploaded by a particular user. A user object can be instantiated by passing a user ID into the User class's constructor. Usage:

    >>>> import yt
    >>>> user = yt.User('MIT')
    >>>> user.username
    'MIT'
    >>>> user.num_playlists
    117
    >>>> user.playlists
    [Playlist(playlist_id="PLUl4u3cNGP62RGk3NhGPDaOBLH9eRmjOL"), ... , Playlist(playlist_id="PLC2CEECFD938FD494")]
    # a list of playlist objects
    
    
    
    
    


