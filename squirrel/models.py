from django.db import models

from django.utils import timezone


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=500, blank=True)
    teaser_text = models.TextField(max_length=500, editable=False, blank=True)
    pub_date = models.DateTimeField('date published', blank=True, null=True)
    download_date = models.DateTimeField('date downloaded', blank=True, null=True)
    author = models.CharField(max_length=250, blank=True)
    publisher = models.CharField(max_length=250, blank=True)
    copyright = models.CharField(max_length=250, blank=True)
    download_url = models.URLField(blank=True)
    source_html = models.TextField()
    source_markdown = models.TextField(editable=False)
    wordcount = models.BigIntegerField(editable=False, blank=True, null=True)
    # TODO: readingtime, keywords, previewimage, language
    # TODO: isRead, isStarred

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.download_url

    @classmethod
    def add(Article, url):
        """Fetch page and add as an article"""
        # TODO: SECURITY check if file:// localhost, 127, 00: links to list server content
        article = Article(download_url=url, download_date=timezone.now(), source_html='<html></html>')
        article.save()
        return article
