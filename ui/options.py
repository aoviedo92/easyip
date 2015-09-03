# coding=utf-8
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import QDialog, QIcon, QCheckBox, QCursor, QLabel, QSpinBox, QPushButton, QGridLayout

__author__ = 'adrian'
# from PyQt4.QtGui import *
# from PyQt4.QtCore import *
from data import load_data, save_options
from lineedit import LineEdit


class Options(QDialog):
    def __init__(self, parent=None):
        super(Options, self).__init__(parent)
        self.setWindowIcon(QIcon('res/opciones4.png'))
        self.setWindowTitle('Opciones')

        self.options = load_data()['options']

        self.chk_mask = QCheckBox(u'Máscara por defecto.')
        self.line_mask = LineEdit(u'máscara', ['required', 'ms'])
        self.line_mask.focusInEvent = lambda _: self.block_focus_event()

        if self.options[0]:
            self.chk_mask.setChecked(True)
            self.line_mask.setText(self.options[1])

        self.chk_dns = QCheckBox('Servidor dns por defecto.')
        self.line_dns = LineEdit('Servidor dns', ['required', 'ip'])
        self.line_dns.focusInEvent = lambda _: self.block_focus_event()
        self.line_mask.setCursor(QCursor(Qt.ForbiddenCursor))

        if self.options[2]:
            self.chk_dns.setChecked(True)
            self.line_dns.setText(self.options[3])

        self.status(self.chk_mask.isChecked(), self.line_mask)
        self.status(self.chk_dns.isChecked(), self.line_dns)

        lbl = QLabel('Cantidad de Configuraciones permitidas.')
        spin = QSpinBox()
        spin.setRange(1, 8)
        spin.setValue(self.options[4])
        spin.setMaximumWidth(50)
        lbl.setBuddy(spin)

        btn_ok = QPushButton('OK')
        btn_ok.setMaximumWidth(200)
        btn_ok.setObjectName('btn_ok')

        btn_cancel = QPushButton('Cancel')
        btn_cancel.setMaximumWidth(200)
        btn_cancel.setObjectName('btn_cancel')

        layout = QGridLayout()
        layout.addWidget(self.chk_mask, 0, 0, 1, 3)
        layout.addWidget(self.line_mask, 1, 0, 1, 3)
        layout.addWidget(self.chk_dns, 2, 0, 1, 3)
        layout.addWidget(self.line_dns, 3, 0, 1, 3)
        layout.addWidget(lbl, 4, 0)
        layout.addWidget(spin, 4, 1)
        layout.addWidget(QLabel(''), 5, 0)
        layout.addWidget(btn_cancel, 6, 1)
        layout.addWidget(btn_ok, 6, 2)
        self.setLayout(layout)

        self.connect(self.chk_mask, SIGNAL('clicked(bool)'), self.set_disable_mask)
        self.connect(self.chk_dns, SIGNAL('clicked(bool)'), self.set_disable_dns)
        self.connect(btn_ok, SIGNAL('clicked()'), self.save_and_exit)
        self.connect(btn_ok, SIGNAL('returnPressed()'), self.save_and_exit)
        self.connect(spin, SIGNAL('valueChanged(int)'), self.spin_value)
        self.connect(btn_cancel, SIGNAL("clicked()"), self.reject)

    def spin_value(self, value):
        self.options[4] = value

    def block_focus_event(self):
        return

    @staticmethod
    def status(check, line_edit):
        if check:
            line_edit.setStyleSheet('background-color: white')
            line_edit.setCursor(QCursor(Qt.IBeamCursor))
            line_edit.setDisabled(False)
        else:
            line_edit.setCursor(QCursor(Qt.ForbiddenCursor))
            line_edit.setStyleSheet('border: 2px solid lightgray; background-color: #f2f2f2')
            line_edit.setDisabled(True)

    def set_disable_mask(self):
        self.status(self.chk_mask.isChecked(), self.line_mask)

    def set_disable_dns(self):
        self.status(self.chk_dns.isChecked(), self.line_dns)

    def save_and_exit(self):
        mask_error = False
        dns_error = False
        if self.chk_mask.isChecked():
            mask_error = self.line_mask.validations()
        if self.chk_dns.isChecked():
            dns_error = self.line_dns.validations()
        if not mask_error and not dns_error:
            self.options[0] = self.chk_mask.isChecked()
            self.options[1] = str(self.line_mask.text())
            self.options[2] = self.chk_dns.isChecked()
            self.options[3] = str(self.line_dns.text())
            save_options(self.options)
            self.accept()