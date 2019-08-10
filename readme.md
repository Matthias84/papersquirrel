[![Coverage Status](https://coveralls.io/repos/github/Matthias84/papersquirrel/badge.svg?branch=master)](https://coveralls.io/github/Matthias84/papersquirrel?branch=master)
read-it-later clone for simple selfhosting and training my Django skills and gathering FLOSS team experience.
Before I was unhappy with wallabag (esp. administration in selfhosting in VPS) and Mozilla pocket (tied to firefox profiles, no selfhosting).

You read a lot of texts on the web, that you want to read later, while on a ride? Just save content from online blogs, newspages, magazines, ... to your devices using your server.
Similar to wallabag / mozilla pocket / instapaper / ... this webapplication will extract text and image content together with metadata and recombines it as easy to read webpages and ebooks for later offline reading on different devices.

## Features

Still work-in-progress and pre-alpha!
Planned features as
* copy HTML, dump media, extract preview, export to markdown, pdf, , ..., 
* integrate via browser, emulate wallabag API, share with others public, offer articles via opds / rss / ...
* multi-user

## What it is  NOT

* for small teams, not serving the whole WWW
* dump wikipedia (use kiwix for Mediawikis instead)
* store videos, multimedia, ... (use youtube-dl frontends instead)
* filter social media streams, ... (use huginn, ... instead)
* outlines and file storage (use evernote / mendeley / ... clones instead)
* only bookmarking (see selfhosted bookmarking)
* custom webpage content scraper (use [DDS](https://django-dynamic-scraper.readthedocs.io) instead)


## Install

* adapt copy and adapt config template at `/papersquirrel/settings`
* `python3 manage.py runserver --settings papersquirrel.settings.local`
* open `http://127.0.0.1:8000/squirrel/`

## Contribute

Please note that I'm not familar with maintaining a FLOSS project, so please be patient :)


## Thanks

This software makes use of great libraries and frameworks that are maintained by others:
* https://github.com/aaronsw/html2text
* django2
* markdown
