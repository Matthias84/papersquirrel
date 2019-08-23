from django.urls import path

from . import views


app_name = 'squirrel'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('article/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('article/add', views.add_article, name='add'),
    path('article/<int:pk>/read', views.mark_read, name='mark_read'),
    path('article/<int:pk>/download?format=html', views.download_html, name='download_html'),
    path('article/<int:pk>/download?format=markdown', views.download_md, name='download_md'),
]
