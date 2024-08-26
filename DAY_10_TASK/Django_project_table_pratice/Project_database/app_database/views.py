from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView


# Create your views here.


#creating the command post sections:
class Commnad_postModels(CreateView):
    model = Comment
    template_name = "app_database/command_forms.html"
    success_url = "command_form"
    fields = "__all__"
