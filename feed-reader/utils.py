import re

from BeautifulSoup import BeautifulSoup

def strip_html(html):
    soup = BeautifulSoup('<html>' + html + '</html>')
    return soup.get_text()


def is_url(text):
    return re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                    text)
