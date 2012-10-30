from feedpage import ManyPageFeed
from video import Video
from utils import url_creator

class Playlist(object):
    """
    Class for representing a YouTube playlist. To instantiate, simply
    pass the ID of the playlist you want. The constructor will
    return an object representing that playlist.
    """
    def __repr__(self):
        return 'Playlist(playlist_id="%s")' % self.id

    def __init__(self, playlist_id):
        playlist_feed = ManyPageFeed(url_creator('playlist', playlist_id))
        self.id = playlist_id
        self.title = playlist_feed.get('title', '$t')
        self.subtitle = playlist_feed.get('subtitle', '$t')
        self.user = playlist_feed.get('author', 0, 'name', '$t')
        self.summary = playlist_feed.get('content', '$t')
        self.num_videos = playlist_feed.get('openSearch$totalResults','$t')
        self.videos = []

        for page in playlist_feed:
            if not page.get('entry'):
                continue
            for video_data_dict in page.get('entry'):
                self.videos.append(Video(video_dict=video_data_dict))
