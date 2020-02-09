# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin

class ImdbTopSpider(scrapy.Spider):
    name = 'imdb_top'
    allowed_domains = ['imdb.com']
    start_urls = ['http://imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv/']

    def parse(self, response):
        urls = response.xpath('//td[@class="titleColumn"]/a/@href').extract()
        abs_urls = [urljoin('http://imdb.com',url) for url in urls]
        for abs_url in abs_urls:
            yield scrapy.Request(url =abs_url, callback = self.parse_show)
    def parse_show(self, response):
        show_name = response.xpath('//div[@class="title_wrapper" ]/h1/text()').extract_first()
        genres_and_year = response.xpath('//div[@class ="subtext"]/a/text()').extract()	
        yield {
            'name': show_name,
            'genre': genres_and_year[:-1],
			'year': genres_and_year[-1]
		}