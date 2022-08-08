# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FacultyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    name = scrapy.Field()
    position = scrapy.Field()
    education = scrapy.Field()
    email = scrapy.Field()
    geo_areas = scrapy.Field()
    interests = scrapy.Field()
