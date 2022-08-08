# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FacultyPipeline:
    def process_item(self, item, spider):
        # line = json.dumps(dict(item)) + '\n'  # Json Lines format allows us to write multiple json 'structs' to a single file
        #                                       # as multiple lines
        #                                       # Note that since json.dumps returns a string we can add an newline to it
        # self.file.write(line)
        return item
