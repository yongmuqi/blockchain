from django.db import models


class AdsTask(models.Model):

    id = models.CharField(db_column='id', max_length=255, blank=True, null=True)
    dayTime = models.CharField(db_column='dayTime', max_length=255, blank=True, primary_key=True)
    runTime = models.CharField(db_column='runTime', max_length=255, blank=True, null=True)
    MetaMask = models.CharField(db_column='MetaMask', max_length=255, blank=True, null=True)
    Carv = models.CharField(db_column='Carv', max_length=255, blank=True, null=True)
    Coinmarketcap = models.CharField(db_column='CoinMarketcap', max_length=255, blank=True, null=True)
    Coingecko = models.CharField(db_column='CoinGecko', max_length=255, blank=True, null=True)
    ZetalabsTime = models.CharField(db_column='ZetalabsTime', max_length=255, blank=True, null=True)
    Zetalabs = models.CharField(db_column='Zetalabs', max_length=255, blank=True, null=True)
    GoerliETH = models.CharField(db_column='GoerliETH', max_length=255, blank=True, null=True)
    CarvDragonball = models.CharField(db_column='CarvDragonball', max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ads_task'
