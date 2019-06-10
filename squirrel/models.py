from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250, blank = True)
    description = models.CharField(max_length=500, blank = True)
    teaser_text = models.TextField(max_length=500, editable = False, blank = True)
    pub_date = models.DateTimeField('date published', blank = True, null = True)
    download_date = models.DateTimeField('date downloaded', blank = True, null = True)
    author = models.CharField(max_length=250, blank = True)
    publisher = models.CharField(max_length=250, blank = True)
    copyright = models.CharField(max_length=250, blank = True)
    download_url = models.URLField(blank = True)
    source_html = models.TextField(blank = True)
    source_markdown = models.TextField(editable = False)
    wordcount = models.BigIntegerField(editable = False, blank = True, null = True)
    # TODO: readingtime, keywords, previewimage, language
    # TODO: isRead, isStarred
    
    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.download_url
