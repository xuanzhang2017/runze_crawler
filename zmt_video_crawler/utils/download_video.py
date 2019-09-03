import requests
from utils.user_agents import headers


def download(video_url, video_path):
    try:
        resp = requests.get(video_url, headers=headers)
    except:
        return False
    with open(video_path, 'wb') as f:
        f.write(resp.content)
    return True
