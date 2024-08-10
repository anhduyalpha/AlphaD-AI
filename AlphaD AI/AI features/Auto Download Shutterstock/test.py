import subprocess
import pygetwindow as gw
def startProgram():
    SW_HIDE = 4
    info = subprocess.STARTUPINFO()
    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = SW_HIDE
    a = subprocess.Popen(r'"C:\Users\Duy\Downloads\All app\Get-Stocks\Get-Stocks.exe"', startupinfo=info)
    hide_app = gw.get
    hide_app.move(-1000,-1000)
startProgram()