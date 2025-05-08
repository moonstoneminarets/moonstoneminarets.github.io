import datetime

AUTHOR = ''
SITENAME = 'Moonstone Minarets'
SITEURL = 'localhost:8000'

PATH = 'content'

TIMEZONE = 'Canada/Eastern'

THEME = 'themes/flex'

DEFAULT_LANG = 'en'

STATIC_PATHS = ['images']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()
    
DEFAULT_PAGINATION = True

THEME = 'themes/flex'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Buncha links. They appear BEFORE the pages list in the sidebar. See: sidebar.html
LINKS = (
    ('Home', '/'), # trailing comma marks it as a list? of tuples
)

# How many words to show before "Continue Reading"
SUMMARY_MAX_LENGTH = None
SUMMARY_MAX_PARAGRAPHS = None

COPYRIGHT_YEAR = datetime.datetime.now().year