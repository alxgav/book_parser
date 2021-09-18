# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LibusItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    category = scrapy.Field()
    sub_categ = scrapy.Field()
    sub_categ_url = scrapy.Field()
    book_url = scrapy.Field()
    url = scrapy.Field()
    gen_url = scrapy.Field()
    title = scrapy.Field()
    url_cover = scrapy.Field()
    author = scrapy.Field()
    rating = scrapy.Field()
    description = scrapy.Field()
    categories = scrapy.Field()
    edition = scrapy.Field()
    language = scrapy.Field()
    ISBN10 = scrapy.Field()
    file = scrapy.Field()
    year = scrapy.Field()
    publisher = scrapy.Field()
    pages = scrapy.Field()
    ISBN13 = scrapy.Field()
    preview = scrapy.Field()
    preview_link = scrapy.Field()
    download_link = scrapy.Field()
    id_book = scrapy.Field()
    pass
