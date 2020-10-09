# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QsCrawlerItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    qs_score = scrapy.Field()
    ranking = scrapy.Field()
    country = scrapy.Field()
    region = scrapy.Field()
    type = scrapy.Field()
    research_ability = scrapy.Field()
    num_of_total_student = scrapy.Field()
    academic_stuff = scrapy.Field()
    num_of_international_student = scrapy.Field()
