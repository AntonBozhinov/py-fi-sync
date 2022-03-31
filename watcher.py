import sys
import time
from watchdog.observers import Observer
from file import FileEventHandler


def watch_dir(path, url):
    event_handler = FileEventHandler(url)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python watcher.py <directory> <remote-url>")
        sys.exit(1)
    watch_dir(sys.argv[1], sys.argv[2])
