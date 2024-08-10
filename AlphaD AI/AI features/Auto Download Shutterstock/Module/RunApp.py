from pywinauto.application import Application
import pygetwindow as gw
import itertools, sys


def run_app_getstocks():
    try:
        hide_app = gw.getWindowsWithTitle('Get Free Shutterstock (https://bhawanigarg.com)')[0]
    except:
        app = Application(backend='uia').start(r"C:\Users\Duy\Downloads\All app\Get-Stocks\Get-Stocks.exe").wait_cpu_usage_lower()
        dialog = app.GetFreeShutterstock
        while 1:
            try:
                hide_app = gw.getWindowsWithTitle('Get Free Shutterstock (https://bhawanigarg.com)')[0]
            except:
                print("Continue to connect")
                continue
            else: 
                print("Connected")
                break
        hide_app.move(0,-1000)
        
        dialog.child_window(title="PASTE URL", auto_id="btnPASTE", control_type="Button").wait('visible', timeout=600).click()   
        dialog.GETNOW.click()
        while 1:
            try:
                dialog.child_window(title="COPY", auto_id="btnCopy", control_type="Button").wait('enabled', timeout=0.1).click()
            except: 
                hide_app.restore()
                continue 
            else: break
        print('Process link is done')
        dialog.Close.click()   
    else:
        hide_app.close()
        main()


def main():
    run_app_getstocks()
if __name__ == "__main__":  
    main()