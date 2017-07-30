#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from uuid import uuid4

AUTHOR = 'Jason L. Weirather, Ph.D.'
SITENAME = 'fasta.io'
SITESUBTITLE = 'a bioinformatics engineer going on adventures'
SITEHOOK = 'lost in a random forest of trees'
SITEEMOJIS = '🌳🌲🌳🤓🗺🌴🌳🌲'
SITEURL = 'http://fasta.io'
THEME = "../fasta-theme/"

def get_uuid4_string(not_used):
   return str(uuid4())

JINJA_FILTERS = {'uuid4':get_uuid4_string}

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('github', 'https://github.com/jason-weirather'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
OUTPUT_PATH = '../'
