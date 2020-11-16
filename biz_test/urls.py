from django.urls import path
from . import views

urlpatterns = [
    path("", views.biz1, name="biz1"),
    path("UALIndex/", views.UALview, name="UsageAddresLIst"),
]