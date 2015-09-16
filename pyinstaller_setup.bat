@echo off
set name=EasyIP
set icon=res/logo.ico
set script=main.py
pyinstaller -n %name% -w -F --hidden-import=atexit -i %icon% %script%
start dist
pause