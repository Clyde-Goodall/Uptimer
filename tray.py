from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, os, up
# from multiprocessing import Process
from subprocess import Popen, PIPE

class UptimerTray():


    #initialization
    def __init__(self):
        self.background = None


        self.uptimer_tray_application = QApplication(sys.argv)
        self.uptimer_tray_application.setQuitOnLastWindowClosed(False)
        self.window = QWidget()
        self.window


        self.icon = QIcon("icon.png")
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(self.icon)
        self.tray.setVisible(True)

        #tray menu/menu items
        self.menu = QMenu()
        self.menu_start = QAction("Start")
        self.menu_pause  = QAction("Pause")
        self.menu_exit = QAction("Exit")
        
        self.menu_exit.triggered.connect(self.shut_down)
        self.menu_start.triggered.connect(self.start)
        self.menu_pause.triggered.connect(self.pause)

        #Menu actions
        self.menu.addAction(self.menu_start)
        self.menu.addAction(self.menu_pause)
        self.menu.addAction(self.menu_exit)

        self.tray.setContextMenu(self.menu)

        self.start()
        
        self.uptimer_tray_application.exec_()

 


    def shut_down(self):
        try:
            print("Shutting down")
            self.background.terminate()
            self.uptimer_tray_application.quit()
        except:
            print("Unable to start Uptimer background task")


    def start(self):
        try:
            self.background = Popen(['python', 'up.py'])
            print("Started")
        except:
            print("Unable to start Uptimer background task")
     

    def pause(self):
        try:
            self.background.terminate()
            print("Paused")
        except:
            print("Background process likely not initialized, unable to pause.")
        

if __name__ == "__main__":
        UptimerTray()
