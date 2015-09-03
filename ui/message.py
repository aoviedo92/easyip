__author__ = 'adrian'
from PyQt4.QtGui import QMessageBox, QIcon
import resources
# #16499A


class Message(QMessageBox):
    def __init__(self, background_color='#FBFBFB', color='#333', btn_background_color='#FBFBFB', btn_color='#333',
                 btn_border='#C1C1C1', size='11', parent=None):
        super(Message, self).__init__(parent)
        self.setWindowIcon(QIcon(':/info2.png'))

        self.setStyleSheet('''
            QMessageBox{
                color: %s;
                background-color: %s;
            }
            QLabel{
                color: %s;
                font: %spt "Segoe UI";
            }
            QPushButton{
                background-color: %s;
                width: 200px;
                height: 40px;
                border-radius: 4px;
                border: 1px solid %s;
                color: %s;
            }
            QPushButton:hover{
                background-color: %s;
            }
        ''' % (color, background_color, color, size, btn_background_color, btn_border, btn_color, btn_border))
