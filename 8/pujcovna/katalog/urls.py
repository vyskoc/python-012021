from django.urls import path
from . import views #views je ve stejným adresáři jako soubor urls.py

urlpatterns = [
    path("", views.IndexView.as_view(),name = "index"),
    path("seznam/", views.SeznamView.as_view(),name = "index")
]