import base64
from typing import Union
import requests
import time

from PIL import Image
from loguru import logger

from taskCode.actions import Config

CAPTCHA_TARGET_NAME_QUESTION_ID_MAPPING = {
    "taxis": "/m/0pg52",
    "bus": "/m/01bjv",
    "school bus": "/m/02yvhj",
    "motorcycles": "/m/04_sv",
    "tractors": "/m/013xlm",
    "chimneys": "/m/01jk_4",
    "crosswalks": "/m/014xcs",
    "traffic lights": "/m/015qff",
    "bicycles": "/m/0199g",
    "parking meters": "/m/015qbp",
    "cars": "/m/0k4j",
    "vehicles": "/m/0k4j",
    "bridges": "/m/015kr",
    "boats": "/m/019jd",
    "palm trees": "/m/0cdl1",
    "mountains or hills": "/m/09d_r",
    "fire hydrant": "/m/01pns0",
    "fire hydrants": "/m/01pns0",
    "a fire hydrant": "/m/01pns0",
    "stairs": "/m/01lynh",
    "出租车": "/m/0pg52",
    "巴士": "/m/01bjv",
    "摩托车": "/m/04_sv",
    "机动车": "/m/0k4j",
    "小轿车": "/m/0k4j",
    "拖拉机": "/m/013xlm",
    "烟囱": "/m/01jk_4",
    "人行横道": "/m/014xcs",
    "红绿灯": "/m/015qff",
    "自行车": "/m/0199g",
    "停车计价表": "/m/015qbp",
    "汽车": "/m/0k4j",
    "桥": "/m/015kr",
    "船": "/m/019jd",
    "棕榈树": "/m/0cdl1",
    "山": "/m/09d_r",
    "消防栓": "/m/01pns0",
    "楼梯": "/m/01lynh",
    "交通工具": "/m/0k4j",
    "公交车": "/m/01bjv",
    "彩色玻璃": "/m/011y23",
    "火车站": "/m/0py27",
    "消火栓": "/m/01pns0",
    "过街人行道": "/m/014xcs",
    "车库门": "/m/08l941",
    "公交站": "/m/01jw_1",
    "停车计时器": "/m/015qbp",
    "丘陵": "/m/09d_r",
    "车辆": "/m/0k4j",
    "公共汽车": "/m/01bjv",
    "交通灯": "/m/015qff",
    "停车咪表": "/m/015qbp"
}
CAPTCHA_ENTIRE_IMAGE_FILE_PATH = 'image/recaptcha/captcha_entire_image.png'
CAPTCHA_SINGLE_IMAGE_FILE_PATH = 'image/recaptcha/captcha_single_image.png'
CAPTCHA_RESIZED_IMAGE_FILE_PATH = 'image/recaptcha/captcha_resized_image.png'


def resize_base64_image(filename, size):
    width, height = size
    img = Image.open(filename)
    new_img = img.resize((width, height))
    new_img.save(CAPTCHA_RESIZED_IMAGE_FILE_PATH)
    with open(CAPTCHA_RESIZED_IMAGE_FILE_PATH, "rb") as f:
        data = f.read()
        encoded_string = base64.b64encode(data)
        return encoded_string.decode('utf-8')


def get_question_id_by_target_name(target_name):
    logger.debug(f'尝试通过以下方式获取问题id {target_name}')
    question_id = CAPTCHA_TARGET_NAME_QUESTION_ID_MAPPING.get(target_name)
    logger.debug(f'问题ID {question_id}')
    return question_id


