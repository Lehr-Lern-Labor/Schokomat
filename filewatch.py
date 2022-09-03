import pyinotify
from time import sleep

notifier = None

class MyEventHandler(pyinotify.ProcessEvent):
    def __init__(self, start_funktion):
        self.start_funktion = start_funktion
    def process_IN_CLOSE_WRITE(self, event):
        print("Neuer Automat hochgeladen:", event.pathname)
        self.start_funktion()

def start_watch(start_funktion):
    global notifier
    # watch manager
    wm = pyinotify.WatchManager()
    wm.add_watch('/home/pi/schokomat/uploads/automat.json', pyinotify.ALL_EVENTS, rec=True)

    # event handler
    eh = MyEventHandler(start_funktion)

    # notifier
    notifier = pyinotify.ThreadedNotifier(wm, eh)
    notifier.start()

def stop_watch():
    global notifier
    notifier.stop()

if __name__ == '__main__':
    start_watch(print)
    while True:
        sleep(1)