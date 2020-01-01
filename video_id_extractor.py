#!/usr/bin/env python
# -*- coding:utf-8 -*-
# extract YouTube videoids from html
import re
import urllib.request as urllib2
from bs4 import BeautifulSoup


def get_videoids(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, features="html.parser")
    videoids = []
    for element in soup('embed'):
        src = element.get('src')
        if re.search(r'v\/([-\w]+)', src):
            videoids.append(re.search(r'v\/([-\w]+)', src).group(1))
    for element in soup('iframe'):
        src = element.get('src')
        if re.search(r'youtube.com\/embed\/', src):
            videoids.append(re.search(r'embed\/([-\w]+)', src).group(1))
    for element in soup('iframe'):
        src = element.get('src')
        if re.search(r'youtube.com\/embed\/', src):
            videoids.append(re.search(r'embed\/([-\w]+)', src).group(1))
    for element in soup('a'):
        href = element.get('href')
        if href and re.search(r'watch\?v=([-\w]+)', href):
            videoids.append(re.search(r'watch\?v=([-\w]+)', href).group(1))
        if href and re.search(r'youtu\.be\/([-\w]+)', href):
            videoids.append(re.search(r'youtu\.be\/([-\w]+)', href).group(1))

    res = {}
    res['videoids'] = list(set(videoids))
    return res
