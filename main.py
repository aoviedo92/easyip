# -*- coding: utf-8 -*-
from PyQt4.QtCore import SIGNAL, pyqtSignature

__author__ = 'adrian'
import sys
from PyQt4.QtGui import *
from ui.ui import Ui_MainWindow
from ui.message import Message
from ui.netconfigtile import NetConfigTile
from ui.combointerfaces import Combo
from ui.dhcpbutton import DHCP
from ui.options import Options
from data import load_data, save_data
from network.interfaces import ipconfig, find_id_by_ad


class Main(QMainWindow, Ui_MainWindow):
    """
    already_dhcp --> para cuando se llame el metodo refresh no se anada otro boton DHCP vacio. una vez q este boton se
                     adiciona, este param se vuelve True, indicando q el boton ya esta.
    red_code --> (codigo rojo) para indicar q no se muestren los carteles de validacion hasta q se de click en salvar
    IPCONFIG --> todos los datos de las interfaces, este atributo se debe actualizar cuando alguna interfaz es conectada
                 o cambiada
    options --> mantiene las opciones del programa, es necesario actualizarlo cuando se cambia alguna opcion
    config --> informacion de los tiles
    """

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.already_dhcp = False
        self.red_code = False
        self.default_tile = False
        self.IPCONFIG = ipconfig()
        self.options = list()
        self.config = list()

        self.setupUi(self)

        self.list_lineEdit_Label = [(self.line_nm, self.lbl_err_nm),
                                    (self.line_ip, self.lbl_err_ip),
                                    (self.line_ms, self.lbl_err_ms),
                                    (self.line_gw, self.lbl_err_gw),
                                    (self.line_dns, self.lbl_err_dns)]

        self.combo = None
        self.combo = Combo(self.IPCONFIG)
        self.layout_lineedit.addWidget(self.combo)
        self.layout_lineedit.addWidget(self.lbl_err_combo)

        for line, lbl in self.list_lineEdit_Label:
            self.connect(line, SIGNAL('returnPressed()'), self.on_btn_only_save_clicked)
            self.layout_lineedit.addWidget(line)
            self.layout_lineedit.addWidget(lbl)

        self.refresh_data()
        self.load_dhcp_buttons()
        self.load_tiles()
        self.line_ms.focusInEvent = lambda _: self.default_mask()
        self.line_dns.focusInEvent = lambda _: self.default_dns()

        self.connects()

    def connects(self):
        self.connect(self.combo, SIGNAL('currentIndexChanged(int)'), self.validator)
        self.connect(self.btn_options, SIGNAL('released()'), self.options_dialog)
        self.connect(self.btn_info, SIGNAL('released()'), self.info_dialog)
        self.connect(self.btn_reload, SIGNAL('released()'), self.reload)

    def reload(self):
        self.IPCONFIG = ipconfig()
        self.combo.update_items(self.IPCONFIG)
        self.load_dhcp_buttons()

    def refresh_data(self):
        data = load_data()
        self.options = data['options']
        self.config = data['config']

    def default_mask(self):
        if self.options[0]:
            self.line_ms.setText(self.options[1])
        else:
            self.line_ms.selectAll()

    def default_dns(self):
        if self.options[2]:
            self.line_dns.setText(self.options[3])
        else:
            self.line_dns.selectAll()

    def load_dhcp_buttons(self):
        some_connected = False
        for config in self.IPCONFIG:
            if config[1] == 'connected':
                some_connected = True
                dhcp = DHCP(config[0], 'DHCP\n' + config[4])
                self.layout_dchp.addWidget(dhcp)
        if not some_connected and not self.already_dhcp:
            self.already_dhcp = True
            dhcp = DHCP('id', 'DHCP\nNo hay ninguna interfaz conectada.')
            self.layout_dchp.addWidget(dhcp)

    def load_tiles(self):
        if len(self.config):
            for list_ in self.config:
                id_ = list_[0]
                ad = list_[1]
                nm = list_[2]
                ip = list_[3]
                ms = list_[4]
                gw = list_[5]
                dns = list_[6]
                tile = NetConfigTile(id_, ad, nm, ip, ms, gw, dns)
                self.layout_wrapper_tile.addWidget(tile)
        else:
            tile = NetConfigTile.default_tile()
            self.default_tile = tile
            self.layout_wrapper_tile.addWidget(tile)

    @pyqtSignature('')
    def on_btn_set_ip_clicked(self):
        tile = self.on_btn_only_save_clicked()
        if tile:
            tile.press_set_ip()

    def options_dialog(self):
        options_dialog = Options()
        options_dialog.setStyleSheet(Ui_MainWindow.set_style_qss())
        options_dialog.exec_()
        self.refresh_data()

    def info_dialog(self):
        self.reload()
        interfaces_disconnected = '<h3>Interfaces desconectadas</h3>'
        interfaces_connected = '<h3>Interfaces conectadas</h3>'
        for config in self.IPCONFIG:
            if config[1] == 'disconnected':
                interfaces_disconnected += '<p>____________________</p>'
                # interfaces_disconnected += '<p>%s</p>' % config[2]
                interfaces_disconnected += '<p>%s</p>' % config[4]
                interfaces_disconnected += '<p>%s</p>' % config[5]
            else:
                interfaces_connected += '<p>%s</p>' % config[2]
                interfaces_connected += '<p>%s</p>' % config[4]
                interfaces_connected += '<p>%s</p>' % config[5]
                interfaces_connected += '<p>%s</p>' % config[6]
                interfaces_connected += '<p>%s</p>' % config[7]
                interfaces_connected += '<p>%s</p>' % config[8]
                interfaces_connected += '<p>____________________</p>'

        link_network_connexion = '<a href="ncpa.cpl">Presione aqui para ver las conexiones de red en Panel de Control.</a>'
        info = '<table><tr><td>%s</td><td>%s</td></tr></table><p>%s</p>' % (
            interfaces_disconnected, interfaces_connected, link_network_connexion)
        Message.information(Message(background_color='white', size='8'), u'Información', info, '')

    @pyqtSignature('')
    def on_btn_only_save_clicked(self):
        self.red_code = True
        if not self.check_full_list() and not self.validator():
            ad = self.combo.currentText()
            id_ = find_id_by_ad(ad, self.IPCONFIG)
            nm = self.line_nm.text()
            ip = self.line_ip.text()
            ms = self.line_ms.text()
            gw = self.line_gw.text()
            dns = self.line_dns.text()
            save_data(str(id_), str(ad), str(nm), str(ip), str(ms), str(gw), str(dns))
            tile = NetConfigTile(id_, ad, nm, ip, ms, gw, dns)
            self.layout_wrapper_tile.addWidget(tile)
            if self.default_tile: self.default_tile.remove_tile()
            tile.add_tile()
            self.refresh_data()
            self.red_code = False
            self.restart_form()
            return tile
        return None

    def restart_form(self):
        print("RESTART")
        for line, lbl in self.list_lineEdit_Label:
            line.focus_out_style()
            line.setText("")
        self.combo.setCurrentIndex(0)

    def check_full_list(self):
        self.refresh_data()
        if len(self.config) >= self.options[4]:
            Message.information(Message(), 'Lista llena', u'Ya has llegado al máximo permitdo de configuraciones.\n'
                                                          u'En caso de querer impedir este comportamiento puedes '
                                                          u'cambiarlo en opciones.', '')
            return True
        return False

    def validator(self, read_only=False):
        """
        Validar cada LineEdit
        :param read_only: cuando se de clic a uno de los botones de salvar, entonces hay q hacer validaciones en vivo
        justo cuando se pierde el foco del LineEdit, pero se queda el cursor marcado en el line edit aunq ya no tenga
        el foco: (TypeError: invalid argument to sipBadCatcherResult()). Entonces cuando llamo a este metodo desde la
        funcion lambda para rescribir otra vez el evento focusOutEvent del LineEdit le paso este argumento en True para q
        el LineEdit sea de solo lectura. Cuando se vuelve a obtener el foco todo marcha ok pq se reescribio en la clase
        LineEdit el evento focusInEvent y se vuelve a poner el modo escritura normal
        :return: FALSO si no hay errores, TRUE si los hay
        """
        print "VALIDATOR"
        error = False
        if self.red_code:
            if self.combo.currentIndex() == 0:
                self.lbl_err_combo.setText('Debe seleccionar una interfaz.')
                self.lbl_err_combo.setVisible(True)
                self.lbl_err_combo.setType_('error')
                error = True
            else:
                self.lbl_err_combo.setVisible(False)
            for line, lbl in self.list_lineEdit_Label:
                errors = line.validations()
                if errors:
                    if errors == "no ip but no it's required":
                        line.focus_out_style()
                    else:
                        error = True
                        lbl.setType_('error')
                        lbl.setText(errors)
                        lbl.setVisible(True)
                        line.error_style()
                else:
                    line.setReadOnly(read_only)
                    line.success_style()
                    lbl.setVisible(False)
            # self.red_code = False
            for line, lbl in self.list_lineEdit_Label:
                # ademas de sobreescribir focusOut en LineEdit, aqui tb lo hacemos, el obj es q despues de dar salvar,
                # al perder el foco un LineEdit con errores se oculten los msg si se satisface la validacion.
                line.focusOutEvent = lambda _: self.validator(True)
        return error


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    app.exec_()
