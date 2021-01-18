from win10toast import ToastNotifier as toast
import time, socket, schedule

def notify(msg1, msg2, t):
    t.show_toast(msg1, msg2, threaded=True, icon_path=None, duration=3)

def poll():
    try:
        host = socket.gethostbyname('1.1.1.1')
        sock = socket.create_connection((host, 80), 2)
        