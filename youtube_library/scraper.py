import couchdb
import json
from user import User

def playlist_to_dict(playlist):
    plist_dict = playlist.__dict__
    plist_dict['date'] = [6, 14, 2012]
    plist_dict['videos'] = [video.__dict__ for video in plist_dict['videos']]
    return plist_dict

def create_database():
    db = couchdb.Server()['fresh_playlists']
    usernames = ['UCBerkeley', 'MIT', 'StanfordUniversity', 'Harvard', 'nptelhrd',
               'oxford', 'YaleUniversity', 'HarveyMuddCollegeEDU', 'khanacademy', 
               'MarakanaTechTV', 'nyu', 'columbiauniversity', 'PCCVideos', 
               'sheridan3003', 'UMKC', 'openmichigan', 'princetonuniversity', 
               'UCLACourses', 'proudlydismal', 'UCITLTC', 'UHouston', 'markthoma']
    for username in usernames:
        for playlist in User(username).playlists:
            db.save(playlist_to_dict(playlist))        

create_database()


    
