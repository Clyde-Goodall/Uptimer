import csv, sys

from PyQt5 import QtCore, QtGui, QtWidgets

class ViewLog(QtWidgets.QWidget):
    def __init__(self, fileName, parent=None):
        super(ViewLog, self).__init__(parent)
        self.fileName = "log.csv"


        self.model = QtGui.QStandardItemModel(self)

        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.resize(700, 500)


        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.tableView)


        self.loadCsv(fileName)

    def loadCsv(self, fileName):
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):    
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)

if __name__ == "__main__":
    import sys
    filename = "log.csv"
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('Uptimer')

    main = ViewLog("log.csv")
    main.show()

    sys.exit(app.exec_())