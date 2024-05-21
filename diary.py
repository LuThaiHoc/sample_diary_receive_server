# dairy: 
from PyQt5.QtCore import QDateTime

from enum import Enum

class DiaryMediaType(Enum):
    IMAGE = "image"
    VIDEO = "video"
    FILE = "file"

class Diary:
    def __init__(self, id="", session_id="", team = "", name="", from_user="", location="", time=QDateTime.currentDateTime(), media="", media_type="", media_filename="", time_insert=QDateTime.currentDateTime()):
        self.id = id
        self.session_id = session_id
        self.team = team
        self.name = name
        self.from_user = from_user
        self.location = location
        self.time : QDateTime = time # time is QDatetime
        self.media = media # media can be image, video, file, need to save it in postgresql
        self.media_type = media_type
        self.media_filename = media_filename
        self.time_insert : QDateTime = time_insert
        
    def print_info(self):
        print("id: ",self.id)
        print("session_id: ",self.session_id)
        print("team: ",self.team)
        print("name: ",self.name)
        print("from_user: ",self.from_user)
        print("location: ",self.location)
        print("time: ",self.time)
        print("media: ",self.media)
        print("media_type: ",self.media_type)
        print("media_filename: ",self.media_filename)
        print("time_insert: ",self.time_insert)
        
    def save_media(self, file_path):
        if self.media is not None:
            try:
                with open(file_path, 'wb') as file:
                    file.write(self.media)
                print(f"Media saved : {file_path}")
            except IOError as e:
                print(f"Error saving media to file: {e}")
        else:
            print("No media data to save.")