from django.urls import path
from .views import *
urlpatterns = [
    path("index",index),
    path("<str:authors>",Authorss, name="author_name"),
]
