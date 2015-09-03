__author__ = 'adrian'
from win32net import NetServerGetInfo
dict_ = NetServerGetInfo(None, 503)
print(dict_)

