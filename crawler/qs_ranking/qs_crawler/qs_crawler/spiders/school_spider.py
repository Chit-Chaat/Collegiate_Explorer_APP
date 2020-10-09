import datetime

import scrapy
from ..items import QsCrawlerItem
import json


def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as input_file:
        return json.load(input_file)


def gen_current_timestamp():
    current_timestamp = str(datetime.datetime.now().timestamp()).split(".")
    current_timestamp_str = ''.join(current_timestamp)[:-3]
    return current_timestamp_str


headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "cache-control": "no-cache",
    "cookie": "__cfduid=de35ecc27c5967b11534be4705f663dc31600910359;"
              " zabUserId=1600910362328zabu0.4824852002565372;"
              " _ga=GA1.2.45828874.1600910362;"
              " STYXKEY_first_visit=yes;"
              " __gads=ID=b21c474b5e86c1f6:T=1600910362:S=ALNI_Ma90NlVVtwzv035DnSQd9NY9MjtYQ;"
              " _fbp=fb.1.1600910365255.1074073799;"
              " _mkto_trk=id:335-VIN-535&token:""_mch-topuniversities.com-1600910365652-13252;"
              " _hjid=b7c7af82-1323-4fa7-8438-c26f431ef67e;"
              " hubspotutk=c428a342d5aadd2a574b7856cae7f5ca;"
              " messagesUtk=5346d84eeb96482282f2fa9ec10b787a;"
              " _gid=GA1.2.1385675015.1601947909; cookie-agreed=2;"
              " home-search-bar=1;"
              " has_js=1;"
              " __hstc=238059679.c428a342d5aadd2a574b7856cae7f5ca.1600910366050.1601960075729.1602008151784.5;"
              " __hssrc=1;"
              " _hjIncludedInPageviewSample=1;"
              " _hjTLDTest=1;"
              " _hjAbsoluteSessionInProgress=0;"
              " Hm_lvt_d4f650e8b28d910a41791663c4ef9cb3=1600910365,1601947911,1602008153,1602008192;"
              " _gat=1;"
              " __hssc=238059679.8.1602008151784;"
              " _gat_UA-37767707-2=1;"
              " Hm_lpvt_d4f650e8b28d910a41791663c4ef9cb3={}".format(gen_current_timestamp()),

    "pragma": "no-cache",
    "referer": "https://www.topuniversities.com/university-rankings/world-university-rankings/2021",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "x-newrelic-id": "UwUCVVVTGwIAV1VXBQkP",
    "x-requested-with": "XMLHttpRequest"
}


def preprocess(dict_list):
    result = dict()
    for item in dict_list:
        result[item['url'].split('/')[-1]] = item
    return result


class SchoolSpiderSpider(scrapy.Spider):
    name = 'school_spider'
    allowed_domains = ['www.topuniversities.com/universities/']
    start_urls = ['https://www.topuniversities.com/university-rankings/world-university-rankings/2021']
    raw_data = read_json_file("../output/qs_ranking_world_2021.jl")

    info_dict = preprocess(raw_data)

    def request(self, url, meta, callback):
        request = scrapy.Request(url=url, meta=meta, callback=callback, headers=headers)
        return request

    def parse(self, response):
        urls = response.xpath("//table[@id='qs-rankings']//tbody//tr//td[2]//div//a[2]/@href")
        for url in urls:
            bundle_info = response.xpath(
                "//div[@class='container']//div[@class='key pull-left']//div[@class='val']/text()")
            yield self.request(url=url,
                               meta={'url': url,
                                     'bundle': bundle_info},
                               callback=self.parse_school)

    def parse_school(self, response):
        global info_dict
        school_item = QsCrawlerItem()
        url = response.meta['url']
        school_item['url'] = url
        school_item['id'] = info_dict[url]['nid']
        school_item['title'] = info_dict[url]['title']
        school_item['qs_score'] = info_dict[url]['score']
        school_item['ranking'] = info_dict[url]['rank_display']
        school_item['country'] = info_dict[url]['country']
        school_item['region'] = info_dict[url]['region']
        # bundle_infos = response.meta['bundle'].split(' ')
        # school_item['type'] = bundle_infos[1]
        # school_item['research_ability'] = bundle_infos[2]
        # school_item['num_of_total_student'] = bundle_infos[3]
        # school_item['academic_stuff'] = int(''.join(bundle_infos[4].split(',')))
        # school_item['num_of_international_student'] = int(''.join(bundle_infos[5].split(',')))
        yield school_item
