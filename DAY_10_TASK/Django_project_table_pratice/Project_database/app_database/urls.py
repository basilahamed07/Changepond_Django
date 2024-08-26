from django.urls import path
from . import views
urlpatterns = [
    path("command_form",views.Commnad_postModels.as_view() )
]
