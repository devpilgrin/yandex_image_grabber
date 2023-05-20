@echo off
if not defined PYTHON (set PYTHON=python)

set PYTHON="env\Scripts\python.exe"

echo "start main.py"

%PYTHON% main.py %*

pause
exit /b

