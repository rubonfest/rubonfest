@echo off
where /q python
if ERRORLEVEL 1 (
  msiexec /qb! /i install\python-2.7.13.msi TARGETDIR="C:\Python27" && SETX PATH "%PATH%;C:\Python27"
)
where /q lektor
if ERRORLEVEL 1 (
  @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((new-object net.webclient).DownloadString('https://getlektor.com/install.ps1'))" && SETX PATH "%PATH%;%LocalAppData%\lektor-cli"
)
where /q git
if ERRORLEVEL 1 (
  install\Git-2.13.0-64-bit.exe /SILENT /NOCANCEL && git config user.email "rubonfest@dev.null" && git config user.name "rubonfest"
)
echo "Installation complete!"