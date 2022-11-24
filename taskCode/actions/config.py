from taskCode.actions import Query


class Config:
    @staticmethod
    def all_ads():
        all_ads = Query().all_db('ads_config')
        return all_ads

    @staticmethod
    def all_bit():
        all_bit = Query().all_db('bit_config')
        return all_bit

    @staticmethod
    def adsId(x):
        ads_config = Query().search_db('ads_config', x)
        adsId = ads_config[1]
        return adsId

    @staticmethod
    def adsNum(x):
        ads_config = Query().search_db('ads_config', x)
        adsNum = ads_config[2]
        return adsNum

    @staticmethod
    def adsAddress(x):
        ads_config = Query().search_db('ads_config', x)
        adsAddress = ads_config[3]
        return adsAddress

    @staticmethod
    def adsMail(x):
        ads_config = Query().search_db('ads_config', x)
        adsMail = ads_config[4]
        return adsMail

    @staticmethod
    def adsName(x):
        ads_config = Query().search_db('ads_config', x)
        adsName = ads_config[5]
        return adsName

    @staticmethod
    def adsTwitter(x):
        ads_config = Query().search_db('ads_config', x)
        adsTwitter = ads_config[6]
        return adsTwitter

    @staticmethod
    def adsDiscord(x):
        ads_config = Query().search_db('ads_config', x)
        adsDiscord = ads_config[7]
        return adsDiscord

    @staticmethod
    def bitId(x):
        bit_config = Query().search_db('bit_config', x)
        bitId = bit_config[1]
        return bitId

    @staticmethod
    def bitNum(x):
        bit_config = Query().search_db('bit_config', x)
        bitNum = bit_config[2]
        return bitNum

    @staticmethod
    def bitAddress(x):
        bit_config = Query().search_db('bit_config', x)
        bitAddress = bit_config[3]
        return bitAddress

    @staticmethod
    def bitMail(x):
        bit_config = Query().search_db('bit_config', x)
        bitMail = bit_config[4]
        return bitMail

    @staticmethod
    def bitName(x):
        bit_config = Query().search_db('bit_config', x)
        bitName = bit_config[5]
        return bitName

    @staticmethod
    def password():
        others = Query().search_db('others', 1)
        password = others[1]
        return password

    @staticmethod
    def password_next():
        others = Query().search_db('others', 2)
        password = others[1]
        return password

    @staticmethod
    def api_key():
        others = Query().search_db('others', 1)
        API_KEY = others[2]
        return API_KEY

    @staticmethod
    def secret_key():
        others = Query().search_db('others', 2)
        SECRET_KEY = others[2]
        return SECRET_KEY