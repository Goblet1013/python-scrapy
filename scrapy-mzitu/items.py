# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class seriesItem(scrapy.Item):
    # define the fields for your item here like:
    series_urls = scrapy.Field()#套图链接
    img_url = scrapy.Field()#图片链接
    pass
