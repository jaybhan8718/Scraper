# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HectorProjectItem(scrapy.Item):
    Title = scrapy.Field()
    Percentage = scrapy.Field()
