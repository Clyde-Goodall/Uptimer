from win10toast import ToastNotifier as toast
import socket, schedule, json, time

class Uptimer:

    def __init__(self):

        self.duration = 0
        self.mute = False
        self.t = ToastNotifier()
        self.interval = 30
        self.disconnected = False 
        self.initial_disconnect = False
        # self.lastTime = None
        self.datetime = None
        self.resumed = False

    #notifies user connection is down
    def notify(self, msg):
        if(self.initial_disconnect):
            if(!self.mute):
                self.t.show_toast("Uptimer", msg, threaded=True, icon_path=None, duration=3)
                self.initial_disconnect = False

    #function for schedule to try connection every X amount of time
    def poll(self):

        try:
            host = socket.gethostbyname('1.1.1.1')
            sock = socket.create_connection((host, 80), 2)   

            if(self.diconnected):
                self.resumed = True
                self.disconnected = False
            else:
                self.resumed = False

            

        except:
            self.disconnected = True
            self.initial_disconnect = True
            self.msg = "Could not establish connecton to server, recording instance."
            print(self.msg)
            self.notify(self.msg)
            self.record()

    #writes to json
    def record(self):
        time = time.asctime(time.localtime(time.time()))


    def init_schedule(interval):


        schedule.every(30).seconds.do(self.poll())

        while True:
            schedule.run_pending()
