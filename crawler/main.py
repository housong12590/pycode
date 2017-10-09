from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from crawler.main_window import Ui_MainWindow

count = 0


def search():
    global count
    count += 1
    print(count)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    ui.btn_search.clicked.connect(search)
    ui.search_key.text()
    sys.exit(app.exec())
