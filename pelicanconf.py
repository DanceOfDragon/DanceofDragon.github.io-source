#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'JIN Lin'
SITENAME = u'JIN Lin | Oh,Interesting'
SITESUBTITLE = u'What I Cannot Create I Do Not Understand.'

SITEURL = 'http://linnus.net'

TIMEZONE = 'Singapore'

DEFAULT_LANG = u'en'

TYPOGRIFY = True

# Related to comment disqus
# RELATIVE_URLS = True

DEFAULT_PAGINATION = 7

#URL settings

#DIRECT_TEMPLATES = ['index','archives','categories','tags']

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%m}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'

#PAGE_URL = 'pages/{slug}/'
#PAGE_SAVE_AS = 'pages/{slug}/index.html'

ABOUT_PAGE = '/pages/about.html'

#THEME
THEME = 'themes/theme-jakevdp'

STATIC_PATHS = ['images','pages', 'pdfs','favicon.ico','extra/CNAME']

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

#plug-ins

PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = ['render_math','sitemap', 'liquid_tags.img','better_codeblock_line_numbering','liquid_tags.youtube','liquid_tags.img','ipynb.liquid','clean_summary']

MARKUP = ('md', 'ipynb')

#sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5,
    },
    "changefreqs": {
        "articles": "daily",
        "indexes": "daily",
        "pages": "monthly",
    }
}

# for liquid tags
# CODE_DIR = 'downloads/code'
# NOTEBOOK_DIR = 'downloads/notebooks'

#related posts
#RELATED_POSTS_MAX = 5

# About Page

ABOUT_PAGE = '/pages/about.html'
#TWITTER_USERNAME = 'XL62812072'
GITHUB_USERNAME = 'DanceOfDragon'
AUTHOR_WEBSITE = 'http://linnus.com'
AUTHOR_CV = "/pdfs/JIN Lin_CV_2017"


#Achives

SHOW_ARCHIVES = True

ENABLE_MATHJAX = True

#clean summary 
CLEAN_SUMMARY_MAXIMUM = 0

#CLEAN_SUMMARY_MINIMUM_ONE = False


#md-highlight
#MD_EXTENSIONS = ['codehilite(css_class=highlight,linenums=False)','extra', 'toc(permalink=true)']

DISQUS_SITENAME = 'linnus'

GOOGLE_ANALYTICS = 'UA-64765479-1'
#ignore files 
IGNORE_FILES = ['.DS_Store', '.DS_store']





