# -*- coding: utf-8 -*-

__author__ = 'adrian'
from PyQt4.QtGui import QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, QFrame, QCursor, \
    QGraphicsDropShadowEffect
from PyQt4.QtCore import Qt, QSize, SIGNAL, QPropertyAnimation

from data import del_data, load_data
from network.setip import set_ip
from message import Message


class NetConfigTile(QFrame):
    def __init__(self, id_, ad, nm, ip, ms='', gw='', dns='', parent=None):
        super(NetConfigTile, self).__init__(parent)
        self.animation = QPropertyAnimation(self, "size")
        self.setObjectName('tile')
        self.setCursor(QCursor(Qt.PointingHandCursor))

        effect = QGraphicsDropShadowEffect(self)
        effect.setOffset(0, 0)
        effect.setBlurRadius(20)
        self.setGraphicsEffect(effect)

        # self.setContextMenuPolicy(Qt.ActionsContextMenu)
        # action = QAction('edit', self)
        # self.addAction(action)
        self.setToolTip('interfaz:  %s\nnombre: %s\nip:            %s\nmascara: %s\ngateway: %s\ndns:         %s' % (
            ad, nm, ip, ms, gw, dns))

        self.setFixedWidth(300)
        self.setMinimumHeight(90)
        self.ID = id_

        self.lbl_nm = QLabel(nm)
        self.lbl_nm.setObjectName('lbl_nm')
        self.lbl_ad = QLabel(ad)
        self.lbl_ad.setObjectName('lbl_ad')
        self.lbl_ip = QLabel(ip)
        self.lbl_ip.setObjectName('lbl_ip')
        self.lbl_ms = QLabel(ms)
        self.lbl_ms.setObjectName('lbl_ms')
        self.lbl_gw = QLabel(gw)
        self.lbl_gw.setObjectName('lbl_gw')
        self.lbl_dns = QLabel(dns)
        self.lbl_dns.setObjectName('lbl_dns')

        layout_left = QVBoxLayout()
        layout_left.addWidget(self.lbl_ad)
        layout_left.addWidget(self.lbl_nm)
        layout_left.addWidget(self.lbl_ip)

        layout_lbl = QHBoxLayout()
        layout_lbl.addLayout(layout_left)

        self.btn_remove = QPushButton()
        self.btn_remove.setFixedSize(QSize(60, 60))
        self.btn_remove.setObjectName('btn_remove')
        self.btn_remove.setCursor(QCursor(Qt.ArrowCursor))

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.btn_remove, 1, 0)
        self.grid_layout.addLayout(layout_lbl, 1, 1, 1, 2)

        self.setLayout(self.grid_layout)
        self.setStyleSheet(self.load_style_sheet())

        self.connect(self.btn_remove, SIGNAL('released()'), self.remove_tile)

    def add_tile(self):
        self.setMinimumHeight(0)
        self.animation.setStartValue(QSize(300, 0))
        self.animation.setEndValue(QSize(300, 90))
        self.animation.start()
        self.connect(self.animation, SIGNAL('finished()'), self.restore_90)

    def restore_90(self):
        self.setFixedHeight(90)
        self.setMinimumHeight(90)

    def remove_tile(self):
        del_data(self.ID)
        dict_ = load_data()
        if dict_['config']:
            self.setMinimumHeight(0)
            self.animation.setStartValue(QSize(300, 90))
            self.animation.setEndValue(QSize(300, 0))
            self.animation.start()
            self.connect(self.animation, SIGNAL('finished()'), self.hide)

    def mousePressEvent(self, event):
        self.setFixedSize(300, 88)
        self.press_set_ip()

    def mouseReleaseEvent(self, event):
        self.setFixedSize(300, 90)

    @staticmethod
    def default_tile():
        return NetConfigTile('id', 'Interfaz de red...',
                             u'Nombre de la configuración...',
                             'IP para salvar...')


    def press_set_ip(self):
        out = set_ip(self.ID,
                     self.lbl_ip.text(),
                     self.lbl_ms.text(),
                     self.lbl_gw.text(),
                     self.lbl_dns.text())

        Message.information(Message(), 'Error', out, '') if out.strip() else \
            Message.information(Message(), u'Éxito', 'Se ha establecido correctamente el ip.', '')

    def released_set_ip(self):
        self.setFixedSize(300, 108)

    @staticmethod
    def load_style_sheet():
        return '''
            #tile{
                border-left: 3px solid lightgray;
                /*border-bottom: 1px solid lightgray;*/
                border-top: 0;
                margin: 0;
                background-color: #FFA500;
            }
            #group{
                font: 14pt "Segoe UI";
            }
            #tile:hover {
                border-radius: 5px;
                border: 0;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                    stop:0 white, stop: 0.6 #f2f2f2, stop:1 white)
            }
            #btn_remove {
                background-image: url(":/remove.png");
                border: 2px solid gray;
                border-radius: 30px;
            }
            #btn_remove:hover {
                background-image: url(":/remove_press.png");
            }
            QLabel{
                color: #333;
            }
            QToolTip{
                /*padding: 5px;*/
                background-color: white;
                border: 1px solid #16499A;
                border-radius: 5px;
                height: 150px;
            }
            #lbl_nm{
                font: 12pt "Segoe UI";
            }
            #lbl_ad{
                font: 8pt "Segoe UI";
            }
            #lbl_ip{
                font: 16pt "Segoe UI";
            }
            '''


# B94A48
class Line(QFrame):
    def __init__(self, parent=None):
        super(Line, self).__init__(parent)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Raised)
        self.setStyleSheet('background-color: gainsboro; '
                           'border: 1px solid ghostwhite;')