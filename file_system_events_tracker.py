
import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/mingm/Downloads"
to_dir = "C:/Users/mingm/Desktop/Downloaded_Files"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpv', '.mp4', '.avi'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.cmd', '.msi', '.dmg']
}

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!!!")

    def on_deleted(self, event):
        print(f"Sorry, {event.src_path} has been deleted!")

    def on_modified(self, event):
        print(f"Someone modified {event.src_path}!")

    def on_moved(self, event):
        print(f"Someone moved {event.src_path}!")


event_handler = FileMovementHandler()


observer = Observer()

observer.schedule(event_handler, from_dir, recursive = True)

observer.start()


try :
    while True:
        time.sleep(2)
        print("running...")
    
except KeyboardInterrupt :
    print("stopped")
    observer.stop()