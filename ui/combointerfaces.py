__author__ = 'adrian'
from PyQt4.QtGui import QComboBox, QIcon
import resources


class Combo(QComboBox):
    def __init__(self, ipconfig, parent=None):
        super(Combo, self).__init__(parent)
        self.ipconfig = ipconfig
        self.addItem('Seleccione una interfaz de red.')
        self.add_items()

    def add_items(self):
        global icon
        for config in self.ipconfig:
            try:
                if config[1] == 'disconnected' and config[3] == 'lan':
                    icon = ':/lan_dis.png'
                if config[1] == 'disconnected' and config[3] == 'wlan':
                    icon = ':/wifi_dis.png'
                if config[1] == 'connected' and config[3] == 'lan':
                    icon = ':/lan_con.png'
                if config[1] == 'connected' and config[3] == 'wlan':
                    icon = ':/wifi_con.png'
                if config[1] == 'connected' and config[3] == 'bluetooth':
                    icon = ':/bluetooth_con.png'
                if config[1] == 'disconnected' and config[3] == 'bluetooth':
                    icon = ':/bluetooth_dis.png'
                self.addItem(QIcon(icon), config[4])
            except NameError:
                self.addItem(QIcon(':/help.png'), config[4])

    def update_items(self, ipconfig):
        self.ipconfig = ipconfig
        while self.count() > 1:
            self.removeItem(1)
        self.add_items()