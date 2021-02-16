import requests
from app import FlaskAppInstance
BASE = "http://127.0.0.1:5000/"



response_post = requests.put(BASE + "video/1", {"likes": 10})
print(response_post.json())