#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# # Fix for ipynb plugin https://github.com/danielfrg/pelican-ipynb/issues/49
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")


AUTHOR = 'Gaurav Modi'
SITENAME = 'Gaurav Modi'
SITEURL = ''
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

PATH = 'content'





# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images',]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Style
TYPOGRIFY = True
# themes configuration
THEME = "./themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'sandstone'
PYGMENTS_STYLE = 'monokai'
AUTHOR = 'Gaurav Modi'
FAVICON = './favicon.ico'


# ipynb configuration
MARKUP = ('md', 'ipynb', )
IGNORE_FILES = ['.ipynb_checkpoints']   # Prevent parsing checkpoints files

# plugins configuration
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb2pelican', 'i18n_subsites',]#'tipue_search',]


JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}






