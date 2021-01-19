from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import up
import sys

uptimer_ui = QApplication([])
uptimer_ui.setQuitOnLastWindowClosed(False)




def exit_program():
    Sys.exit("Closing")

icon = QIcon("icon.png")
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

menu = QMenu()
menu_exit = QAction("Exit")
menu_exit.triggered.connect(exit_program)
menu.addAction(menu_exit)

tray.setContextMenu(menu)


up.Uptimer(5, False)
uptimer_ui.exec_()
