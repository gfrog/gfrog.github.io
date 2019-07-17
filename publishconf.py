#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://www.gfrog.net'
ABSOLUTE_URL = SITEURL
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

GMAPS_API_KEY = "AIzaSyB63YDb3SVNe84KeNXPh5zIjJ_uwr5vsII"

DELETE_OUTPUT_DIRECTORY = True

IGNORE_FILES = ['.#*', '*drafts*']

# Following items are often useful when publishing

DISQUS_SITENAME = "gfrog"
#GOOGLE_ANALYTICS = ""
