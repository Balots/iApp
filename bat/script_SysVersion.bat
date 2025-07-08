@echo off 
chcp 65001 > nul
setlocal enabledelayedexpansion
:: all non-utf8 symbols goes to nul
::set input params like hostname. Write here if you need new one.
set /p input=""
set "HOST=!input!"

::set logfile. Time and Date format. 
set logfile=script_SysVersion.log
set datetime=%date:~6,4%-%date:~3,2%-%date:~0,2%_%time:~0,2%-%time:~3,2%-%time:~6,2%

::Use psexec utils to get info from remote computer.
for /f "tokens=2 delims==" %%A in ('psexec \\!HOST! wmic os get caption /value') do set "os_caption=%%A"
echo %date% %time%	PC:!HOST!	!os_caption! >> "%logfile%"
::\t delimiter
exit \b