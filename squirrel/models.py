from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    teaser_text = models.TextField(max_length=500, editable = False)
    pub_date = models.DateTimeField('date published')
    download_date = models.DateTimeField('date downloaded')
    author = models.CharField(max_length=250)
    publisher = models.CharField(max_length=250)
    copyright = models.CharField(max_length=250)
    download_url = models.URLField()
    source_html = models.TextField()
    source_markdown = models.TextField()
    wordcount = models.BigIntegerField()
    # TODO: readingtime, keywords, previewimage, language
    # TODO: isRead, isStarred
