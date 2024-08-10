import re , requests , os ,time 
import win32clipboard as clb
from bs4 import BeautifulSoup
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright, Playwright
from Module.PyAutoGUI import alert, confirm, prompt, alert_with_title
from Module.RunApp import run_app_getstocks
from Module.WebBrowser import chorme_stock_by_app
from Module.ProcessLink import process_name_image


def clear_clb():
    clb.OpenClipboard()
    clb.EmptyClipboard()
    clb.CloseClipboard()
    
def clipboard():
    alert("Copy the link of the image you want to download")
    while True:
        time.sleep(0.5)
        clb.OpenClipboard()    
        try:           
            Original_link: str = clb.GetClipboardData()
            print(Original_link)
        except:
            clear_clb()
            main()
        else:
            clb.CloseClipboard()
            if 'https://www.shutterstock.com/vi/image-photo' in Original_link:
                break
            else:
                alert("You may not copy the shutterstock link, or the link is not the image link \n\n Please copy the link of the image you want to download in shutterstock")
                continue
    
    print("The original link is: ", Original_link)
    Name_image = process_name_image(Original_link) 
    ID_image = process_name_image(Original_link)            
    Accept: str = confirm(f"Do you want to download image with the Name: {Name_image[1]} and ID: {ID_image[2]}", "Notifications")
    if Accept == 'Ok':         
        run_app(Original_link)
    else: 
        clear_clb()
        main()   

def run_app(Original_link):
    run_app_getstocks()
    run(Original_link)
    
def run(Original_link):
    Two_link = chorme_stock_by_app(Original_link)
        # ---------------------
    download_images(Two_link[0], Two_link[1])
        # ---------------------

def download_images(Final_link, Original_link):
    os.chdir(os.path.join(r"C:\Users\Duy\Stock\Image"))
    name_for_open: str = process_name_image(Original_link)
    name_for_open: str = name_for_open[0]
    print(f"The name of the image was: {name_for_open}")
    # ---------------------
    with open(name_for_open, 'wb') as f:
        image: bytes = requests.get(Final_link)
        f.write(image.content)
    # ---------------------
    alert_with_title("Download Success", "Notification")
    Notice : str = confirm("Do you want to see the download files", "Notification")
    if Notice == 'Ok':
        open_file(name_for_open)
    else:
        main()
    # ---------------------
    
def open_file(name_for_open):
    Path: str = r"C:\Users\Duy\Stock\Image"
    Name: str = "\\" + name_for_open
    os.startfile(Path+Name)
    continue_down = confirm("Do you want to continue download another image?", "Notification")    
    print
    if continue_down == 'Ok':
        main()
    else: 
        print("Closing program")
        exit()

def main():
    
    clipboard()
        
main()

