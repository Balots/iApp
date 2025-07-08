@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion
set logfile=test.log

for /f "tokens=2 delims==" %%A in ('psexec \\upr5-temp wmic memorychip get Capacity /value') do (
    set "RESULT=%%A"
    echo !RESULT! >> "%logfile%"
)
exit /b