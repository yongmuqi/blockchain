import requests
from playwright.sync_api import sync_playwright


class Drivers:
    def __init__(self):
        self.browser = None
        self.pages = None

    def startBrowser(self, NumId, soft):
        if soft == 'bit_task':
            headers = {'id': NumId, 'loadExtensions': True}
            openurl = "http://127.0.0.1:54345/browser/open"
            resp = requests.post(openurl, json=headers).json()
            if resp['data']['ws'] and resp['data']['http']:
                p = sync_playwright().start()
                self.browser = p.chromium.connect_over_cdp(endpoint_url=resp['data']['ws'])
                context = self.browser.contexts[0]
                self.pages = context.pages[0]
            return self.pages, self.browser

        elif soft == 'ads_task':
            url = 'http://local.adspower.net:50325/api/v1/browser/'
            open_url = url + 'start?user_id=' + NumId + '&open_tabs=1' + '&launch_args=["--window-position=400,0", "--start-maximized"]'
            resp = requests.get(open_url).json()
            if resp['code'] == 0 and resp['data']['ws'] and resp['data']['ws']['puppeteer']:
                p = sync_playwright().start()
                self.browser = p.chromium.connect_over_cdp(endpoint_url=resp['data']['ws']['puppeteer'])
                context = self.browser.contexts[0]
                self.pages = context.pages[0]
            return self.pages, self.browser
