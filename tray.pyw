from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, os, up, platform
# from multiprocessing import Process
import subprocess
from subprocess import Popen, PIPE

class UptimerTray():


    #initialization
    def __init__(self):
        
        #platform-specific subprocess window flags (Currently only specified for windows)
        self.startupinfo = None
        if platform.system() == 'Windows':
            self.platform_info = subprocess.STARTUPINFO()
            self.platform_info.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        self.uptimer_tray_application = QApplication(sys.argv)
        self.uptimer_tray_application.setQuitOnLastWindowClosed(False)
        self.window = QWidget()

        #tray menu icon
        self.icon = QIcon("icon.png")
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(self.icon)
        self.tray.setVisible(True)

        #tray menu/menu items
        self.menu = QMenu()
        self.menu_view = QAction("View Log")
        self.menu_start = QAction("Start")
        self.menu_pause  = QAction("Pause")
        self.menu_exit = QAction("Exit")
        
        self.menu_view.triggered.connect(self.view_log)
        self.menu_exit.triggered.connect(self.shut_down)
        self.menu_start.triggered.connect(self.start)
        self.menu_pause.triggered.connect(self.pause)

        #Menu actions
        self.menu.addAction(self.menu_view)
        self.menu.addSeparator()
        self.menu.addAction(self.menu_start)
        self.menu.addAction(self.menu_pause)
        self.menu.addSeparator()
        self.menu.addAction(self.menu_exit)

        #append menu to tray application
        self.tray.setContextMenu(self.menu)

        self.start()

        self.uptimer_tray_application.exec_()


    def view_log(self):
        try:
            self.window = Popen(['python', 'C:/Users/gooda/Documents/DEV/connection-tester/view.py'], shell=True)    
            print("Viewing log")
        except Exception as e:
            print(e)


    def shut_down(self):
        try:
            print("Shutting down")
            self.background.terminate()
            self.uptimer_tray_application.quit()
        except:
            print("Unable to start Uptimer background task")


    def start(self):
        try:
            self.background = Popen(['python', 'C:/Users/gooda/Documents/DEV/connection-tester/up.py'], shell=False, startupinfo=self.platform_info)
            self.menu_start.setEnabled(False)
            self.menu_pause.setEnabled(True)
            print("Started")
        except:
            print("Unable to start Uptimer background task")
     

    def pause(self):
        try:
            self.background.terminate()
            self.menu_start.setEnabled(True)
            self.menu_pause.setEnabled(False)
            print("Paused")
        except:
            print("Background process likely not initialized, unable to pause.")
        

if __name__ == "__main__":
        UptimerTray()
