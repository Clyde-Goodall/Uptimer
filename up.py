from win10toast import ToastNotifier as toast
import socket, csv, time, schedule
from timeit import default_timer as timer
from datetime import datetime
import tray



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
        self.pause = False
        self.init_schedule()


    #notifies user connection is down
    def notify(self, msg):
        if(self.mute == False):
            self.t.show_toast("Uptimer", msg, threaded=True, icon_path="icon.ico", duration=3)
            self.initial_disconnect = False


    #function for schedule to try connection every X amount of time
    def poll(self):
        
        self.disc = 0
        try:
            host = socket.gethostbyname('1.1.1.1')
            sock = socket.create_connection((host, 80), 2)   
            print("Ping successful")
            
        #connection fails:
        except:
            if(self.disconnected == False):
                self.disc = timer()
                msg = "Could not establish connecton to server, recording instance."
                print(msg)     
                self.disconnected = True
                self.notify(msg)
        
        else:
            if(self.disconnected == True):
                self.disconnected = False
                
                self.time_of_outage = datetime.now().strftime("%I:%M:%S %p")
                self.elapsed = timer() - self.disc
                print("downtime: " + str(self.elapsed))
                self.record(self.time_of_outage, self.elapsed)
                self.notify("Connection back online")
                
                

            
                

    #writes to json
    def record(self, time, elapsed):
        print("Recording....")
        
        outage_date = datetime.now().strftime("%m/%d/%Y")
        #file write goes here
        with open('log.csv', 'a+', newline='') as c:
            writer = csv.writer(c)
            print("Instance recorded")
            writer.writerow([outage_date, time, elapsed])


    def init_schedule(self):

        schedule.every(self.interval).seconds.do(self.poll)

        while not self.pause:
            schedule.run_pending()
            time.sleep(1)
    