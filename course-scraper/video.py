from feedpage import VideoFeed

class Video(object):
    """
    Class for representing a YouTube Video. This class can be
    instantiated with either a video ID or a key-value pair dictionary
    containing video data. If an ID is provided, then the properties
    of this video will automatically be fetched from YouTube
    """
    def __repr__(self):
        return 'Video(video_id="%s")' % self.id

    def __init__(self, video_id=None, **kwargs):
        if video_id:
            video_feed = VideoFeed.from_id(video_id)
        elif 'video_dict' in kwargs:
            video_feed = VideoFeed(kwargs['video_dict'])
        else:
            raise TypeError('argument to Video.__init__() must be a video ID')

        self.id = video_feed.get('media$group', 'yt$videoid', '$t')
        self.title = video_feed.get('media$group', 'media$title', '$t')
        self.summary = video_feed.get('media$group', 'media$description', '$t')
        self.keywords = video_feed.get('media$group', 'media$keywords', '$t')
        self.duration = video_feed.get('media$group', 'yt$duration', 'seconds')
        self.thumbnails = video_feed.get('media$group', 'media$thumbnail')
        self.rating = video_feed.get('gd$rating', 'average')
        self.num_raters = video_feed.get('gd$rating', 'numRaters')
