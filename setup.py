# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    windows=[
        {
            "script": "main.py",
            "icon_resources": [(0, "res/logo.ico"), (1, "res/logo.png")]
        }
    ],
    # data_files = [
    # (
    #         'imageformats', [r'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qico4.dll']
    #     )
    # ],

    options={
        "py2exe": {
            'bundle_files': 1,
            'compressed': True,
            "dll_excludes": ["MSVCP90.dll"],
            "includes": ["sip", "PyQt4.QtGui", "PyQt4.QtCore"]
        }
    },
    zipfile=None,
    name="easyIp",
    version="1.0",
    description="Facilitar la configuracion ip",
    author="Adrian Oviedo",
)


