import sys
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RestartHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.start_process()

    def start_process(self):
        if self.process:
            self.process.kill()
        self.process = subprocess.Popen([sys.executable, self.script])

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f"Archivo modificado: {event.src_path}. Reiniciando bot...")
            self.start_process()

if __name__ == "__main__":
    path = "."
    script = "bot.py"  # Cambia al nombre de tu archivo principal

    event_handler = RestartHandler(script)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
