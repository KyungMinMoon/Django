# board/urls.py
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # articles/create/
    path('create/', views.create_article, name='create_article'),
    # articles/
    path('', views.article_index, name='article_index'),
    # articles/1/
    path('<int:article_pk>/', views.article_detail, name='article_detail'),
    # articles/1/comments/create/
    path('<int:article_pk>/comments/create/', views.create_comment, name='create_comment'),
    # articles/1/comments/2/delete/
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
]