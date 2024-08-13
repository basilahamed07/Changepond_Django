from django.shortcuts import render
from django.http import *
from .models import Author
# Create your views here.
def Authorss(request,authors):
    try:
        author = authors.split()
        print(author)
        # print(Author.objects.get(First_name=author[0]))
        lists = list((Author.objects.all()))
        # for trash in range(0,len(lists)):
        #     print(lists = Author.objects.all()[trash])
        responce_data = render(request,"authors/author_name.html",{"text":(Author.objects.get(First_name=author[0]))})
        return HttpResponse(responce_data)
    except:
        return HttpResponse("bad request")

def index(request):
    return render(request,"authors/authors.html",{"author":Author.objects.all()})

def month_details(request,month):
    try:
        month_text = Month[month]
        # responce_data = render_to_string("month/month.html")
        responce_data = render(request,"month/month.html",{"text":month_text})
        return HttpResponse(responce_data)
    except:
        return HttpResponseNotFound(f"<h1>{month} Not Found <h1>")