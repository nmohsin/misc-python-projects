import re

from BeautifulSoup import BeautifulSoup

def strip_markup(markup):
    return re.sub(r'(<!--.*?-->|<[^>]*>)', '', markup)

def is_url(text):
    return re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                    text)

def shorten(text, size):
    if len(text) <= size:
        return text
    return text[ : size] + "..."
