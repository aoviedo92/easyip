__author__ = 'adrian'
d = {'b': 'b'}
print '''
a {b}
'''.format(**d)

def valid_ip(ip):
    try:
        parts = ip.split('.')
        valid = len(parts) == 4 and all(0 <= int(part) < 256 for part in parts)
        if valid:
            return True
        return "Formato ip no valido"
    except ValueError:
        return "Una de las partes no es numero"
    except (AttributeError, TypeError):
        return "No es una cadena convertible"

print valid_ip('0.0.0.0')