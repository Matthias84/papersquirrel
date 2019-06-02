from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Article


class IndexView(generic.ListView):
    template_name = 'squirrel/index.html'
    context_object_name = 'latest_article_list'
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Article.objects.order_by('-download_date')[:5]
