from gc import callbacks
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import FacultyItem
import re
import logging

class SociSpider(CrawlSpider):
    name = 'soci'
    allowed_domains = ['sociology.uchicago.edu']
    start_urls = ['https://sociology.uchicago.edu/directories/full/sociology-faculty']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_faculty', follow=True),
    # )

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    # def parse(self,response):
    #     logger = logging.getLogger()
    #     logger.info("HERE")
    #     with open("savefile", 'wb') as f:
    #         f.write(response.body)
    #     self.log(f'Saved file {"savefile"}')

    def parse(self, response):
        classes = response.xpath('//div[@class="directory-entry"]')

        for i in range(len(classes)):
            item = FacultyItem()
            p = classes[i]
            item['name'] = p.xpath('.//h2/a/text()').get()
            item['position'] = p.xpath('.//p[@class="title"]/text()').get().rstrip(' \n').lstrip(' \n')
            item['email'] = p.xpath('.//p[@class="email"]/a/text()').get()
            interests_match = re.compile(r'Interests:(.*)</p>')
            item['interests'] = re.search(interests_match,p.get()).group(1).replace(u'\xa0', u' ').lstrip(' ').rstrip(' .').split(', ')
            item['geo_areas'] = ""
            yield item


            

            




