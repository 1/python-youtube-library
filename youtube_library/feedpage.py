from utils import get, url_creator
import json
from urllib import urlopen

class VideoFeed(object):
    @classmethod
    def from_id(cls, video_id):
        try:
            feed = json.loads(urlopen(url_creator('video', video_id)).read())
            return cls(feed.get('entry'))
        except ValueError:
            raise Exception('Invalid video ID: %s' % video_id)

    def get(self, *keys):
        return get(self.data_dict, *keys)

    def __init__(self, video_feed_dict):
        self.data_dict = video_feed_dict


class ManyPageFeed(object):
    def __iter__(self):
        while True:
            yield self
            if self.is_last_page():
                raise StopIteration
            self = ManyPageFeed(self.get('link', -1, 'href'))

    def __init__(self, url):
        self.data_dict = json.loads(urlopen(url).read()).get('feed')

    def get(self, *keys):
        return get(self.data_dict, *keys)

    def is_last_page(self):
        return self.get('link', -1, 'rel') != 'next'

