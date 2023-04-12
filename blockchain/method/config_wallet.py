from .mysql import Mysql


class Config_Wallet:
    @staticmethod
    def adsMetaMask(x):
        ads_config = Mysql().search_db('ads_wallet', x)
        adsMetaMask = ads_config[2]
        return adsMetaMask

    @staticmethod
    def adsPhantom(x):
        ads_config = Mysql().search_db('ads_wallet', x)
        adsPhantom = ads_config[4]
        return adsPhantom

    @staticmethod
    def adsKeplr(x):
        ads_config = Mysql().search_db('ads_wallet', x)
        adsKeplr = ads_config[6]
        return adsKeplr

    @staticmethod
    def adsSui(x):
        ads_config = Mysql().search_db('ads_wallet', x)
        adsSui = ads_config[8]
        return adsSui

    @staticmethod
    def adsArgentX(x):
        ads_config = Mysql().search_db('ads_wallet', x)
        adsArgentX = ads_config[10]
        return adsArgentX

    @staticmethod
    def adsPetra(x):
        ads_config = Mysql().search_db('ads_wallet', x)
        adsPetra = ads_config[12]
        return adsPetra

    @staticmethod
    def adsMartian(x):
        ads_config = Mysql().search_db('ads_wallet', x)
        adsMartian = ads_config[14]
        return adsMartian

    @staticmethod
    def adsFuel(x):
        ads_config = Mysql().search_db('ads_wallet', x)
        adsFuel = ads_config[16]
        return adsFuel
