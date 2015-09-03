# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userinterface.ui'
#
# Created: Tue Jul 07 03:09:09 2015
# by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from labelerror import Label
from lineedit import LineEdit

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(735, 500)
        MainWindow.setFixedSize(735, 500)
        MainWindow.setWindowTitle(
            QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../res/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8(self.central_widget_css()))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
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
        self.line = QtGui.QFrame(self.widget)
        self.line.setFrameShadow(QtGui.QFrame.Raised)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.main_layout.addWidget(self.line)
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
        self.btn_set_ip.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_set_ip.setText(
            QtGui.QApplication.translate("MainWindow", "Guardar y ejecutar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_set_ip.setObjectName(_fromUtf8("btn_set_ip"))
        self.layout_button_box.addWidget(self.btn_set_ip)
        self.btn_only_save = QtGui.QPushButton(self.widget)
        self.btn_only_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_only_save.setText(
            QtGui.QApplication.translate("MainWindow", "Guardar y nada más", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_only_save.setObjectName(_fromUtf8("btn_only_save"))
        self.layout_button_box.addWidget(self.btn_only_save)
        self.layout_form.addLayout(self.layout_button_box)
        self.main_layout.addLayout(self.layout_form)
        self.wrapper_layout.addLayout(self.main_layout)
        self.layout_info_help = QtGui.QHBoxLayout()
        self.layout_info_help.setObjectName(_fromUtf8("layout_info_help"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.layout_info_help.addItem(spacerItem1)
        self.btn_options = QtGui.QPushButton(self.widget)
        self.btn_options.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_options.setStyleSheet(_fromUtf8(self.btn_help_info_options_css()))
        self.btn_options.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("res/opciones4.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_options.setIcon(icon1)
        self.btn_options.setIconSize(QtCore.QSize(41, 40))
        self.btn_options.setObjectName(_fromUtf8("btn_options"))
        self.layout_info_help.addWidget(self.btn_options)
        self.btn_info = QtGui.QPushButton(self.widget)
        self.btn_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_info.setStyleSheet(_fromUtf8(self.btn_help_info_options_css()))
        self.btn_info.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("res/info2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_info.setIcon(icon2)
        self.btn_info.setIconSize(QtCore.QSize(60, 60))
        self.btn_info.setObjectName(_fromUtf8("btn_info"))
        self.layout_info_help.addWidget(self.btn_info)
        self.btn_help = QtGui.QPushButton(self.widget)
        self.btn_help.setMaximumSize(QtCore.QSize(10777215, 16777215))
        self.btn_help.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_help.setToolTip(_fromUtf8(""))
        self.btn_help.setStyleSheet(_fromUtf8(self.btn_help_info_options_css()))
        self.btn_help.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("res/help2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_help.setIcon(icon3)
        self.btn_help.setIconSize(QtCore.QSize(60, 60))
        self.btn_help.setObjectName(_fromUtf8("btn_help"))
        self.layout_info_help.addWidget(self.btn_help)
        self.wrapper_layout.addLayout(self.layout_info_help)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_set_ip, self.btn_only_save)

        self.lbl_info = Label()
        self.layout_wrapper_tile = QtGui.QVBoxLayout()
        self.layout_tiles.addLayout(self.layout_wrapper_tile)
        self.layout_tiles.addStretch(1)

        self.layout_wrapper_tile.addWidget(self.lbl_info)
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



    def retranslateUi(self, MainWindow):
        pass

    @staticmethod
    def central_widget_css():
        return '''
            *{
                height: 40px;
            }
            #centralwidget{
                background-color: ghostwhite;
            }
            QLineEdit,
            QComboBox,
            QPushButton{
                font: 14pt \"Segoe UI\";
                border: 1px solid silver;
                padding-left: 10px;
                color: darkslategray;
            }
            #btn_set_ip{
                background-color: #16499A;
                color: lightgray;
                border: 1px solid lightgray;
            }
            #btn_only_save{
                background-color: #4390DF;
                color: lightgray;
                border: 1px solid lightgray;
            }
            #image_ifaces{
                width: 100px;
            }
        '''

    @staticmethod
    def btn_help_info_options_css():
        return '''
            border: 0px solid black;
            width: 40px;
            border-radius: 20px;
        '''

