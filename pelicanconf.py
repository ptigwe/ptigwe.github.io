#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tobenna Peter, Igwe'
SITENAME = 'PTIGWE'
SITEURL = 'http://localhost:8000'
SITESUBTITLE = ' '

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/ptigwe'),
        ('github', 'https://github.com/ptigwe'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'pelican-clean-blog'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets', 'sitemap', 'i18n_subsites', 'extract_toc']

SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = True
SHOW_SITESUBTITLE_IN_HTML = True

SITEMAP = {
        'format' : 'txt',
        'exclude': ['tag/', 'category/']
        }

DEFAULT_CATEGORY = 'misc'

CC_LICENSE = 'CC-BY-NC-SA'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

I18N_SUBSITES = {
        'ja': {
            'AUTHOR': u'イグエ・トベンナ・ぺーたー',
            'LOCALE': 'ja_JP.utf8',
            }
        }
