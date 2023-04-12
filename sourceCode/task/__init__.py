from .carv import Carv
from .coingecko import Coingecko
from .coinmarketcap import Coinmarketcap


class Task:

    def __init__(self, page, browser):
        self.carv = Carv(page, browser)
        self.coingecko = Coingecko(page, browser)
        self.coinmarketcap = Coinmarketcap(page, browser)