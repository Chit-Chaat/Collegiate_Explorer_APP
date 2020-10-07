__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '10/6/2020 11:15 AM'

import json


import requests
import datetime


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
url = "https://www.topuniversities.com/sites/default/files/qs-rankings-data/946820.txt"

ranking = requests.get(url=url + "?_=" + gen_current_timestamp(),
                       headers=headers)

print(ranking.text)
# actually all data are encrypted
