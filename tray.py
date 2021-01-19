from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, os, up
from multiprocessing import Process

class UptimerTray():

    def view_log():
        view.ViewLog().loadCsv()

    #initialization
    def __init__(self):


        self.uptimer_tray = QApplication([])
        self.uptimer_tray.setQuitOnLastWindowClosed(False)


        self.icon = QIcon("icon.png")
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(self.icon)
        self.tray.setVisible(True)

        #tray menu
        self.menu = QMenu()
        self.menu_exit = QAction("Exit")
        self.menu_exit.triggered.connect(os._exit)

        self.log = QAction("View Log")
        self.log.triggered.connect(self.view_log)

        self.menu.addAction(self.log)
        self.menu.addAction(self.menu_exit)

        self.tray.setContextMenu(self.menu)
        
        self.uptimer_tray.exec_()
        

if __name__ == "__main__":
    UptimerTray()
