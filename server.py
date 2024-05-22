from flask import Flask, request, jsonify
from datetime import datetime
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

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

    diary = Diary(
        id=data.get('id', ''),
        session_id=data.get('session_id', ''),
        team=data.get('team', ''),
        name=data.get('name', ''),
        from_user=data.get('from_user', ''),
        location=data.get('location', ''),
        time=datetime.strptime(data.get('time'), '%Y-%m-%d %H:%M:%S'),
        media=filepath,
        media_type=data.get('media_type', ''),
        media_filename=filename,
        time_insert=datetime.strptime(data.get('time_insert'), '%Y-%m-%d %H:%M:%S')
    )
    diary.show()
    diaries.append(diary)

    return jsonify({'message': 'Diary entry created successfully'}), 201

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)