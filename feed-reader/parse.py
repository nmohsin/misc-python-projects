#! /usr/bin/env python

"""Parsing functionality for RSS feeds."""

import requests
import xml.etree.ElementTree as ET
import utils

def tree_from_url(url):
    """Builds a parse tree for a given file.

    Args:
    url (str): A URL pointing to the file.

    Returns:
    xml.etree.ElementTree.ElementTree: The parse tree of the file at `url`.
    """
    response = requests.get(url)
    assert response.status_code == 200
    return tree_from_string(response.content)

def tree_from_string(contents):
    """Builds a parse tree from a string.

    Args:
    contents (str): A string representing an XML document.

    Returns:
    xml.etree.ElementTree.ElementTree: The parse tree of `contents`.
    """
    return ET.fromstring(contents)


def header_data(tree):
    tags = ['title', 'link', 'description']
    return [tree[0].find(tag).text for tag in tags]

def items(tree):
    return [parse_item(subtree)
            for subtree
            in tree[0].findall('item')]

def parse_item(item_tree):
    item_dict = {}

    title_subtree = item_tree.find('title')
    if title_subtree is not None:
        item_dict['title'] = title_subtree.text

    desc_subtree = item_tree.find('description')
    if desc_subtree is not None:
        item_dict['description'] = desc_subtree.text

    guid_subtree = item_tree.find('guid')
    if guid_subtree is not None:
        text = guid_subtree.text
        has_permalink_attrib = 'isPermaLink' in guid_subtree.attrib
        marked_permalink = has_permalink_attrib and guid_subtree.attrib['isPermaLink']

        if marked_permalink:
            item_dict['url'] = text
        elif not marked_permalink and utils.is_url(text):
            item_dict['url'] = text

    if 'url' not in item_dict:
        link_subtree = item_tree.find('link')
        if link_subtree is not None:
            text = link_subtree.text
            item_dict['url'] = text

    return item_dict

    

    
            
        
            

    

        







    
    


    






    
