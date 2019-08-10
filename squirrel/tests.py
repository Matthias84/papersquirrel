import codecs
import datetime
import os


from django.test import TestCase
from django.utils import timezone

from .models import Article


class ArticleModelTests(TestCase):
    def test_add_basic(self):
        """
        Minimal create and fetch article scenario
        """
        article = Article.add('https://localhost','' ,html_source='<html></html>')
        self.assertEqual(article.id, 1)
        self.assertTrue(timezone.now() - datetime.timedelta(seconds=30) < article.download_date < timezone.now())
        self.assertEqual(article.source_html, '<html></html>')

    def test_add_empty(self):
        article = Article.add('https://localhost','' , html_source='<html></html>')
        self.assertEqual(article.id, 1)
        self.assertEqual(article.source_html, '<html></html>')

    def test_add_content_analysis(self):
        with codecs.open('./squirrel/tests/basic-html.html', 'r', 'utf-8') as f:
            src = f.read()
            article = Article.add('https://localhost/basic-html/', '', html_source=src)
            self.assertEqual(article.source_html, src)
