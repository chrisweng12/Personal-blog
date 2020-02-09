from django.shortcuts import render
from .models import Articles
from django.http import HttpResponse

# Create your views here.
def article_list(request):
    articles = Articles.objects.all().order_by("date")
    return render(request, "articles/article_list.html", {"articles":articles})

def article_details(request, slug):
    #return HttpResponse(slug)
    article = Articles.objects.get(slug = slug)
    
    return render(request,"articles/article_detail.html",{"article":article})