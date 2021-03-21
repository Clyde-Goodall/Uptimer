import csv, sys


from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes

class ViewLog(QtWidgets.QWidget):
    def __init__(self, fileName, parent=None):
        self.id = "uptimer"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(self.id)

        super(ViewLog, self).__init__(parent)
        self.fileName = "log.csv"


        self.model = QtGui.QStandardItemModel(self)

        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.resize(350, 500)

        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.tableView)


        self.loadCsv(fileName)

    def loadCsv(self, fileName):
        self.columns = ['Date', 'Time']
   
        with open(fileName, "r") as fileInput:
            
            for row in csv.reader(fileInput):   
   
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)
        for c in range(2):
            self.model.setHeaderData(c, QtCore.Qt.Horizontal, self.columns[c])

    # def buildGraph(self, data):
    #     #todo

if __name__ == "__main__":
    import sys
    filename = "log.csv"
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Uptimer")
    app.setWindowIcon(QtGui.QIcon("icon.ico"))

    main = ViewLog("log.csv")
    main.show()

    sys.exit(app.exec_())