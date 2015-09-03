__author__ = 'adrian'
from PyQt4 import QtCore, QtGui
import sys


class myWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(myWindow, self).__init__(parent)
        myLayout = QtGui.QVBoxLayout(self)
        Button = QtGui.QPushButton('Resize')
        myLayout.addWidget(Button)
        Button.setMinimumWidth(200)
        self.setMaximumWidth(300)
        Button.clicked.connect(self.resizeDialog)

    def resizeDialog(self):
        self.animation = QtCore.QPropertyAnimation(self, "size")
        if self.size().width() == 200:
            self.animation.setEndValue(QtCore.QSize(600,300))
        else:
            print(3)
            self.animation.setEndValue(QtCore.QSize(400,100))
        self.animation.start()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('myApp')
    dialog = myWindow()
    dialog.resize(200, 100)
    dialog.show()
    sys.exit(app.exec_())