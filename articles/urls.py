from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_topics, name='list_topics'),
    path('headlines/<int:pk>/', views.list_headlines, name='headlines'),
    path('article/<int:pk>/', views.details, name='article_details'),
    path('article/new/', views.add_article, name='new_article'),
    path('article/edit/<int:pk>', views.edit_article, name='edit_article'),
    path('article/delete/<int:pk>', views.delete_article, name='delete_article')
]
