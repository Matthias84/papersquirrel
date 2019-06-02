from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250, blank = True)
    description = models.CharField(max_length=500, blank = True)
    teaser_text = models.TextField(max_length=500, editable = False, blank = True)
    pub_date = models.DateTimeField('date published', blank = True, null = True)
    download_date = models.DateTimeField('date downloaded')
    author = models.CharField(max_length=250, blank = True)
    publisher = models.CharField(max_length=250, blank = True)
    copyright = models.CharField(max_length=250, blank = True)
    download_url = models.URLField()
    source_html = models.TextField()
    source_markdown = models.TextField(editable = False)
    wordcount = models.BigIntegerField(editable = False, blank = True, null = True)
    # TODO: readingtime, keywords, previewimage, language
    # TODO: isRead, isStarred
    
    def __str__(self):
        return self.title
