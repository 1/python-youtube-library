from feedpage import ManyPageFeed
from utils import url_creator
from playlist import Playlist

class User(object):
    def __init__(self, username):
        feed = ManyPageFeed(url_creator('user', username))
        self.username = feed.get('author', 0, 'name', '$t')
        self.num_playlists = feed.get('openSearch$totalResults', '$t')
        self.playlists = []

        for page in feed:
            if not page.get('entry'):
                continue
            for playlist_dict in page.get('entry'):
                playlist_id = playlist_dict.get('yt$playlistId', {}).get('$t')
                self.playlists.append(Playlist(playlist_id))
