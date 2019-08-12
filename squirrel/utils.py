#!/usr/bin/env python

import codecs
import datetime
import re
import requests
import html2text
from bs4 import BeautifulSoup
from dateutil import parser as duparser


def downloadPage(url,useragent = 'papersquirrel/0.1 (Linux; ) requests/2.22'):
    """Download HTML page via HTTP following redirects, encodings, ..."""
    # TODO: Detect status codes and MIME headers
    r = requests.get(url, headers = {'User-Agent': useragent,
                                    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'})
    return r.text


def getMetaData(html):
    """Extract some metadata of HTML document as dict"""
    # TODO: prefer OGP / RDF / SM / ... metadata
    dom = BeautifulSoup(html, 'html.parser')
    title = None
    description = None
    kw = None
    author = None
    publisher = None
    date_publish = None
    copyright = None
    if dom.title:
        title = dom.title.string
        if title.find('|') > -1:
            title = title.split('|')[0].rstrip()
            # TODO: check if second part is domain or author
    for meta in dom.find_all('meta'):
        try:
            if meta['name'] == 'description':
                description = meta['content']  # TODO: remove possible HTML garbage within
            if meta['name'] == 'keywords':
                keywords = meta['content']
                keywords = keywords.split(',')
                kw = []
                for word in keywords:
                    word = word.strip()
                    kw.append(word)
            if meta['name'] == 'author':
                author = meta['content']
            if meta['name'] == 'publisher':
                publisher = meta['content']
            if meta['name'] == 'date':
                date_publish = meta['content']
                date_publish = duparser.parse(date_publish)
        except KeyError:
            pass
    for link in dom.find_all('link'):
        if link.rel:
            if link['rel'] == 'copyright':
                copyright = link['href']
    return {'title': title,
            'description': description,
            'keywords': kw,
            'author': author,
            'publisher': publisher,
            'date_publish': date_publish,
            'copyright': copyright}


def getContentPlainText(html):
    """Returns page text as human readable plaintext"""
    # TODO: Skip navigation, inline JS, widgets, newlines, ...
    dom = BeautifulSoup(html, 'html.parser')
    return dom.get_text()

def getContentMarkdown(html):
    """Returns page text as richtext markdown"""
    return html2text.html2text(html)

def getImportantContentDom(html, verbose = False):
    '''
    Return <div> element that wraps text incl. headings but doesn't include menus /...
    
    Traverse DOM and calculate content weigth per element (wordcount).
    '''
    MIN_TEXT_RATIO = 0.65
    dom = BeautifulSoup(html, 'html.parser')
    txt = dom.body.get_text()
    wordcountTotal = len(re.findall(r'\w+', txt))
    if verbose:
        print("Body words: ", wordcountTotal)
    candidate = (0, None)
    # crawl down and get percentage of words below this child element
    for child in dom.descendants:
        if child.name == 'div':
            highlight = ''
            hierachy = ""
            wordcountChild = len(re.findall(r'\w+', child.get_text()))
            # keep as little infos as possible -> till below word ratio
            if (wordcountChild / wordcountTotal) >= MIN_TEXT_RATIO:
                    candidate = child
                    highlight = '\033[94m'
            if verbose:
                #print debug infos
                level = 0
                for parent in child.parents:
                    hierachy = parent.name + '.' +hierachy
                    level = level +1
                label = ''
                if 'class' in child.attrs :
                    label = child['class']
                print(highlight, hierachy,child.name, level, label, wordcountChild, '\033[0m')
    return candidate

def main(args):
    return 0


if __name__ == '__main__':
    url = 'https://www.tagesschau.de/inland/eu-wahl-111.html'
#    page = downloadPage(url)
#    with codecs.open('tagesschau_artikel.html', "w", 'utf-8') as f:
#        f.writelines(page)
    with codecs.open("./test/test-assets/Behörde genehmigt das 'Fusion Festival'   NDR.de - Nachrichten - Mecklenburg-Vorpommern.html", 'r', 'utf-8') as f:
        page = f.read()
        # print(page)
        meta = getMetaData(page)
        meta['origin_url'] = url
        meta['date_download'] = datetime.datetime.now()
        # print(meta)
        # print(getContentPlainText(page))
        # print(getContentMarkdown(page))
        # printContentWeights(page)
        md = getContentMarkdown(str(getImportantContentDom(page)))
        print(md)
        
