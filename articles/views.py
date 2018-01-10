from django.http import HttpResponse

from django.shortcuts import render
from .models import Article
import random


def articles_create(request):
	return render(request, 'home.html',{})

def articles_detail(request):
	return render(request, 'detail.html',{})

def articles_update(request):

	mylist = Article.objects.all()

	Laura = {"user": request.user,
		"number": random.randint(1,1000),
		"mylist": mylist
		}
	return render(request, 'update.html',Laura)

def articles_list(request, article_id):

	updates = Article.objects.get(id=article_id)

	stuff= {
	"hey":updates,
	"hello":"thing"
	}

	return render(request, 'list.html',stuff)

def articles_delete(request):
	return HttpResponse("<h1> Delete </h1>")

# Create your views here.
