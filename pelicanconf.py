#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ken Mwanza'
SITENAME = 'Ken Mwanza'
SITEURL = 'http://127.0.0.1:8000'

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['sitemap', 'bootstrapify']
BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover']
}

PATH = 'content'

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}

GOOGLE_ANALYTICS = 'UA-188337095-1'

TIMEZONE = 'America/Toronto'

SITESUBTITLE = 'Random Thoughts'

PYGMENTS_STYLE = 'colorful'

DESCRIPTION = "Random Thoughts"

HIDE_AUTHORS = True

THEME_CSS_OVERRIDES = ['theme/css/oldstyle.css']

DEFAULT_LANG = 'en'

#LINKS = True
ICONS = (
    ('github', 'https://github.com/KenMwanza'),
    ('linkedin', 'https://www.linkedin.com/in/ken-mwanza/')
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'alchemy'