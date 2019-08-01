#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'gfrog'
SITENAME = 'My Life, My Love!'
SITESUBTITLE = '指点江山 激昂文字 修身隆德 自然自我'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh_CN'
DEFAULT_DATE_FORMATS = '%F %T'

FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
SLUGIFY_SOURCE = 'basename'

ARTICLE_PATH = 'posts'
# @see http://docs.getpelican.com/en/3.5.0/settings.html#url-settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}.html'


STATIC_PATHS = ['extra/CNAME',
                'extra/favicon.ico',
                'extra/robots.txt',
                'js/',
               ]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/favicon.ico': {'path': 'favicon.ico'},
                       'extra/robots.txt': {'path': 'robots.txt'},
                       'js/': {'path': 'js/'},
                      }


# set all post to draft by default, set `Status: published`
# when want to publish it.
DEFAULT_METADATA = {
    'status': 'draft',
}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
            #"cjk-auto-spacing",
            "related_posts",
            "photos",
            "liquid_tags.video",
            "liquid_tags.gram",
            "liquid_tags.youtube",
            "i18n_subsites",
            "pelican-gist",
            "pelican-cover-image",
            "liquid_tags.gmap",
            "sitemap",
            "tipue_search"
          ]


THEME = "themes/pelican-bootstrap3/"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
BOOTSTRAP_THEME = 'united'
PYGMENTS_STYLE = "default"
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
SHOW_ARTICLE_CATEGORY = True
BOOTSTRAP_NAVBAR_INVERSE = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISABLE_SIDEBAR_TITLE_ICONS = True
CC_LICENSE = "CC-BY-NC-SA"

BANNER = 'https://lh3.googleusercontent.com/JqXPGYzWGHLA_TvmD0yPkMswbnBH3I6lPaslG1lYqT_Cn2QlFSPgllt0vqQoZz7p_Cz05I7i9-WX-dOwV71bwgqhOthkSJbSWRtc2fQZSuT9ukAIzsFVHMnipaZ7b_5waXJg4E3S6yQ=w1500'
BANNER_SUBTITLE = SITESUBTITLE
# BANNER_ALL_PAGES = True

GMAPS_API_KEY = ""
try:
    with open("private/gmaps_api.key", 'r') as file:
        GMAPS_API_KEY = file.readline().strip()
except FileNotFoundError:
    pass

IGNORE_FILES = ['.#*', '*posts*', '*pages*']
PAGE_PATHS= []

DIRECT_TEMPLATES = ('index', 'categories', 'tags', 'archives', 'search')

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    },
    'exclude': [
        'tag/',
        'category/'
    ]
}

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
        )

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/gfrog'),
    ('Tweets Archive', '/pages/tweets-archive.html'),
    ('Instagram Archive', '/pages/instagram-archive.html'),
         )

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
