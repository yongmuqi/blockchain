from django.conf import settings
from django.contrib import admin
from django.views import static
from django.urls import path, include

import web
from web import views, urls

urlpatterns = [
    #    path('admin/', admin.site.urls),
    path('', views.index, name='home'),

    path('', include(web.urls)),
]
