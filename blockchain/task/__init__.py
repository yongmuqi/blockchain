from .carv import Carv
from .coingecko import Coingecko
from .layer3 import Layer3
from .wallet import Wallet
from .zetalabs import Zetalabs
from .coinmarketcap import CoinMarketCap


class Task:
    driver = None

    def __init__(self, driver):
        self.carv = Carv(driver)
        self.coingecko = Coingecko(driver)
        self.layer3 = Layer3(driver)
        self.wallet = Wallet(driver)
        self.zetalabs = Zetalabs(driver)
        self.coinmarketcap = CoinMarketCap(driver)