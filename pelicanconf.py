#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lkk Team'
SITENAME = 'Lkk Team Blog'
SITEURL = 'http://lekongkong.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('乐空空', 'http://www.lekongong.com/'),
         ('百姓网', 'http:www.baixing.comm'),
         ('Github', 'https://github.com/LeKongKong/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME='Flex'

SITETITLE = 'Lkk Team'
SITESUBTITLE = 'make world better~~'
SITEDESCRIPTION = 'Lkk Team members Thoughts and Writings'
SITELOGO = 'http://s.baixing.net/lkk/favicon.png'
BROWSER_COLOR = '#333'

FAVICON = 'http://s.baixing.net/lkk/favicon.png'
ROBOTS = 'index, follow'

COPYRIGHT_YEAR = 2018
CC_LICENSE = { 'name': 'Creative Commons Attribution-ShareAlike', 'version':'4.0', 'slug': 'by-sa' }

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
#CUSTOM_CSS = 'static/custom.css'

MAIN_MENU = True
