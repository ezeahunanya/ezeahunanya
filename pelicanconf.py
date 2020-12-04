#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Eze Ahunanya'
SITENAME = 'Eze Ahunanya'
SITETITLE = 'Eze Ahunanya'
SITESUBTITLE = 'Learning is a lifelong process'
SITEURL = 'http://localhost:8000'
# SITELOGO = ''
# FAVICON = '/images/favicon.ico'
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

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
LINKS = (('ezeahunanya@outlook.com', 'mailto: ezeahunanya@outlook.com'),
         )

# Social widget
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/ezeahunanya/'),
    ('github', 'https://github.com/ezeahunanya'),
)
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "/Users/user/OneDrive/Documents/projects/pelican-themes/Flex"

INDEX_SAVE_AS = 'blog/index.html'

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

DISPLAY_CATEGORIES_ON_MENU = False

DELETE_OUTPUT_DIRECTORY = True

ARTICLE_URL = 'blog/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

ARTICLE_PATHS = ['blog']

MENUITEMS = (
 ('Blog', '/blog'),
 ('Projects', '/projects'),
)

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True
