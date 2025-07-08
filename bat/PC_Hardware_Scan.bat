@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion
:: Setting filename with date and time
set "datetime=%date:~6,4%-%date:~3,2%-%date:~0,2%_%time:~0,2%-%time:~3,2%-%time:~6,2%"
set "logfile=PC_Hardware_Scan.log"
set ADAPTER_NAME=Ethernet

:: Getting username
for /f "tokens=2 delims==" %%A in ('wmic os get caption /value') do set "os_caption=%%A"
for /f "tokens=2 delims==" %%U in ('wmic computersystem get username /value') do set "username=%%U"

:: Getting local IP address
for /f "tokens=2 delims=:" %%I in ('ipconfig ^| findstr "IPv4"') do (
    set "ip=%%I"
    set "ip=!ip: =!"
)
:: Writing to file

echo ===== User and IP Information ===== >> "%logfile%"
echo Date: %date% %time% >> "%logfile%"
echo Username: !username! >> "%logfile%"
echo Local IPv4: !ip! >> "%logfile%"
echo SysVersion: !os_caption! >> "%logfile%"

echo Scanning PC hardware components... >> "%logfile%"
echo ========================================= >> "%logfile%"
echo. >> "%logfile%"

:: 1. General system information
echo [1. System Information] >> "%logfile%"
echo ========================================= >> "%logfile%"
wmic computersystem get Manufacturer,Model,SystemType /value >> "%logfile%"
echo. >> "%logfile%"

:: 2. Processor (CPU)
echo [2. Processor (CPU)] >> "%logfile%"
echo ========================================= >> "%logfile%"
wmic cpu get Name,Manufacturer,NumberOfCores,NumberOfLogicalProcessors,MaxClockSpeed /value >> "%logfile%"
echo. >> "%logfile%"

:: 3. Memory (RAM)
echo [3. Memory (RAM)] >> "%logfile%"
echo ========================================= >> "%logfile%"
wmic memorychip get Manufacturer,PartNumber,Capacity,Speed,DeviceLocator /value >> "%logfile%"
wmic os get TotalVisibleMemorySize,FreePhysicalMemory /value >> "%logfile%"
echo. >> "%logfile%"

:: 4. Graphics Card (GPU)
echo [4. Graphics Card (GPU)] >> "%logfile%"
echo ========================================= >> "%logfile%"
wmic path win32_VideoController get Name,AdapterRAM,DriverVersion,CurrentHorizontalResolution,CurrentVerticalResolution /value >> "%logfile%"
echo. >> "%logfile%"

:: 5. Storage (HDD/SSD/NVMe)
echo [5. Storage Devices (HDD/SSD/NVMe)] >> "%logfile%"
echo ========================================= >> "%logfile%"
wmic diskdrive get Model,Size,InterfaceType,MediaType /value >> "%logfile%"
echo. >> "%logfile%"
wmic logicaldisk where DriveType=3 get DeviceID,Size,FreeSpace /value >> "%logfile%"
echo. >> "%logfile%"

:: 6. Motherboard
echo [6. Motherboard] >> "%logfile%"
echo ========================================= >> "%logfile%"
wmic baseboard get Manufacturer,Product,SerialNumber /value >> "%logfile%"
echo. >> "%logfile%"

:: 7. Network Adapter
echo [7. Network Adapters] >> "%logfile%"
echo ========================================= >> "%logfile%"
wmic nic where NetEnabled=true get Name,MacAddress,Speed /value >> "%logfile%"
echo. >> "%logfile%"

:: 8. Battery (for laptops)
echo [8. Battery (if present)] >> "%logfile%"
echo ========================================= >> "%logfile%"
wmic path win32_battery get Name,EstimatedChargeRemaining /value >> "%logfile%"
echo. >> "%logfile%"

:: 9. BIOS
echo [9. BIOS Information] >> "%logfile%"
echo ========================================= >> "%logfile%"
wmic bios get Manufacturer,Name,Version,ReleaseDate /value >> "%logfile%"
echo. >> "%logfile%"

echo Collecting installed programs information... >> "%logfile%"
echo ============================================ >> "%logfile%"
echo. >> "%logfile%"

:: 1. Programs list from registry (32-bit)
echo [1. Programs (32-bit)] >> "%logfile%"
echo ============================================ >> "%logfile%"
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall >> "%logfile%"
echo. >> "%logfile%"

:: 2. Programs list from registry (64-bit)
echo [2. Programs (64-bit)] >> "%logfile%"
echo ============================================ >> "%logfile%"
reg query HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall >> "%logfile%"
echo. >> "%logfile%"

:: Completion
echo ========================================= >> "%logfile%"
echo BREAK >> "%logfile%"
echo Report file saved as: %logfile% >> "%logfile%"

exit /b