# -*- coding: utf-8 -*-
__author__ = 'adrian'
from PyQt4.QtGui import QPushButton, QMessageBox
from network.setip import dhcp
from message import Message


class DHCP(QPushButton):
    def __init__(self, id_, text, parent=None):
        super(DHCP, self).__init__(parent)
        self.ID = id_
        self.setText(text)
        self.setStyleSheet('''
            font: 9pt "Segoe UI";
            border-radius: 5px;
            background-color: white;
            color: lightgray;
            border: 1px solid lightgray;
        ''')

    def mousePressEvent(self, *args, **kwargs):
        print(self.ID)
        if self.ID == 'id':
            return
        out = dhcp(self.ID)
        Message.information(Message(), 'Error', out, '') if out.strip() else \
            Message.information(Message(), u'Éxito', 'Se ha establecido correctamente dhcp para la interfaz.', '')