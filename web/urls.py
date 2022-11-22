from django.urls import path
from web import views

urlpatterns = [
    path('list/', views.list),

    path('status/', views.status),

    path('runTask/', views.runTask),
]