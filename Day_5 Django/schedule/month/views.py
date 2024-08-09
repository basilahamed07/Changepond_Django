from django.shortcuts import render
from django.http import *

# sample function
Month = {
    "jan":"Learning Python",
    "feb":"sleeping",
    "may":"do nothing",
    "april":"april Fool"
}

def month_details(request,month):
    try:
        month_text = Month[month]
        return HttpResponse(f"<h1>{month_text}<h1>")
    except:
        return HttpResponseNotFound(f"<h1>{month} Not Found <h1>")
# Create your views here.
    