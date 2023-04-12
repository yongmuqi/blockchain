import time

import requests
from selenium import webdriver


# hubstudio_connector.exe --server_mode=http --http_port=6873 --app_id= --group_code= --app_secret=

# 获取webdriver
def startBrowser(hubId):
    url = "http://127.0.0.1:6873/api/v1/browser/start"
    data = {
        "containerCode": hubId
    }
    resp = requests.post(url, json=data).json()
    webdriver_path = resp["data"]["webdriver"]
    port = resp["data"]["debuggingPort"]
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", '127.0.0.1:' + str(port))
    driver = webdriver.Chrome(webdriver_path, options=options)
    return driver


def stopBrowser(hubId):
    url = "http://127.0.0.1:6873/api/v1/browser/stop?containerCode=" + hubId
    requests.get(url).json()


def open_baidu(driver):
    driver.get("https://www.baidu.com/")
    time.sleep(3)


if __name__ == '__main__':
    # 获取webdriver
    driver = startBrowser('36720345')  # 填写打开环境返回的webdriver和debuggingPort参数
    # 运行脚本
    open_baidu(driver)
    time.sleep(3)
    stopBrowser('36720345')
