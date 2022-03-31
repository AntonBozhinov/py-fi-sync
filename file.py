import requests
from watchdog.events import FileSystemEventHandler


class FileEventHandler(FileSystemEventHandler):
    def __init__(self, url: str):
        self.url = url

    def on_created(self, event):
        file_name = event.src_path.split('/')[-1]
        print(f'[INFO] {file_name} has been created')
        upload(event.src_path, self.url)


def upload(file: str, url: str):
    with open(file, "rb") as f:
        res = requests.post(url, files={"file": f})
        if not res.ok:
            print(f'[ERROR] Upload file failed with status code: {res.status_code}')
        print(res.json())
        return res.json()
