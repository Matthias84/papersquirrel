import unittest
import codecs
import datetime
from dateutil.tz import tzutc
import os

import squirrel.utils as utils

testpath = os.path.dirname(os.path.abspath(__file__))


class TestUtils(unittest.TestCase):

    def test_metadata_empty(self):
        meta = utils.getMetaData('')
        self.assertEqual(meta, {'title': None,
                                'description': None,
                                'keywords': None,
                                'author': None,
                                'publisher': None,
                                'date_publish': None,
                                'copyright': None,
                                'thumbnail': None})

    def test_metadata_empty_html(self):
        with codecs.open(os.path.join(testpath, 'empty-html.html'), 'r', 'utf-8') as f:
            page = f.read()
            meta = utils.getMetaData(page)
            self.assertEqual(meta, {'title': 'A article Demo',
                                    'description': None,
                                    'keywords': None,
                                    'author': None,
                                    'publisher': None,
                                    'date_publish': None,
                                    'copyright': None,
                                    'thumbnail': None})

    def test_metadata_basic(self):
        with codecs.open(os.path.join(testpath, 'basic-html.html'), 'r', 'utf-8') as f:
            page = f.read()
            meta = utils.getMetaData(page)
            self.assertEqual(meta, {'title': 'A article Demo',
                                    'description': 'My demo for an test article page',
                                    'keywords': ['demo', 'test', 'papersquirrel'],
                                    'author': 'matthias84',
                                    'publisher': 'localhost',
                                    'date_publish': datetime.datetime(2019, 5, 30, 11, 12, 13),
                                    'copyright': None,
                                    'thumbnail': None})

    def test_metadata_ogp(self):
        with codecs.open(os.path.join(testpath, 'ogp.html'), 'r', 'utf-8') as f:
            page = f.read()
            meta = utils.getMetaData(page)
            self.assertEqual(meta, {'title': 'A OGP test',
                                    'description': 'testing opengraph metatags',
                                    'keywords': None,
                                    'author': 'myself',
                                    'publisher': None,
                                    'date_publish': datetime.datetime(2019, 9, 24, 17, 18, 42, tzinfo=tzutc()),
                                    'copyright': None,
                                    'thumbnail': 'localhost/logo.png'})

    def test_markdown(self):
        with codecs.open(os.path.join(testpath, 'basic-html.html'), 'r', 'utf-8') as f:
            page = f.read()
            md = utils.getContentMarkdown(page)
            self.assertEqual(md, """# Demo time

Lorem ipsum, Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem
ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem
ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem
ipsum,Lorem ipsum,

Lorem ipsum, Lorem ipsum, **Lorem ipsum** , _Lorem ipsum_ , ~~Lorem ipsum~~
,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem
ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem
ipsum,Lorem ipsum,Lorem ipsum,

Lorem ipsum, Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem
ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem
ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem ipsum,Lorem
ipsum,Lorem ipsum,

""")

    def test_important_content(self):
        with codecs.open(os.path.join(testpath, 'basic-html.html'), 'r', 'utf-8') as f:
            page = f.read()
            domFiltered = utils.getImportantContentDom(page)
            self.assertEqual(domFiltered.attrs['id'], 'content')

    def test_important_content_article(self):
        """Check filter with <article> tags"""
        with codecs.open(os.path.join(testpath, 'article-html.html'), 'r', 'utf-8') as f:
            page = f.read()
            domFiltered = utils.getImportantContentDom(page, verbose=False)
            self.assertEqual(domFiltered.name, 'article')
            print(domFiltered.attrs)

    def test_important_content_wikipedia(self):
        """Check filter against realworld content, here wikipedia
        https://en.wikipedia.org/wiki/Rostock"""
        with codecs.open(os.path.join(testpath, 'wikipedia-rostock.html'), 'r', 'utf-8') as f:
            page = f.read()
            domFiltered = utils.getImportantContentDom(page, verbose=False)  # enable vebose for debug!
            self.assertEqual(domFiltered.attrs['class'][0], 'mw-parser-output')
            print(domFiltered.attrs)


if __name__ == '__main__':
    unittest.main()
