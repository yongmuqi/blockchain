from taskCode.actions import Query


class Config:
    def __init__(self):
        self.q = Query()

    def adsId(self, x):
        ads_config = self.q.search_db('ads_config', x)
        adsId = ads_config[1]
        return adsId

    def adsNum(self, x):
        ads_config = self.q.search_db('ads_config', x)
        adsNum = ads_config[2]
        return adsNum

    def adsAddress(self, x):
        ads_config = self.q.search_db('ads_config', x)
        adsAddress = ads_config[3]
        return adsAddress

    def adsMail(self, x):
        ads_config = self.q.search_db('ads_config', x)
        adsMail = ads_config[4]
        return adsMail

    def adsName(self, x):
        ads_config = self.q.search_db('ads_config', x)
        adsName = ads_config[5]
        return adsName

    def adsTwitter(self, x):
        ads_config = self.q.search_db('ads_config', x)
        adsTwitter = ads_config[6]
        return adsTwitter

    def adsDiscord(self, x):
        ads_config = self.q.search_db('ads_config', x)
        adsDiscord = ads_config[7]
        return adsDiscord

    def bitId(self, x):
        bit_config = self.q.search_db('bit_config', x)
        bitId = bit_config[1]
        return bitId

    def bitNum(self, x):
        bit_config = self.q.search_db('bit_config', x)
        bitNum = bit_config[2]
        return bitNum

    def bitAddress(self, x):
        bit_config = self.q.search_db('bit_config', x)
        bitAddress = bit_config[3]
        return bitAddress

    def bitMail(self, x):
        bit_config = self.q.search_db('bit_config', x)
        bitMail = bit_config[4]
        return bitMail

    def bitName(self, x):
        bit_config = self.q.search_db('bit_config', x)
        bitName = bit_config[5]
        return bitName

    def password(self):
        others = self.q.search_db('others', 1)
        password = others[1]
        return password

    def password_next(self):
        others = self.q.search_db('others', 2)
        password = others[1]
        return password