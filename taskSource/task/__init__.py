from .carv import Carv
from .coingecko import Coingecko
from .discord import Discord
from .layer3 import Layer3
from .wallet import Wallet
from .zetalabs import Zetalabs
from .fusionist import Fusionist
from .coinmarketcap import CoinMarketCap
from .scroll import Scroll
from .others import Others


class Task:
    driver = None

    def __init__(self, driver):
        self.carv = Carv(driver)
        self.coingecko = Coingecko(driver)
        self.discord = Discord(driver)
        self.layer3 = Layer3(driver)
        self.wallet = Wallet(driver)
        self.zetalabs = Zetalabs(driver)
        self.fusionist = Fusionist(driver)
        self.coinmarketcap = CoinMarketCap(driver)
        self.scroll = Scroll(driver)
        self.others = Others(driver)
