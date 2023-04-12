from .carv import Carv
from .coingecko import Coingecko
from .coinmarketcap import Coinmarketcap
from .discord import Discord
from .goerliETH import GoerliETH
from .layer3 import Layer3
from .wallet import Wallet
from .other import Other
from .scroll import Scroll
from .twitter import Twitter
from .zetalabs import Zetalabs
from .discord_Xpath import discord
from .fusionist import fusionist


class taskBase:
    driver = None

    def __init__(self, driver):
        self.wallet = Wallet(driver)
        self.carv = Carv(driver)
        self.goerliETH = GoerliETH(driver)
        self.zetalabs = Zetalabs(driver)
        self.coinmarketcap = Coinmarketcap(driver)
        self.scroll = Scroll(driver)
        self.coingecko = Coingecko(driver)
        self.discord = Discord(driver)
        self.discords = discord(driver)
        self.twitter = Twitter(driver)
        self.layer3 = Layer3(driver)
        self.other = Other(driver)
        self.fusionist = fusionist(driver)
