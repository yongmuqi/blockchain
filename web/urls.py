from django.urls import path
from web import views

urlpatterns = [
    path('list/', views.list),

    path('bitlist/', views.bitlist),

    path('status/', views.status),

    path('bitstatus/', views.bitstatus),

    path('adspower/', views.adspower),

    path('bitbrowser/', views.bitbrowser),

    path('others/', views.others),

    path('othersads/', views.othersAds),

    path('othersbit/', views.othersBit),

    path('runTask/', views.runTask),

    path('bitTask/', views.bitTask),

    path('adsAllTask/', views.adsAllTask),

    path('bitAllTask/', views.bitAllTask),

    path('runFailTask/', views.runFailTask),

    path('runAdsFailTask/', views.runAdsFailTask),

]