__author__ = 'adrian'
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Label(QLabel):
    def __init__(self, type_='', parent=None):
        super(Label, self).__init__(parent)
        self.type_ = type_
        self.setVisible(False)


    def setType_(self, type_):
        self.type_ = type_
        if self.type_ == 'error':
            self.setStyleSheet(self.common_style() + self.error_style())
        elif self.type_ == 'info':
            self.setStyleSheet(self.common_style() + self.info_style())

    @staticmethod
    def error_style():
        return '''
            color: #9A1616;
            '''

    @staticmethod
    def info_style():
        return '''
            background-color: #4390DF;
            padding: 10px;

        '''

    @staticmethod
    def common_style():
        return '''
            color: lightgray;
            padding: 2px;
            border-radius: 4px;
            '''