import requests as requests
import scrapy
import json
import requests

from bs4 import BeautifulSoup

from ..items import LibusItem


def get_content_html(text):
    return BeautifulSoup(text, 'lxml')


class CatalogSpider(scrapy.Spider):
    name = 'catalog'
    # allowed_domains = ['en.1lib.pl']
    # start_urls = ['https://en.1lib.pl/category-list']
    # start_urls = ['https://en.1lib.pl']
    # start_urls = ['https://en.1lib.pl/book/2696469/e34ae5']
    start_urls = ['https://1lib.us']

    # proxy = '140.227.25.56:5678'

    def start_requests(self):
        for pages in json.load(open('/home/alxgav/projects/book/libus/n.json', 'r')):
            print(pages["sub_categ_url"],
                  '=========================================================================================')
            for i in range(1, 11):
                url = f'{pages["sub_categ_url"]}?page={i}'
                request = scrapy.Request(url, callback=self.parse_pages)
                # request.meta['proxy'] = self.proxy
                yield request
            # break

    def parse_pages(self, response):
        for href in response.css('h3[itemprop="name"] a::attr("href")').extract():
            url = response.urljoin(href)
            # print(url, '===============url')
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        items = LibusItem()
        try:
            items['title'] = response.css('h1[itemprop="name"]::text').extract_first('').strip()
        except:
            items['title'] = ''
        try:
            items['url'] = response.request.url
        except:
            items['url'] = ''
        id_book = response.request.url.split('/')[-2]
        try:
            items['url_cover'] = response.css('.z-book-cover img::attr("src")').extract_first()
        except:
            items['url_cover'] = ''
        try:
            items['author'] = response.css('a[itemprop="author"]::text').extract()
        except:
            items['author'] = ''
        try:
            items['rating'] = response.css('.book-rating-interest-score::text').extract_first('').strip()
        except:
            items['rating'] = ''
        try:
            items['description'] = get_content_html(response.xpath('//*[@id="bookDescriptionBox"]').get()).select_one(
                '#bookDescriptionBox').text.strip()
        except:
            items['description'] = ''
        # for d in response.css('.bookProperty'):
        #     try:
        #         if d.css('.property_label::text').extract_first('').stip() == 'Categories:':
        #             items['categories'] = d.css('.property_value::text').extract_first('').stip()
        #     except:
        #         items['categories'] = ''
        try:

            soup = get_content_html(response.css('.bookDetailsBox').get())
            for i in soup.select('.bookProperty'):
                try:
                    if i.select_one('.property_label').text.strip() == 'Categories:':
                        items['categories'] = i.select_one('.property_value').text.strip()
                except:
                    items['categories'] = ''
                try:
                    if i.select_one('.property_label').text.strip() == 'Edition:':
                        items['edition'] = i.select_one('.property_value').text.strip()
                except:
                    items['edition'] = ''
                try:
                    if i.select_one('.property_label').text.strip() == 'Language:':
                        items['language'] = i.select_one('.property_value').text.strip()
                except:
                    items['language'] = ''
                try:
                    if i.select_one('.property_label').text.strip() == 'ISBN 10:':
                        items['ISBN10'] = i.select_one('.property_value').text.strip()
                except:
                    items['ISBN10'] = ''
                try:
                    if i.select_one('.property_label').text.strip() == 'File:':
                        items['file'] = i.select_one('.property_value').text.strip()
                except:
                    items['file'] = ''
                try:
                    if i.select_one('.property_label').text.strip() == 'Year:':
                        items['year'] = i.select_one('.property_value').text.strip()
                except:
                    items['year'] = ''
                try:
                    if i.select_one('.property_label').text.strip() == 'Publisher:':
                        items['publisher'] = i.select_one('.property_value').text.strip()
                except:
                    items['publisher'] = ''
                try:
                    if i.select_one('.property_label').text.strip() == 'Pages:':
                        items['pages'] = i.select_one('.property_value').text.strip()
                except:
                    items['pages'] = ''
                try:
                    if i.select_one('.property_label').text.strip() == 'ISBN 13:':
                        items['ISBN13'] = i.select_one('.property_value').text.strip()
                except:
                    items['ISBN13'] = ''
        except:
            pass
        # items['preview'] = response.css('pre::text').extract_first('').strip()
        try:
            items['preview_link'] = response.urljoin(response.css('a.btn-default::attr("href")').get())
        except:
            items['preview_link'] = ''
        # print (response.xpath('.addDownloadedBook::attr("href"').extract(), '=====================')
        try:
            items['download_link'] = response.urljoin(response.css('a.btn.addDownloadedBook::attr("href")').get())
        except:
            items['download_link'] = ''
        if items['title'] != '':
            yield items
