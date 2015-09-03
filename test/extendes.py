from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys


class ExtendedQLabel(QLabel):
    def __init__(self, img, size=(20, 20), parent=None):
        QLabel.__init__(self, parent)
        print(2)
        self.setScaledContents(True)
        self.resize(size[0], size[1])
        self.setPixmap(QPixmap(img))
        # self.set_image()

    def mouseReleaseEvent(self, ev):
        self.emit(SIGNAL('released()'))

    def mousePressEvent(self, QMouseEvent):
        self.emit(SIGNAL('clicked()'))

        # def wheelEvent(self, ev):
        # self.emit(SIGNAL('scroll(int)'), ev.delta())


class MainUI(QWidget):
    BUTTON_IMAGE = '../res/plus.png'

    def __init__(self, parent=None):
        super(MainUI, self).__init__(parent)
        print(3)
        self.resize(600, 600)
        layout = QVBoxLayout()
        self.ImageButton = ExtendedQLabel('../res/plus.png', (100, 100))
        self.ImageButton.setMaximumWidth(300)
        self.ImageButton.setMaximumHeight(300)
        layout.addWidget(self.ImageButton)
        self.setLayout(layout)

        self.connect(self.ImageButton, SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.ImageButton, SIGNAL('released()'), self.buttonR)
        # self.connect(self.ImageButton, SIGNAL('scroll(int)'), self.wheelScrolled)


    def buttonClicked(self):
        print('Button Clicked')

    def buttonR(self):
        print('Button R')

        # def wheelScrolled(self, scrollAmount):
        # scrollAmount /= 10
        #     self.ImageButton.resize(self.width() + scrollAmount, self.height() + scrollAmount)
        #     self.resize(self.ImageButton.size())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainUI()
    win.show()
    app.exec_()
    sys.exit()
