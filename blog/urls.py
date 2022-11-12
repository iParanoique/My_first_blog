from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', PostByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostByTag.as_view(), name='tag'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('search/', Search.as_view(), name='search'),
    path('comment/<int:pk>/', AddComment.as_view(), name='comment'),
]
