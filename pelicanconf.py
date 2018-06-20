#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# # Fix for ipynb plugin https://github.com/danielfrg/pelican-ipynb/issues/49
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")


AUTHOR = 'Gaurav Modi'
SITENAME = "Gaurav Modi"
SITEURL = ''
SITEDESCRIPTION = "Data Analysis and Machine Learning Blog"
OPEN_GRAPH_IMAGE = 'images/gauravmodi.jpg'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

GITHUB_URL = 'https://github.com/gauravmodi'

PATH = 'content'

DISPLAY_ARTICLE_INFO_ON_INDEX = False
DISPLAY_ARTICLE_SUMMARY_ON_INDEX = False

# Category Settings and Menu items
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
#    ('About', ''),
    # ('Contact', 'https://docs.google.com/forms/d/e/1FAIpQLSd_67Y_w4mvfDw3KQQEJJygHSumOYqH-eiByDI-xUStsw0T1Q/viewform?usp=sf_link'),
    ('RESUME', 'https://z.umn.edu/gaurav_resume'),
    ('LinkedIn', 'https://www.linkedin.com/in/modigaurav01/'),
    ('GitHub', 'https://github.com/gauravmodi/')
)

# Retain .git files while publishing
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".hg", ".git", ".bzr", "CNAME", "README.md"]

# URL settings
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{category}/{slug}/'
PAGE_SAVE_AS = '{category}/{slug}/index.html'

#Default Date format 21 Jan 2018
DEFAULT_DATE_FORMAT = '%d %b %Y'

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

STATIC_PATHS = [
  'images',
  'data',
  'extra'
]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Style
TYPOGRIFY = True
# themes configuration
THEME = "themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'united'
PYGMENTS_STYLE = 'default'
AUTHOR = 'Gaurav Modi'
# FAVICON = 'favicon.ico'
HIDE_SIDEBAR = True
CUSTOM_CSS = 'static/css/custom.css'

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    # input_path : output_path
    'extra/custom.css': {'path': 'static/css/custom.css'},
    # 'extra/custom.js': {'path': 'static/js/custom.js'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# ipynb configuration
MARKUP = ('md', 'ipynb', )
IGNORE_FILES = ['.ipynb_checkpoints']   # Prevent parsing checkpoints files

#Markdown Extensions
MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra']

# plugins configuration
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb2pelican', 'i18n_subsites',]#'tipue_search',]


JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
