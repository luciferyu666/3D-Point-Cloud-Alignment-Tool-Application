from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'檔案 {event.src_path} 被修改了')

    def on_created(self, event):
        print(f'檔案 {event.src_path} 被創建了')

    def on_deleted(self, event):
        print(f'檔案 {event.src_path} 被刪除了')

if __name__ == "__main__":
    path = "/path/to/your/directory"
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
