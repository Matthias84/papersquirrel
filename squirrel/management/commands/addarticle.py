from django.core.management.base import BaseCommand, CommandError
from squirrel.models import Article

class Command(BaseCommand):
    help = 'Add article and fetch URL'
    
    def add_arguments(self, parser):
        parser.add_argument('url', type=str)
    
    def handle(self, *args, **options):
        url = options['url']
        article = Article.add(url)
        self.stdout.write(self.style.SUCCESS('Successfully added with ID "%s"' % article.id))
