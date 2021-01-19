from multiprocessing import Process
import up, tray, view

def run_uptimer():
    background = Process(target=up.Uptimer, args=(5, False)).start()
    tray_menu = Process(target=tray.UptimerTray).start()

if __name__ == "__main__":
    run_uptimer()