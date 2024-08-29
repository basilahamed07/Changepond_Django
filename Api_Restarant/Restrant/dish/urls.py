from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import catogoryViewset
 
 
 #prebuild code for swagger api
router = DefaultRouter()
router.register('', catogoryViewset, basename='author')
app_name ='author'
 
urlpatterns=[
    path('', include(router.urls)),
]