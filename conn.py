from win10toast import ToastNotifier as toast
import socket, schedule, json, time
from datetime import date

#Entire uptimer class
class Uptimer:

    def __init__(self, interval, mute):

        self.duration = 0
        self.mute = mute
        self.t = toast()
        self.interval = interval
        self.disconnected = False 
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

        try:
            host = socket.gethostbyname('1.1.1.1')
            sock = socket.create_connection((host, 80), 2)   
            print("Ping successful")
            if(self.diconnected):
                self.disconnected = False

            
        #connection fails:
        except:
            if(self.disconnected == False):
                msg = "Could not establish connecton to server, recording instance."
                print(msg)     
                self.record()
                self.notify(msg)
            self.disconnected = True
            
              


    #writes to json
    def record(self):
        
        data = json.dumps(
                {
                    
                   date.today().strftime("%m/%d/%Y")  :  time.localtime(time.time()) 

                }
            )

        #file write goes here
        with open('log.json', 'r') as r:
            f = r.read()
        
        j = json.loads(f)
        j.update(data)
        
        with open('log.json', 'w') as out:
            out.write(json.dumps(j))

    def init_schedule(self):

        schedule.every(self.interval).seconds.do(self.poll)

        while True:
            schedule.run_pending()
            time.sleep(1)

Uptimer(2, False)