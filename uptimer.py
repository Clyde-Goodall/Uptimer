from win10toast import ToastNotifier as toast
import socket, schedule, csv, time
from timeit import default_timer as timer
from datetime import date

#Entire uptimer class
class Uptimer:

    def __init__(self, interval, mute):

        self.duration = 0
        self.mute = mute
        self.t = toast()
        self.interval = interval
        self.disconnected = False 
        self.recording = False
        # self.lastTime = None
        self.datetime = None
      
        self.init_schedule()


    #notifies user connection is down
    def notify(self, msg):
        if(self.mute == False):
            self.t.show_toast("Uptimer", msg, threaded=True, icon_path=None, duration=3)
            self.initial_disconnect = False


    #function for schedule to try connection every X amount of time
    def poll(self):
        
        self.disc = 0
        try:
            host = socket.gethostbyname('1.1.1.1')
            sock = socket.create_connection((host, 80), 2)   
            print("Ping successful")
            if(self.disconnected == True):
                # self.recording = False
                self.disconnected = False
                
                self.time_of_outage = time.localtime(time.time()) 
                self.elapsed = timer() - self.disc
                self.record(self.time_of_outage, self.elapsed)
                
                

            
        #connection fails:
        except:
            if(self.disconnected == False):
                self.disc = timer()
                msg = "Could not establish connecton to server, recording instance."
                print(msg)     
                self.disconnected = True
                # self.recording = True
                self.notify(msg)
                

    #writes to json
    def record(self, time, elapsed):
        print("Recording....")
        
        date = date.today().strftime("%m/%d/%Y")
        #file write goes here
        with open('log.csv', 'w') as c:
            writer = cvs.writer(c)
            print("Instance recorded")
            writer.writerow({'Date' : date, 'Time' : time, 'Downtime' : elapsed})


    def init_schedule(self):

        schedule.every(self.interval).seconds.do(self.poll)

        while True:
            schedule.run_pending()
            time.sleep(1)

Uptimer(5, False)