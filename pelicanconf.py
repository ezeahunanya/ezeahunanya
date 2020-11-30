#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Eze Ahunanya'
SITENAME = 'Eze Ahunanya'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Email', 'mailto: ezeahunanya@outlook.com'),
         )

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/ezeahunanya//'),
         ('GitHub', 'https://github.com/ezeahunanya'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

INDEX_SAVE_AS = 'blog/index.html'

DISPLAY_CATEGORIES_ON_MENU = False

DELETE_OUTPUT_DIRECTORY = True

ARTICLE_URL = 'blog/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

ARTICLE_PATHS = ['blog']

MENUITEMS = [
 ('Home', '/'),
 ('Blog', '/blog'),]
