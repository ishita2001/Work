# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from  web.models import Product

class Scraped_Item(DjangoItem):

    # define the fields for your item here like:
    print("!!!!!!!!!")
    django_model = Product
    #  name = scrapy.Field()
    #  price = scrapy.Field()
    #  link = scrapy.Field()