from django.contrib import admin
from django.urls import path

from articles import views





urlpatterns =[ 

	path('create/', views.articles_create, name="url1"),

	path('detail/', views.articles_detail, name="url2"),

	path('list/<int:article_id>/', views.articles_list, name="url3"),

	path('update/', views.articles_update, name="url4"),

	path('delete/', views.articles_delete, name="url5"),

 ]
