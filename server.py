from flask import Flask, render_template, request, jsonify
from datetime import datetime
from werkzeug.utils import secure_filename
import os
import mimetypes
from PyQt5.QtCore import QDateTime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

class Diary:
    def __init__(self, id="", session_id="", team="", name="", from_user="", location="", time=datetime.now(), media="", media_type="", media_filename="", time_insert=datetime.now()):
        self.id = id
        self.session_id = session_id
        self.team = team
        self.name = name
        self.from_user = from_user
        self.location = location
        self.time = time
        self.media = media
        self.media_type = media_type
        self.media_filename = media_filename
        self.time_insert = time_insert
    def show(self):
        print("id:", self.id)
        print("session_id:", self.session_id)
        print("team:", self.team)
        print("name:", self.name)
        print("from_user:", self.from_user)
        print("location:", self.location)
        print("time:", self.time)
        print("media:", self.media)
        print("media_type:", self.media_type)
        print("media_filename:", self.media_filename)
        print("time_insert:", self.time_insert)


diaries = []

@app.route('/upload_diary', methods=['POST'])
def upload_diary():
    data = request.form
    media = request.files['media']

    filename = secure_filename(media.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    media.save(filepath)
    
    media_binary_data = media.read()
    
    # Get media type
    media_type = mimetypes.guess_type(filename)[0]
    media_class = "file"
     # Classify media type
    if media_type:
        if media_type.startswith('image'):
            media_class = "image"
        elif media_type.startswith('video'):
            media_class = "video"
       

    diary = Diary(
        id=data.get('id', ''),
        session_id=data.get('session_id', ''),
        team=data.get('team', ''),
        name=data.get('name', ''),
        from_user=data.get('from_user', ''),
        location=data.get('location', ''),
        time=QDateTime(datetime.strptime(data.get('time'), '%Y-%m-%dT%H:%M')),
        media=media_binary_data,
        media_type=media_class,
        media_filename=filename,
        time_insert=QDateTime.currentDateTime()
    )

    diary.show()
    diaries.append(diary)

    return jsonify({'message': 'Diary entry created successfully'}), 201

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(host="localhost", port=5000, debug=True)