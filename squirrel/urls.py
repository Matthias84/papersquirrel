from django.urls import path

from . import views


app_name = 'squirrel'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('article/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('article/add', views.add_article, name='add'),
]
