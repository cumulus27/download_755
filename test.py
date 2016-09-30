#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test function
"""

import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import time
import datetime

from scrape_755 import Crawl
from scrape_755 import Download_url


if __name__ == '__main__':
    day_limit=7
    namelist=['hori-miona','tashima-meru']
    for name_id in namelist:
        print('Downloading {}\'s pictures and movies now...'.format(name_id))
        my_crawl=Crawl(name_id,day_limit)
        [image_url,video_url]=my_crawl.get_url()
        if len(image_url)>0:
            image_dl=Download_url(name_id,image_url,'image')
            image_dl.download()
        if len(video_url)>0:
            video_dl=Download_url(name_id,video_url,'video')
            video_dl.download()
        print('Download {} photos and {} video from {}.'.format(len(image_url),len(video_url),name_id))
