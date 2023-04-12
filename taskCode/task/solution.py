from random import random
import re
import requests
import time
import base64
from PIL import Image
from loguru import logger

from taskCode.actions import Config

CAPTCHA_ENTIRE_IMAGE_FILE_PATH = 'image\yescaptcha\captcha_entire_image.png'
CAPTCHA_SINGLE_IMAGE_FILE_PATH = 'image\yescaptcha\captcha_single_image_%s.png'
CAPTCHA_RESIZED_IMAGE_FILE_PATH = 'image\yescaptcha\captcha_resized_image.png'


# 传入图片路径和调整大小，返回编码后的结果
def resize_base64_image(filename, size):
    width, height = size
    img = Image.open(filename)
    new_img = img.resize((width, height))
    new_img.save(CAPTCHA_RESIZED_IMAGE_FILE_PATH)
    with open(CAPTCHA_RESIZED_IMAGE_FILE_PATH, "rb") as f:
        data = f.read()
        encoded_string = base64.b64encode(data)
        return encoded_string.decode('utf-8')


class Solution(object):
    def __init__(self, driver):
        self.driver = driver
        self.mainXpath = '//iframe[contains(@src, "checkbox")]'
        self.imageXpath = '//iframe[contains(@src, "challenge")]'
        self.api_url = 'https://api.yescaptcha.com/createTask'
        self.api_key = Config.yescaptcha_key()

    # yesCaptcha网站API的封装，调用它后服务器返回相应参数
    def create_task(self, queries, question):
        data = {
            "clientKey": str(self.api_key),
            "sourceCode": {
                "type": "HCaptchaClassification",
                "queries": queries,   # 每张验证码图片对应的 Base64 编码
                "question": question  # 要识别的问题整句
            },
            "softID": 78
        }
        try:
            response = requests.post(self.api_url, json=data)
            result = response.json()
            logger.debug(f'Captcha网站识别的结果 {result}')
            return result
        except requests.RequestException:
            logger.exception('Captcha网站识别出错', exc_info=True)

    # 切换到验证码入口的frame
    def switch_to_captcha_entry_iframe(self) -> None:
        self.driver.wait.wait_switch_to_default()
        self.driver.wait.wait_switch_to_frame(self.mainXpath)

    # 切换到验证码图片里面的内容的frame
    def switch_to_captcha_content_iframe(self) -> None:
        self.driver.wait.wait_switch_to_default()
        self.driver.wait.wait_switch_to_frame(self.imageXpath)

    # 点击验证码的入口，然后把验证码触发出来
    def trigger_captcha(self) -> None:
        self.switch_to_captcha_entry_iframe()
        captcha_entry = self.driver.wait.wait_visibility_of_element_CSS('#anchor #checkbox')
        captcha_entry.click()
        self.switch_to_captcha_content_iframe()
        captcha_element = self.driver.wait.wait_visibility_of_element_CSS('.sourceCode-grid')
        if captcha_element.is_displayed:
            logger.debug('Captcha验证触发成功')

    # 检验验证是否成功，如果成功则返回True
    def get_is_successful(self):
        try:
            self.switch_to_captcha_entry_iframe()
            anchor = self.driver.wait.wait_visibility_of_element_CSS('#anchor #checkbox')
            checked = anchor.get_attribute('aria-checked')
            logger.debug(f'检查 {checked}')
            return str(checked) == 'true'
        except BaseException:
            return 1 == 1

    def verify_captcha(self):
        # 获取验证码问题的文本
        captcha_target_text = self.driver.wait.wait_visibility_of_element_CSS('.prompt-text').text
        logger.debug(f'获取验证码问题的文本： {captcha_target_text}')
        # 提取每张验证码图片的 url，并存入resized_single_captcha_base64_strings列表
        single_captcha_elements = self.driver.wait.wait_visibility_of_elements_CSS('.sourceCode-image .image-wrapper .image')
        resized_single_captcha_base64_strings = []
        for i, single_captcha_element in enumerate(single_captcha_elements):
            single_captcha_element_style = single_captcha_element.get_attribute('style')
            pattern = re.compile('url\("(https.*?)"\)')
            match_result = re.search(pattern, single_captcha_element_style)
            single_captcha_element_url = match_result.group(1) if match_result else None
            with open(CAPTCHA_SINGLE_IMAGE_FILE_PATH % (i,), 'wb') as f:
                f.write(requests.get(single_captcha_element_url).content)
            # 调用resize_base64_image方法，传入图片路径和调整大小，然后可以返回编码后的结果
            resized_single_captcha_base64_string = resize_base64_image(
                CAPTCHA_SINGLE_IMAGE_FILE_PATH % (i,), (100, 100))
            resized_single_captcha_base64_strings.append(
                resized_single_captcha_base64_string)

        # 调用create_task方法，通过YesCaptcha网站的API进行图像识别
        captcha_recognize_result = self.create_task(resized_single_captcha_base64_strings, captcha_target_text)
        if not captcha_recognize_result:
            logger.error('无法获得captcha识别结果')
            return
        recognized_results = captcha_recognize_result.get(
            'solution', {}).get('objects')

        if not recognized_results:
            logger.error('未获得captcha认可的索引')
            return

        # 根据服务器返回的正确图片索引，进行点击
        recognized_indices = [i for i, x in enumerate(recognized_results) if x]
        logger.debug(f'识别的正确图片索引 {recognized_indices}')
        click_targets = self.driver.wait.wait_visibility_of_elements_CSS('.sourceCode-image')
        for recognized_index in recognized_indices:
            click_target = click_targets[recognized_index]
            click_target.click()
            time.sleep(random())

        # 图片点击完成后，点击验证按钮
        verify_button = self.driver.wait.wait_visibility_of_element_CSS('.button-submit')
        if verify_button.is_displayed:
            verify_button.click()
            time.sleep(5)

        # 检验验证是否成功，如果失败则继续验证
        is_succeed = self.get_is_successful()
        if is_succeed:
            logger.debug('验证成功')
            self.driver.wait.wait_switch_to_parent_frame()

        else:
            time.sleep(3)
            self.switch_to_captcha_content_iframe()
            self.verify_captcha()

    def resolve(self):
        self.trigger_captcha()
        time.sleep(3)
        self.verify_captcha()
