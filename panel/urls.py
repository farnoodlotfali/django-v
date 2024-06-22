
from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "Panel"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("teleposts/", views.get_user_posts_view, name="get_user_posts"),
    path("test/", views.getPhoneNumberAndCode, name="test"),

]
