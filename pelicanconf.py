#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Goran Peretin'
SITENAME = u"Goran Peretin"
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

GOOGLE_ANALYTICS = 'UA-32940905-1'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = False
PATH = 'content'
ARTICLE_DIR = 'posts'
PAGE_DIR = 'pages'

ARTICLE_URL = '{slug}'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME='themes/vapor'

TEMPLATE_PAGES = {
        'talks.html': 'talks.html'
    }
