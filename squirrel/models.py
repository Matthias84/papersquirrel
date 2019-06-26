from django.db import models
from django.utils import timezone

from squirrel.utils import downloadPage, getMetaData


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    teaser_text = models.TextField(max_length=500, editable=False, blank=True)
    pub_date = models.DateTimeField('date published', blank=True, null=True)
    download_date = models.DateTimeField('date downloaded', blank=True, null=True)
    author = models.CharField(max_length=250, blank=True, null=True)
    publisher = models.CharField(max_length=250, blank=True, null=True)
    copyright = models.CharField(max_length=250, blank=True, null=True)
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

    def save(self, *args, **kwargs):
        """Save and refresh meta data"""
        meta = getMetaData(self.source_html)
        self.title = meta['title']
        self.description = meta['description']
        self.author = meta['author']
        self.publisher = meta['publisher']
        self.pub_date = meta['date_publish']
        self.copyright = meta['copyright']
        super().save(*args, **kwargs)

    @classmethod
    def add(Article, url, html_source=None):
        """Fetch page and add as an article. If source provided, it is used as page content instead"""
        # TODO: SECURITY check if file:// localhost, 127, 00: links to list server content
        if html_source:
            article = Article(download_url=url, download_date=timezone.now(), source_html= html_source)
            article.save()
        return article
