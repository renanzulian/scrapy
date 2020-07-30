# -*- coding: utf-8 -*-
import scrapy


class BrasileiraoWikipediaSpider(scrapy.Spider):
    name = 'brasileirao-wikipedia'
    allowed_domains = ['https://en.wikipedia.org/wiki/Campeonato_Brasileiro_S%C3%A9rie_A']
    start_urls = ['http://https://en.wikipedia.org/wiki/Campeonato_Brasileiro_S%C3%A9rie_A/']

    def parse(self, response):
        pass
