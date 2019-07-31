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
               ]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/favicon.ico': {'path': 'favicon.ico'},
                       'extra/robots.txt': {'path': 'robots.txt'},
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
            "cjk-auto-spacing",
            "related_posts",
            "photos",
            "liquid_tags.video",
            "liquid_tags.gram",
            "liquid_tags.youtube",
            "i18n_subsites",
            "pelican-gist",
            "pelican-cover-image"
          ]


THEME = "themes/pelican-bootstrap3/"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
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


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
        )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/gfrog'),
         )

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
