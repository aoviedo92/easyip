# -*- coding: utf-8 -*-
__author__ = 'adrian'
from PyQt4.QtGui import QLineEdit
import re


class LineEdit(QLineEdit):
    def __init__(self, placeholder, validations_list, parent=None):
        self.validations_list = validations_list
        super(LineEdit, self).__init__(parent)
        self.setPlaceholderText(placeholder)

    def focusInEvent(self, QFocusEvent):
        super(LineEdit, self).focusInEvent(QFocusEvent)
        self.setReadOnly(False)
        self.focus_in_style()

    def focusOutEvent(self, QFocusEvent):
        super(LineEdit, self).focusOutEvent(QFocusEvent)
        self.focus_out_style()

    def error_style(self):
        self.setStyleSheet("border: 1px solid #9A1616")

    def success_style(self):
        self.setStyleSheet("border: 1px solid #00FA9A")

    def focus_in_style(self):
        self.setStyleSheet("border: 1px solid grey")

    def focus_out_style(self):
        self.setStyleSheet("border: 1px solid silver")

    def validations(self):
        if "required" in self.validations_list:
            if str(self.text()).strip() == "":
                return "Este campo es obligatorio"
        if "ip" in self.validations_list:
            return self.valid_ip()

    def valid_ip(self):
        try:
            parts = str(self.text()).strip().split('.')
            if parts == [''] and "required" not in self.validations_list:
                return "no ip but no it's required"
            valid = len(parts) == 4 and all(0 <= int(part) < 256 for part in parts)
            if valid:
                return False
            return u"Formato ip no válido"
        except ValueError:
            return u"Una de las partes no es número"
        except (AttributeError, TypeError):
            return "No es una cadena convertible"

    def valid_mask(self):
        pass
        #     if not self.valid_ip():
        #         parts = str(self.text()).strip().split('.')
