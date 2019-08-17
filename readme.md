[![Coverage Status](https://coveralls.io/repos/github/Matthias84/papersquirrel/badge.svg?branch=master)](https://coveralls.io/github/Matthias84/papersquirrel?branch=master)
read-it-later clone for easy to setup selfhosting and to training my Django skills and gathering FLOSS team experience.
Before I was unhappy with [wallabag](https://wallabag.org) (esp. administration in selfhosting in VPS) and Mozilla [pocket](https://support.mozilla.org/de/kb/was-ist-pocket) (tied to firefox, no selfhosting, ...).

So you read a lot of texts on the web, that you want to read later, while on a ride? Just save content from online blogs, newspages, magazines, ... to your devices using your own service.
Similar to wallabag / mozilla pocket / instapaper / ... this webapplication will extract text and image content together with metadata and recombines it as simplified webpages or ebooks to read it later on misc. devices while offline.

## Features

    Still work-in-progress and pre-alpha!

Planned features are
* copy HTML, dump media, extract preview, export to markdown, pdf, , ..., 
* integrate via browser, emulate wallabag API, share with others public, offer articles via opds / rss / ...
* multi-user

## What it is  NOT

* serving a whole enterprise, only smal teams
* dump wikipedia (use [kiwix](http://www.kiwix.org) for Mediawikis instead)
* store videos, multimedia, ... (use [youtube-dl](https://ytdl-org.github.io) frontends instead)
* filter social media streams, ... (use [huginn](https://github.com/huginn/huginn), ... instead)
* outlines and file storage (use evernote / mendeley] / ... [clones](https://github.com/Kickball/awesome-selfhosted#note-taking-and-editors) instead)
* only bookmarking (see [selfhosted bookmarking](https://github.com/Kickball/awesome-selfhosted#bookmarks-and-link-sharing))
* custom webpage content scraper (use [DDS](https://django-dynamic-scraper.readthedocs.io) instead)


## Install

* create a python virtualenv and `pip -r requirements.txt`
* clone git repository
* `cd /papersquirrel/settings` to copy and adapt a local config from template
* `python3 manage.py migrate --settings papersquirrel.settings.local`
* `python3 manage.py makesuperuser --settings papersquirrel.settings.local`

To test your setup, try to invoke it like

* `python3 manage.py runserver --settings papersquirrel.settings.local`
* open `http://127.0.0.1:8000/squirrel/`

For production please use an uWSGI config that invokes `papersquirrel/wsgi.py`
See Django docs for snippets.

## Update

* stop your service 
* backup the database
* pull git repository
* run `python3 manage.py migrate --settings papersquirrel.settings.local`
* restart your service 

## Contribute

Please note that I'm not familar with maintaining a FLOSS project, so please be patient :)

For submitting bugs / feature requests please visit the [github project](https://github.com/Matthias84/papersquirrel).

Before submitting pull requests, please start a issue, to talk about your idea.
Then you can start local development, by adding `pip install flake8 coverage`.
Please add tests to make sure, that you don't drop code test coverage. Check them via `python3 manage.py test --settings papersquirrel.settings.local`
Also check code quality using flake8, to get the right layout.


## Thanks

This software makes use of great libraries and frameworks that are maintained by others:
* [html2text](https://github.com/aaronsw/html2text) to extract rich formated text as markdown
* [beautifulsoup4]() python HTML parser lib
* django2 web framework
* bootstrap web frontend framework
