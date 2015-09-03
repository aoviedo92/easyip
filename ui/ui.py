# -*- coding: utf-8 -*-

import ctypes
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL
from labelerror import Label
from lineedit import LineEdit
from imagebutton import ImageButton
import resources

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

APP_ID = 'dev$oviedo.easyIP-PyQt4.v1.0'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(735, 500)
        MainWindow.setFixedSize(735, 500)
        MainWindow.setWindowTitle("EasyIP")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8(self.set_style_qss()))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(4, 6, 721, 491))
        self.widget.setObjectName(_fromUtf8("widget"))

        self.wrapper_layout = QtGui.QVBoxLayout(self.widget)
        self.wrapper_layout.setMargin(0)
        self.wrapper_layout.setObjectName(_fromUtf8("wrapper_layout"))

        self.main_layout = QtGui.QHBoxLayout()
        self.main_layout.setObjectName(_fromUtf8("main_layout"))

        self.layout_tiles = QtGui.QVBoxLayout()
        self.layout_tiles.setObjectName(_fromUtf8("layout_tiles"))
        self.main_layout.addLayout(self.layout_tiles)

        # self.line = QtGui.QFrame(self.widget)
        # self.line.setFrameShadow(QtGui.QFrame.Raised)
        # self.line.setFrameShape(QtGui.QFrame.VLine)
        # self.line.setFrameShadow(QtGui.QFrame.Sunken)
        # self.line.setObjectName(_fromUtf8("line"))
        # self.main_layout.addWidget(self.line)


        self.layout_form = QtGui.QVBoxLayout()
        self.layout_form.setObjectName(_fromUtf8("layout_form"))
        self.layout_dchp = QtGui.QHBoxLayout()
        self.layout_dchp.setObjectName(_fromUtf8("layout_dchp"))
        self.layout_form.addLayout(self.layout_dchp)

        spacerItem = QtGui.QSpacerItem(635, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.layout_form.addItem(spacerItem)

        self.layout_lineedit = QtGui.QVBoxLayout()
        self.layout_lineedit.setObjectName(_fromUtf8("layout_lineedit"))
        self.layout_form.addLayout(self.layout_lineedit)

        self.layout_button_box = QtGui.QHBoxLayout()
        self.layout_button_box.setObjectName(_fromUtf8("layout_button_box"))

        self.btn_set_ip = QtGui.QPushButton(self.widget)
        self.btn_set_ip.setText("Guardar y ejecutar")
        self.btn_set_ip.setObjectName(_fromUtf8("btn_set_ip"))
        # self.btn_set_ip = ImageButton(':/pin.png')
        self.layout_button_box.addWidget(self.btn_set_ip)

        self.btn_only_save = QtGui.QPushButton(self.widget)
        self.btn_only_save.setText(u"Guardar y nada más")
        self.btn_only_save.setObjectName(_fromUtf8("btn_only_save"))
        # self.btn_only_save = ImageButton(':/plus.png')
        self.layout_button_box.addWidget(self.btn_only_save)

        self.layout_form.addLayout(self.layout_button_box)
        self.main_layout.addLayout(self.layout_form)
        self.wrapper_layout.addLayout(self.main_layout)

        self.layout_info_help = QtGui.QHBoxLayout()
        self.layout_info_help.setObjectName(_fromUtf8("layout_info_help"))

        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.layout_info_help.addItem(spacerItem1)

        # self.layout_button_box.addStretch(1)

        self.btn_options = ImageButton(':/opciones.png')
        self.btn_options.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.layout_info_help.addWidget(self.btn_options)
        # self.layout_button_box.addWidget(self.btn_options)

        self.btn_info = ImageButton(':/info.png')
        self.btn_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.layout_info_help.addWidget(self.btn_info)
        # self.layout_button_box.addWidget(self.btn_info)

        self.btn_reload = ImageButton(':/reload.png', ':/reload_press.png')
        self.btn_reload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.layout_info_help.addWidget(self.btn_reload)
        # self.layout_button_box.addWidget(self.btn_help)

        self.wrapper_layout.addLayout(self.layout_info_help)

        self.layout_wrapper_tile = QtGui.QVBoxLayout()
        self.layout_tiles.addLayout(self.layout_wrapper_tile)
        self.layout_tiles.addStretch(1)

        self.lbl_err_combo = Label()
        self.lbl_err_nm = Label()
        self.lbl_err_ad = Label()
        self.lbl_err_ip = Label()
        self.lbl_err_ms = Label()
        self.lbl_err_gw = Label()
        self.lbl_err_dns = Label()

        self.line_nm = LineEdit('Nombre.', ['required'])
        self.line_ip = LineEdit('Ip.', ['required', 'ip'])
        self.line_ms = LineEdit(u'Máscara.', ['required', 'ms'])
        self.line_gw = LineEdit('Puerta de enlace...', ['ip'])
        self.line_dns = LineEdit('Servidor dns...', ['ip'])

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_set_ip, self.btn_only_save)

    def retranslateUi(self, MainWindow):
        pass

    @staticmethod
    def set_style_qss():
        return '''
            *{
                height: 40px;
            }
            #centralwidget{
                background-color: white;
            }
            QLineEdit,
            QComboBox,
            QCheckBox,
            QSpinBox,
            QPushButton{
                font: 12pt \"Segoe UI\";
                border: 1px solid silver;
                padding-left: 10px;
                color: #333;
            }
            QComboBox:editable {
                background: white;
            }
            QComboBox::drop-down {
                border: 1px solid white;
                width: 25px;
            }
            QComboBox::down-arrow {
                image: url(:/downarrow.png);
            }
            QComboBox::down-arrow:on{
                image: url(:/uparrow.png);
            }
            QComboBox:!editable:on, QComboBox::drop-down:editable:on {
                border: 1px solid #16499A;
                border-bottom: 0;
            }
            QComboBox QAbstractItemView {
                border: 1px solid #16499A;
                selection-background-color: lightgray;
                border-top: 0;
                padding: 3px;
                font-size: 7pt \"Segoe UI\";
            }
            QPushButton{
                border-radius: 4px;
                width: 200px;
                background-color: #FBFBFB;
            }
            QPushButton:hover{
                background-color: #C1C1C1;
            }
            #btn_only_save, #btn_ok{
                background-color: #4390DF;
                color: #FBFBFB
            }
            #btn_only_save:hover, #btn_ok:hover{
                background-color: #16499A;
            }
            Options{
                background-color: white;
                padding: 10px;
            }
            Options QCheckBox {
                border: 0;
                padding-left: 0;
            }
            Options QLabel{
                font: 12pt \"Segoe UI\";
                color: darkslategray;
            }
            QSpinBox {
                padding-top: 3px;
                padding-bottom: 3px;
            }
            QSpinBox::up-button {
                background-repeat: no-repeat;
                background-image: url(:/uparrow.png);
                border: 0;
                margin-top: 4px;
                margin-right: 4px;
                width: 10px;
            }
            QSpinBox::down-button{
                margin-right: 4px;
                width: 10px;
                background-repeat: no-repeat;
                background-image: url(:/downarrow.png);
                border: 0;
            }
            QCheckBox::indicator {
                width: 15px;
                height: 15px;
                border: 1px solid lightgray;
            }
            QCheckBox::indicator:checked {
                image: url(:/button_ok1.png);
            }
        '''

    @staticmethod
    def btn_help_info_options_css():
        return '''
            border: 0px solid black;
            width: 40px;
            border-radius: 20px;
        '''