class reCaptcha(object):
    def __init__(self, driver):
        self.driver = driver
        self.mainXpath = 'iframe[title="reCAPTCHA"]'
        self.imageXpath = 'iframe[src*="bframe?"]'
        self.api_url = 'https://api.yescaptcha.com/createTask'
        self.api_key = Config.yescaptcha_key()

    def create_task(self, image_base64_string, question_id):
        logger.debug(f'start to recognize image for question {question_id}')
        data = {
            "clientKey": self.api_key,
            "sourceCode": {
                "type": "ReCaptchaV2Classification",
                "image": image_base64_string,
                "question": question_id,
                "softID": 78
            }
        }
        try:
            response = requests.post(self.api_url, json=data)
            result = response.json()
            logger.debug(f'captcha识别结果 {result}')
            return result
        except requests.RequestException:
            logger.exception(
                '识别captcha时出错', exc_info=True)

    # 切换到验证码入口的frame
    def switch_to_captcha_entry_iframe(self) -> None:
        self.driver.wait.wait_switch_to_default()
        self.driver.wait.wait_switch_to_frame_CSS('iframe[title="reCAPTCHA"]')

    # 切换到验证码图片里面的内容的frame
    def switch_to_captcha_content_iframe(self) -> None:
        self.driver.wait.wait_switch_to_default()
        self.driver.wait.wait_switch_to_frame_CSS(self.imageXpath)

    def get_entire_captcha_natural_width(self) -> Union[int, None]:
        result = self.driver.wait.wait_execute_script(
            "return document.querySelector('div.rc-image-tile-wrapper > img').naturalWidth")
        if result:
            return int(result)
        return None

    def get_entire_captcha_display_width(self) -> Union[int, None]:
        entire_captcha_element = self.driver.wait.wait_visibility_of_element_CSS('#rc-imageselect-target')
        if entire_captcha_element:
            return entire_captcha_element.rect.get('width')
        return None

    def trigger_captcha(self) -> None:
        self.switch_to_captcha_entry_iframe()
        captcha_entry = self.driver.wait.wait_visibility_of_element_ID('recaptcha-anchor')
        captcha_entry.click()
        time.sleep(2)
        self.switch_to_captcha_content_iframe()
        try:
            entire_captcha_element = self.driver.wait.wait_visibility_of_element_CSS('#rc-imageselect-target')
            if entire_captcha_element.is_displayed:
                logger.debug('已成功触发captcha')
        except BaseException:
            is_succeed = self.get_is_successful()
            if is_succeed:
                logger.debug('验证成功')
            else:
                verify_error_info = self.get_verify_error_info()
                logger.debug(f'verify_error_info {verify_error_info}')
                self.verify_entire_captcha()

    def get_captcha_target_name(self):
        captcha_target_name_element = self.driver.wait.wait_visibility_of_element_CSS('.rc-imageselect-desc-wrapper strong')
        return captcha_target_name_element.text

    def get_verify_button(self):
        verify_button = self.driver.wait.wait_visibility_of_element_CSS('#recaptcha-verify-button')
        return verify_button

    def verify_single_captcha(self, index):
        time.sleep(3)
        elements = self.driver.wait.wait_visibility_of_elements_CSS('#rc-imageselect-target table td')
        single_captcha_element = elements[index]
        class_name = single_captcha_element.get_attribute('class')
        logger.debug(f'验证单个captcha {index}, class {class_name}')
        if 'selected' in class_name:
            logger.debug(f'未显示新的单个captcha')
            return
        logger.debug('显示新的单个captcha')
        single_captcha_url = self.driver.wait.wait_visibility_of_element_CSS('img').get_attribute('src')
        logger.debug(f'single_captcha_url {single_captcha_url}')
        with open(CAPTCHA_SINGLE_IMAGE_FILE_PATH, 'wb') as f:
            f.write(requests.get(single_captcha_url).content)
        resized_single_captcha_base64_string = resize_base64_image(
            CAPTCHA_SINGLE_IMAGE_FILE_PATH, (100, 100))
        single_captcha_recognize_result = self.create_task(
            resized_single_captcha_base64_string, get_question_id_by_target_name(self.captcha_target_name))
        if not single_captcha_recognize_result:
            logger.error('count未获得单个captcha识别结果')
            return
        has_object = single_captcha_recognize_result.get(
            'solution', {}).get('hasObject')
        if has_object is None:
            logger.error('未获得captcha认可的索引')
            return
        if has_object is False:
            logger.debug('在这个单独的captcha中没有更多的对象')
            return
        if has_object:
            single_captcha_element.click()
            # check for new single captcha
            self.verify_single_captcha(index)

    def get_verify_error_info(self):
        self.switch_to_captcha_content_iframe()
        self.driver.wait.wait_execute_script("return document.querySelector('div.rc-imageselect-incorrect-response')?.text")

    def get_is_successful(self):
        self.switch_to_captcha_entry_iframe()
        anchor = self.driver.wait.wait_visibility_of_element_ID('recaptcha-anchor')
        checked = anchor.get_attribute('aria-checked')
        logger.debug(f'验证 {checked}')
        return str(checked) == 'true'

    def get_is_failed(self):
        return bool(self.get_verify_error_info())

    def verify_entire_captcha(self):
        entire_captcha_natural_width = self.get_entire_captcha_natural_width()
        logger.debug(
            f'entire_captcha_natural_width {entire_captcha_natural_width}'
        )
        self.captcha_target_name = self.get_captcha_target_name()
        logger.debug(
            f'captcha_target_name {self.captcha_target_name}'
        )
        entire_captcha_element = self.driver.wait.wait_visibility_of_element_CSS('#rc-imageselect-target')
        entire_captcha_url = self.driver.wait.wait_visibility_of_element_CSS('td img').get_attribute('src')
        logger.debug(f'entire_captcha_url {entire_captcha_url}')
        with open(CAPTCHA_ENTIRE_IMAGE_FILE_PATH, 'wb') as f:
            f.write(requests.get(entire_captcha_url).content)
        logger.debug(
            f'saved entire captcha to {CAPTCHA_ENTIRE_IMAGE_FILE_PATH}')
        resized_entire_captcha_base64_string = resize_base64_image(
            CAPTCHA_ENTIRE_IMAGE_FILE_PATH, (entire_captcha_natural_width, entire_captcha_natural_width))
        logger.debug(
            f'resized_entire_captcha_base64_string, {resized_entire_captcha_base64_string[0:100]}...')
        entire_captcha_recognize_result = self.create_task(
            resized_entire_captcha_base64_string,
            get_question_id_by_target_name(self.captcha_target_name)
        )
        if not entire_captcha_recognize_result:
            logger.error('未获得captcha识别结果')
            return
        recognized_indices = entire_captcha_recognize_result.get(
            'solution', {}).get('objects')
        if not recognized_indices:
            logger.error('未获得captcha认可的索引')
            return
        single_captcha_elements = self.driver.wait.wait_visibility_of_elements_CSS('#rc-imageselect-target table td')
        for recognized_index in recognized_indices:
            single_captcha_element = single_captcha_elements[recognized_index]
            single_captcha_element.click()
            # check if need verify single captcha
            self.verify_single_captcha(recognized_index)

        # after all captcha clicked
        verify_button = self.get_verify_button()
        if verify_button.is_displayed:
            verify_button.click()
            time.sleep(3)

        is_succeed = self.get_is_successful()
        if is_succeed:
            logger.debug('验证成功')
        else:
            verify_error_info = self.get_verify_error_info()
            logger.debug(f'verify_error_info {verify_error_info}')
            self.verify_entire_captcha()

    def resolve(self):
        self.trigger_captcha()
        time.sleep(3)
        try:
            self.verify_entire_captcha()
        except BaseException:
            pass