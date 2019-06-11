import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Article


# Create your tests here.
class ArticleModelTests(TestCase):
    def test_add_basic(self):
        """
        Minimal create and fetch article scenario
        """
        article = Article.add('https://localhost')
        self.assertEqual(article.id, 1)
        self.assertTrue(timezone.now() - datetime.timedelta(seconds=30) < article.download_date < timezone.now())
