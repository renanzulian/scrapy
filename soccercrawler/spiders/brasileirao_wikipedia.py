# -*- coding: utf-8 -*-
import scrapy
import re


class BrasileiraoWikipediaSpider(scrapy.Spider):
    name = 'brasileirao-wikipedia'
    allowed_domains = ['https://en.wikipedia.org/wiki/Campeonato_Brasileiro_S%C3%A9rie_A']
    start_urls = ['https://en.wikipedia.org/wiki/Campeonato_Brasileiro_S%C3%A9rie_A']

    def parse(self, response):
        clubs = response.xpath('//table[2]/tbody/tr/td[1]/a/text()').getall()
        wins = response.xpath('//table[2]/tbody/tr/td[2]/text()').getall()
        self.club_ranking_generator(clubs, wins)

    def club_ranking_generator(self, clubs: list, wins: list)-> dict:
        wins_formatted = self.wins_formatter(wins)
        print(clubs, wins_formatted)

    def wins_formatter(self, wins: list)-> list:
        result = map(lambda value: int(value.replace('\n', '')), wins)
        return [r for r in result]