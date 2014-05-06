#! /usr/bin/env python

"""
Just random stuff I'm using for debugging.
"""

import parse

def foo(pt):
    for item in pt.iter('item'):
        link, desc, guid = item.find('link'), item.find('description'), item.find('guid')
        if link is not None:
            print "Link:", link.text
        if desc is not None:
            print "Description:", desc.text
        if guid is not None:
            print "GUID:", guid.text
            
        print


def test(url):
    print 'TESTING', url
    print '=' * 80
    pt = parse.tree_from_url(url)
    print parse.header_data(pt)
    print
    for elem in parse.items(pt):
        pprint_dict(elem)
    print

def test2(feed_url):
    pt = parse.tree_from_url(feed_url)
    print parse.header_data(pt)


def pprint_dict(d):
    for key, value in sorted(d.items()):
        print key, ':',  value
    print

def main():
    # test('http://cyber.law.harvard.edu/rss/examples/rss2sample.xml')
    # test('http://www.feedforall.com/sample.xml')
    # test('http://www.feedforall.com/sample-feed.xml')
    test2('http://www.feedforall.com/blog-feed.xml')

if __name__ == '__main__':
    main()
    
