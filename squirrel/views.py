from io import StringIO
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, FileResponse
from django.urls import reverse
from django.utils.text import slugify
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article
from .forms import AddArticleForm


class IndexView(generic.ListView):
    template_name = 'squirrel/index.html'
    context_object_name = 'latest_article_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Article.objects.order_by('-download_date')


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Article
    template_name = 'squirrel/detail.html'


@login_required
def add_article(request):
    '''Form to add and fetch a new article'''
    if request.method == 'POST':
        form = AddArticleForm(request.POST)
        if form.is_valid():
            dlurl = form.cleaned_data['download_url']
            agent = form.cleaned_data['useragent']
            print(agent)
            article = Article.add(url=dlurl, useragent=agent)
            article.save()
            return HttpResponseRedirect(reverse('squirrel:detail', args=(article.id,)))
    else:
        form = AddArticleForm()
    return render(request, 'squirrel/add.html', {'form': form})


@login_required
def mark_read(request, pk):
    '''Set article as marked'''
    article = Article.objects.get(pk=pk)
    article.isRead = not article.isRead
    article.save()
    return redirect('squirrel:index')


@login_required
def download_html(request, pk):
    '''Generate HTML file with original article source'''
    article = Article.objects.get(pk=pk)
    buff = StringIO(article.source_html)
    response = FileResponse(buff.getvalue(), as_attachment=True)
    response['Content-Disposition'] = 'attachment; filename="' + slugify(article.title) + '.html"'  # name need to be set this way
    return response


@login_required
def download_md(request, pk):
    '''Generate HTML file with original article source'''
    article = Article.objects.get(pk=pk)
    buff = StringIO(article.getMarkdown())
    response = FileResponse(buff.getvalue(), as_attachment=True, content_type='text/markdown')
    response['Content-Disposition'] = 'attachment; filename="' + slugify(article.title) + '.md"'  # name need to be set this way
    return response
