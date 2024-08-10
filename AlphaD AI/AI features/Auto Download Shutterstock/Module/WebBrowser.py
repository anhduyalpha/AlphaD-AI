import win32clipboard as clb
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright, Playwright
import itertools

def chorme_stock_by_app(Original_link):
    with sync_playwright() as playwright:
        print('Opening Browser and Downloading')
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        # ---------------------
        clb.OpenClipboard()
        data: str= clb.GetClipboardData()
        clb.CloseClipboard()
        page.goto(data)
        while True:
            itertools.cycle(['|', '/', '-', '\\'])
            page.wait_for_load_state('networkidle')
            page.url
            short_link: str = page.url
            if "https://short.bhawanigarg.com/" in short_link:
                continue
            else: 
                final_link: str = short_link
                print('Final link is:', final_link)
                break
        context.close()
        browser.close()
    return final_link, Original_link
def main():
    chorme_stock_by_app()
    
    
if __name__ == "__main__":
    main()