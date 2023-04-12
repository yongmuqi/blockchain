import time
from playwright.sync_api import Page, Browser


class Function:
    def __init__(self, page, browser):
        self.page: Page = page
        self.browser: Browser = browser

    # 切换页面page功能
    def wait_for_and_switch_to_new_window(self, timeout=30):
        start_time = time.time()
        context = self.browser.contexts[0]
        all_pages = len(context.pages)
        print(all_pages)
        while time.time() - start_time < timeout:
            if len(context.pages) > 1:
                self.page = context.pages[-1]  # 切换到最新打开的页面
                break
            time.sleep(1)

    # 切换上下文功能，一个浏览器窗口算一个context，对于狐狸钱包那种弹出式的，也算一个context
    def wait_for_new_popup(self, newWindows, timeout=30):
        start_time = time.time()
        while time.time() - start_time < timeout:
            for context in self.browser.contexts:
                for page in context.pages:
                    if newWindows in page.title():
                        return page
            time.sleep(1)