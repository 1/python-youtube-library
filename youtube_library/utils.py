def get(root, *keys):
    """
    Returns root[key1]...[keyn] if all keys are valid, otherwise
    returns None
    """
    for key in keys:
        try:
            root = root[key]
        except (KeyError, IndexError):
            return None
    return root

def url_creator(feed_type, yt_id):
    """
    Given a feed type (e.g video, playlist, or user) and an ID (of a
    video, playlist, or user), this function returns the URL to fetch
    the feed.
    """
    if feed_type == 'video':
        url = 'https://gdata.youtube.com/feeds/api/videos/%s?' % yt_id
        query_parameters = 'v=2&alt=json'
    elif feed_type == 'playlist':
        url = 'https://gdata.youtube.com/feeds/api/playlists/%s?' % yt_id
        query_parameters = 'v=2&alt=json&max-results=50'
    elif feed_type == 'user':
        url = 'https://gdata.youtube.com/feeds/api/users/%s/playlists?' % yt_id
        query_parameters = 'v=2&alt=json&max-results=50'
    else:
        raise Exception('No such feed type!')
    return url + query_parameters
    
