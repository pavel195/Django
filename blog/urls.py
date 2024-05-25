from django.urls import path
from .views import *

urlpatterns = [
    path('lists/', index),
    path('new/', new_page),
    path('css/', css_page),
    path('some/', dartblog, name='home'),
    path('pseudo/', pseudo),
    path('forms/', forms),
    path('adapt/', adapt),
    path('',Home.as_view(), name= 'home'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('posts/add-news/', add_news, name='add_news')
]
