from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QLabel, QPixmap

__author__ = 'adrian'


class ImageButton(QLabel):
    def __init__(self, img, img_hover=False, size=(45, 45), parent=None):
        QLabel.__init__(self, parent)
        self.img = img
        self.img_hover = img_hover
        if not self.img_hover:
            self.img_hover = img
        self.setScaledContents(True)
        self.resize(size[0], size[1])
        self.setMaximumWidth(size[0])
        self.setMaximumHeight(size[1])
        self.setPixmap(QPixmap(img))
        # self.setStyleSheet(self.set_style_qss())

    def mouseReleaseEvent(self, event):
        self.setPixmap(QPixmap(self.img))
        self.emit(SIGNAL('released()'))

    def mousePressEvent(self, event):
        self.setPixmap(QPixmap(self.img_hover))
        self.emit(SIGNAL('clicked()'))

    def set_style_qss(self):
        return '''
            ImageButton:hover{
                /*background-image: url(:/info.png);*/
                border: 1px solid gray;
                border-radius: 25px;
            }
            '''