# coding=utf-8
__author__ = 'adrian'
import os
from locale import getdefaultlocale


def set_lang_dict():
    lang_dict_ = dict()
    lang = getdefaultlocale()[0][:2]
    if lang == 'es':
        lang_dict_['adapter'] = 'Adaptador'
        lang_dict_['mask'] = 'subred'
        lang_dict_['gateway'] = 'Puerta de enlace'
        lang_dict_['mac'] = 'Direcci\xa2n f\xa1sica'
    elif lang == 'en':
        lang_dict_['adapter'] = 'Adapter'
        lang_dict_['mask'] = 'mask'
        lang_dict_['gateway'] = 'gateway'
        lang_dict_['mac'] = 'Physics Address'
    return lang_dict_


def ipconfig():
    interfaces_info = []
    # read = os.popen('ipconfig /all').read().split('\n')
    read = [line for line in os.popen('ipconfig /all').readlines()
            if line != "\n"]
    for i in range(len(read)):
        if read[i].startswith(lang_dict['adapter']):
            j = i + 1
            type_ = 'lan' if read[i].find('inal\xa0mbrica') == -1 else 'wlan'
            interface = list(find_name_interface(read[i]))
            # type_ = 'bluetooth' if interface[2]
            if interface:
                interface.append(type_)
                while not read[j].startswith(lang_dict['adapter']) and j + 1 < len(read):
                    if read[j].find('Desc') != -1:
                        desc = read[j].split(':')[1].strip()
                        if desc.lower().find('bluetooth') != -1:
                            interface[3] = 'bluetooth'
                        interface.append(desc)
                    if read[j].find('IPv4') != -1:
                        interface.append(read[j].split(':')[1].strip())
                    if read[j].find(lang_dict['mask']) != -1:
                        interface.append(read[j].split(':')[1].strip())
                    if read[j].find(lang_dict['gateway']) != -1:
                        interface.append(read[j].split(':')[1].strip())
                    if read[j].find(lang_dict['mac']) != -1:
                        interface.append(read[j].split(':')[1].strip())
                    j += 1
                interfaces_info.append(interface)
    return interfaces_info


def interfaces():
    """
    muestra la info de las interfaces de esta forma
    Índ     Mét         MTU         Estado              Nombre
    ---  ----------  ----------  ------------  ---------------------------
      1          50  4294967295  connected     Loopback Pseudo-Interface 1
      7          25        1500  connected     Wi-Fi
      6           5        1500  disconnected  Ethernet
      8           5        1500  disconnected  Conexión de área local* 1
    :return: [id, estado, nombre]
    """
    read = os.popen('netsh interface ip show interfaces').read()
    read = read.split('\n')
    l = []
    for i in range(3, len(read)):
        l.append([line for line in read[i].split(' ') if line != ''])
    l2 = [line for line in l if line != []]
    ifc = []
    for e in l2:
        id_ = e[0]
        state = e[3]
        name = ' '.join(e[4:]) if len(e) > 5 else e[4]
        ifc.append([id_, state, name])
    for e in ifc:
        if 'Loopback Pseudo-Interface 1' in e:
            ifc.remove(e)
    return ifc


def find_name_interface(str_to_search):
    """
    recibe una cadena q puede contener el nombre de una intefaz
    :param str_to_search:
    :return: nombre de la interfaz
    """
    interface_list = interfaces()
    for interface in interface_list:
        if str_to_search.find(interface[2]) != -1:
            return interface
    return []


def find_id_by_ad(ad, ipconfig_):
    for config in ipconfig_:
        if ad in config:
            return config[0]
    return False


lang_dict = set_lang_dict()

# SHOW_INTERFACES = interfaces()
# for l in ipconfig():
#     print(l)
# print os.popen('ipconfig /all').readlines().split('\n')
# print os.popen('ipconfig /all').readlines()
# print interfaces()
# print ipconfig()