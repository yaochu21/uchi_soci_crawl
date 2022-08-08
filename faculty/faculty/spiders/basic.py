from gc import callbacks
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import FacultyItem
import re
import logging

class BasicSpider(CrawlSpider):
    name = 'basic'
    allowed_domains = ['anthropology.uchicago.edu']
    start_urls = ['https://anthropology.uchicago.edu/people/faculty']

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
        names = response.xpath('//h3/a/text()').getall()
        descriptions = response.xpath('//p/text()').getall()[:-6]
        descriptions.pop(6)
        emails = [a[7:] for a in response.css('a[href^="mailto"]::attr(href)').getall()]
        emails.pop(9)

        self.log(len(names))

        assert(len(names) == len(descriptions) == len(emails))
        for i in range(len(names)):
            new_item = FacultyItem()
            new_item['name'] = names[i]
            new_item['email'] = emails[i]
            description = descriptions[i]

            match = re.compile(r'\((.*?)\) (.*)')
            partition = re.search(match,description)
            titles = partition.group(1)
            fields = partition.group(2).split(' (')[0]

            new_item['education'] = titles.split(';')[0]
            new_item['position'] = titles.split(';')[1].lstrip(' ')
            new_item['geo_areas'] = fields.split('; ')[-1]
            new_item['interests'] = fields.split('; ')[:-1]
            yield new_item


            

            




