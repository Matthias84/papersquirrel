from io import StringIO
from django.shortcuts import render
from django.http import HttpResponseRedirect, FileResponse
from django.urls import reverse
from django.utils.text import slugify
from django.views import generic

from .models import Article
from .forms import AddArticleForm


class IndexView(generic.ListView):
    template_name = 'squirrel/index.html'
    context_object_name = 'latest_article_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Article.objects.order_by('-download_date')[:5]


class DetailView(generic.DetailView):
    model = Article
    template_name = 'squirrel/detail.html'


def add_article(request):
    '''Form to add and fetch a new article'''
    if request.method == 'POST':
        form = AddArticleForm(request.POST)
        if form.is_valid():
            dlurl = form.cleaned_data['download_url']
            article = Article.add(url=dlurl)
            article.save()
            return HttpResponseRedirect(reverse('squirrel:detail', args=(article.id,)))
    else:
        form = AddArticleForm()
    return render(request, 'squirrel/add.html', {'form': form})

def download_html(request, pk):
    '''Generate HTML file with original article source'''
    article = Article.objects.get(pk=pk)
    buff = StringIO(article.source_html)
    response = FileResponse(buff.getvalue(), as_attachment=True)
    response['Content-Disposition'] = 'attachment; filename="'+slugify(article.title)+'.html"' # name need to be set this way
    return response

def download_md(request, pk):
    '''Generate HTML file with original article source'''
    article = Article.objects.get(pk=pk)
    buff = StringIO(article.getMarkdown())
    response= FileResponse(buff.getvalue(), as_attachment=True, content_type='text/markdown')
    response['Content-Disposition'] = 'attachment; filename="'+slugify(article.title)+'.md"' # name need to be set this way
    return response
