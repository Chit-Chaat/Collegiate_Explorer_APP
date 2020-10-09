# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class QsCrawlerPipeline:
    def __init__(self):
        self.result_file_name = "qs_ranking_world_2021.jl"
        self.result_file = open(self.result_file_name, 'wb')

    def process_item(self, item, spider):
        data = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.result_file.write(data.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.result_file.close()
