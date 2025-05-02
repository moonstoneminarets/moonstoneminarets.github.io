### Dev and prod config ###

AUTHOR = ''
SITENAME = 'Moonstone Minarets'
SITEURL = 'localhost:8000'

PATH = 'content'

TIMEZONE = 'Canada/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Mailing List', 'pages/mailing-list.html'),
    ("Ashiq Alibhai, Author", "https://www.ashiqalibhai.com"),)

# Social widget
SOCIAL = ()# (('You can add links in your config file', '#'),
           #('Another social link', '#'),)

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