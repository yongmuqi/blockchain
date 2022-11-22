import operator

from aip import AipOcr
from taskCode.actions.config import Config


class Baidu:
    # 封装百度图片文字识别并返回文字坐标,输入需要识别的文案和图片地址，返回文案在图片上的坐标
    @staticmethod
    def baidu_return_cordinate(text, imagepath):
        APP_ID = '27563132'
        API_KEY = Config.api_key()
        SECRET_KEY = Config.secret_key()
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        # 读取图片
        with open(imagepath, 'rb') as fp:
            # 识别到信息以字典形式返回
            dic = client.accurate(fp.read())
            # 遍历字典与想要的文案对比，如果对比到就返回坐标
            for word in dic.get("words_result"):
                if operator.contains(word.get("words"), text):
                    return [word['location']['top'], word['location']['left']]
            else:
                return None
