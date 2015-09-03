__author__ = 'adrian'
import os
from locale import getdefaultlocale

def set_ip(id_, ip, ms, gw='', dns=''):
    set_ip_address_command = "netsh interface ip set address %s static %s %s %s" % (str(id_), str(ip), str(ms), str(gw))
    set_dns_address_command = "netsh interface ip set dnsservers name=%s source=static address=%s validate=no" % (
        str(id_), str(dns))
    read1 = os.popen(set_ip_address_command).read()
    # read2 = ''
    if dns:
        read2 = os.popen(set_dns_address_command).read()
    # return unicode_(read1 + '\n' + read2)
    return read1.decode(getdefaultlocale()[1])

def dhcp(id_):
    com = "netsh interface ip set address %s dhcp" % id_
    read = os.popen(com).read()
    return unicode_(read)


def unicode_(obj, encoding='utf-8'):
    """
    :param obj: un obj q puede ser un str, byte, etc q sera convertido a unicode.
    :param encoding: tipo de codificacion para la conversion
    :return: obj convertido en unicode tipo utf-8, latin u otra codif especificada
    """
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            try:
                obj = unicode(obj, encoding)
            except UnicodeDecodeError:
                obj = unicode(obj, 'latin-1')
    return obj
