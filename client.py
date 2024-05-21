import requests

url = 'http://localhost:5000/upload_diary'
data = {
    'id': '1',
    'session_id': 'session1',
    'team': 'team1',
    'name': 'diary1',
    'from_user': 'user1',
    'location': 'location1',
    'time': '2024-05-20 12:34:56',
    'media_type': 'image',
    'time_insert': '2024-05-20 12:34:56'
}
files = {'media': open('./map.png', 'rb')}

response = requests.post(url, data=data, files=files)
print(response.json())