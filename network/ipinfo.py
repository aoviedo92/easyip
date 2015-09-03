# -*- coding: utf-8 -*-
import os
import re
import locale


def InfoIP():
    if locale.getdefaultlocale()[0][:2] != 'es':
        return [[], []]
    lee = os.popen('ipconfig').read()
    lect = lee.split('\n')
    lines = [line for line in lect if line != '']
    ad_desc = []
    ad_con = []
    for i in range(1, len(lines)):
        if re.match(".*Adaptador.*", lines[i]):
            if re.match('.*Estado de los medios.*', lines[i + 1]):
                ad_desc.append(unicode_(lines[i][0:-1]))
            else:
                ip = None
                subred = None
                gateway = None
                for j in range(i, i + 6):
                    exp_ip = re.match(".*IPv4.*: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$", lines[j])
                    exp_subred = re.match(".*subred[\.\s]*: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$", lines[j])
                    exp_gateway = re.match(".*predeterminada[\.\s]*: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$", lines[j])
                    if exp_ip: ip = exp_ip.group(1)
                    if exp_subred: subred = exp_subred.group(1)
                    if exp_gateway: gateway = exp_gateway.group(1)
                ad_con.append([unicode_(lines[i][0:-1]),
                               ip if ip else '',
                               subred if subred else '',
                               gateway if gateway else ''])
    return [ad_desc, ad_con]


def setIP(ifc, ip, ms='', gw='', dns=''):
    com = "cmd /c netsh interface ip set address %s static %s %s %s" % (ifc, ip, ms, gw)
    # com = "cmd /c netsh interface ip set address \"" + ifc + "\" static " + ip + " " + ms + " " + gw
    com2 = "cmd /c netsh interface ip set dnsservers name=%s source=static address=%s validate=no" % (ifc, dns)
    # com2 = "cmd /c netsh interface ip set dnsservers name=\"" + ifc + "\" source=static address=" + dns + " validate=no"
    read1 = os.popen(com).read()
    read2 = ''
    if dns:
        read2 = os.popen(com2).read()
    out = unicode_(read1 + '\n' + read2)
    return out


def dhcp(ifc):
    com = "cmd /c netsh interface ip set address %s dhcp" % ifc
    read = os.popen(com).read()
    read = unicode_(read)
    return read


def ncpa():
    os.system('ncpa.cpl')


def interfaces():
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
        ifc.append([id_, state, unicode_(name)])
    for e in ifc:
        if 'Loopback Pseudo-Interface 1' in e:
            ifc.remove(e)
    return ifc


def if_in():
    ad_desc = InfoIP()[0]
    ad_con = InfoIP()[1]
    # print ad_con
    interfaces_ = interfaces()
    for ad in ad_desc:
        if 'Adaptador de Ethernet' in ad:
            name = ad[22:]
            for ifc in interfaces_:
                if name in ifc[2]:
                    ifc.append('lan')
        elif 'Adaptador de LAN inalmbrica' in ad:
            name = ad[28:]
            for ifc in interfaces_:
                if name in ifc[2]:
                    ifc.append('wlan')
    for ad in ad_con:
        if 'Adaptador de Ethernet' in ad[0]:
            name = ad[0][22:]
            for ifc in interfaces_:
                if name in ifc[2]:
                    ifc.append('wifi')
        elif 'Adaptador de LAN inalmbrica' in ad[0]:
            name = ad[0][28:]
            for ifc in interfaces_:
                if name in ifc[2]:
                    ifc.append('wifi')
    for interface in interfaces_:
        if len(interface) == 3:
            interface.append(None)
    return interfaces_


    # print if_in()
    # print len('Adaptador de LAN inalmbrica')
    # print locale.getdefaultlocale()


def unicode_(obj, encoding='utf-8'):
    """
    :param obj: un obj q puede ser un str, byte, etc q sera convertido a unicode.
    :param encoding: tipo de codificacion para la conversion
    :return: obj convertido en unicode tipo utf-8, latin u otra codif especificada
    """
    print 'to_unicode_or_bust_in', type(obj), obj
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            try:
                obj = unicode(obj, encoding)
                print(1)
                print obj
            except UnicodeDecodeError:
                obj = unicode(obj, 'latin-1')
                # except NoLatin:
                # pass
    print 'to_unicode_or_bust_out', type(obj), obj
    return obj


def lan_show_interfaces():
    read = os.popen('netsh lan show interfaces').read()
    read = read.split('\n')[3:]
    read = [line.strip() for line in read if line != '']
    # print('\n'.join(read))
    lan_interfaces = []
    try:
        for i in range(0, len(read), 5):
            name = read[i].split(':')[1].strip()
            desc = read[i+1].split(':')[1].strip().split(' - ')[0].strip()
            lan_interfaces.append([name, desc])
    except IndexError:
        pass
    print(lan_interfaces)

print(interfaces())
