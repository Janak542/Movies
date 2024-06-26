# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movies_image_link = scrapy.Field()
    movies_name = scrapy.Field()
    movies_link_for_download = scrapy.Field()

