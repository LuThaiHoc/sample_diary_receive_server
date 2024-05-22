import requests

url = 'http://localhost:5000/upload_diary'
data = {
    'name': 'UPDATE NEW POSITION',
    'team': 'BLUE',
    'from_user': 'alex',
    'location': 'location1',
    'time': '2024-05-20T12:34'
}
files = {'media': open('./diary.py', 'rb')}

response = requests.post(url, data=data, files=files)
print(response.json())