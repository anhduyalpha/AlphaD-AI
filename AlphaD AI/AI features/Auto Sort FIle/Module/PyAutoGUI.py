import pyautogui as pag

def alert(text):
    text : str = pag.alert(text =text, button = ('Ok'))
    return text
    
def alert_with_title(text, title):
    text : str = pag.alert(text =text, title= title, button = ('Ok'))
    return text

def confirm(text,title):
    text : str = pag.confirm(text = text, title = title, buttons = ['Ok', 'Cancel'])
    return text

def prompt():
    pass

def main():
    alert()
    confirm()
    alert_with_title()
    prompt()

if __name__ == '__main__':
    main()