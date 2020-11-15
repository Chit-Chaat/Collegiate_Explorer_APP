__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '11/12/2020 10:37 PM'

import csv
import json
import os
import random
import sys
import time

import requests
from playsound import playsound


def read_file(filepath):
    with open(filepath, encoding='utf-8') as file:
        data = json.load(file)
        return data


def save2file(data, filepath):
    with open(filepath, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


if __name__ == '__main__':

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "cache-control": "no-cache",
        "cookie": "_pxhd=794e5c10cba82c4f94beb4347d0b7267c489fbc9ea10bd57334ec95dd9993eed:bfb921a0-fd30-11ea-814b-09b35b66eb70; xid=8045f931-5687-48dc-bfd8-7db56d2d972f; experiments=%5E%5E%5E%24%5D; _gcl_au=1.1.1577562867.1600819642; _ga=GA1.2.1705852934.1600819642; _scid=ac21cde9-09bb-48a0-a633-6b4716d8ec0b; _fbp=fb.1.1600819642332.813683261; _pxvid=bfb921a0-fd30-11ea-814b-09b35b66eb70; ab.storage.deviceId.97a5be8e-e2ba-4f2c-9159-9ae910fa9648=%7B%22g%22%3A%22bafdefc4-5bcc-1d82-af0c-e69cfb675c1f%22%2C%22c%22%3A1600909650194%2C%22l%22%3A1600909650194%7D; __gads=ID=6630f51febcfb35e:T=1600909684:S=ALNI_MZBdYt7hjlnxKMruRcfTzci1nkKKg; _mkto_trk=id:829-OCU-633&token:_mch-niche.com-1602795847605-36805; niche_cookieConsent=true; _gid=GA1.2.907923889.1605143878; _sctr=1|1605081600000; hintSeenLately=true; recentlyViewed=entityHistory%7CentityName%7CAdams%2BState%2BUniversity%7CentityGuid%7C8bd4768e-4754-4147-8409-c518304ee7f2%7CentityType%7CCollege%7CentityFragment%7Cadams-state-university%7CRabbinical%2BSeminary%2Bof%2BAmerica%7C41db57ee-6938-4b0b-af38-fc64694bbb03%7Crabbinical-seminary-of-america%7CCitadel%2BMilitary%2BCollege%2Bof%2BSouth%2BCarolina%7Cb84a0ba2-fc8a-4859-80af-597026d8d1f1%7Ccitadel-military-college-of-south-carolina%7CClark%2BCollege%7C2e606e66-ed58-4e31-91a9-59a84cc7cb39%7Cclark-college%7CsearchHistory%7CColorado%7C128115b8-13f9-4e43-a016-915da57b0729%7CState%7Ccolorado%7CNew%2BYork%7C820bdb36-718f-42a2-a471-5e2aa98007da%7Cnew-york%7CSouth%2BCarolina%7C4e14b3cc-29b7-46c8-b531-601bf3625739%7Csouth-carolina%5E%5E%5E%240%7C%40%241%7C2%7C3%7C4%7C5%7C6%7C7%7C8%5D%7C%241%7C9%7C3%7CA%7C5%7C6%7C7%7CB%5D%7C%241%7CC%7C3%7CD%7C5%7C6%7C7%7CE%5D%7C%241%7CF%7C3%7CG%7C5%7C6%7C7%7CH%5D%5D%7CI%7C%40%241%7CJ%7C3%7CK%7C5%7CL%7C7%7CM%5D%7C%241%7CN%7C3%7CO%7C5%7CL%7C7%7CP%5D%7C%241%7CQ%7C3%7CR%7C5%7CL%7C7%7CS%5D%5D%5D; ab.storage.sessionId.97a5be8e-e2ba-4f2c-9159-9ae910fa9648=%7B%22g%22%3A%22b4563857-20b3-f689-f9f5-e4dad8093602%22%2C%22e%22%3A1605255209766%2C%22c%22%3A1605247426776%2C%22l%22%3A1605253409766%7D; _uetsid=e621d510248411ebb5b93d4f02c21d9d; _uetvid=d7ae27746348ac0082dec693b56d70f3; pageViews=132; _pxff_rf=1; _pxff_fp=1; _px3=b8c0283ab1c121a12679270ea7626095492c9841400c6f6db0a2147c85a177ea:zKmrp7dhxg6sMPUsw9eV2O1C5j4IaENjzn+9b5ZwW0hCFOnwE3VFvIALU8B6fU4AxelQprZmUxXyZExARMOEsw==:1000:SOeU9LuMm4hY7MeDGweSxc3TrwcEzhIbCebw86KZQu4IXUaCJSE8TiJCtjE9svh1Iwds7D+8TD02jXZtty+lRZdxQS+RANVf1e20812hz+gq8grYG+YOYwWJkS9CQQ6kwaq0ofmrmzABk+idAn3XRfZ45OENHlsc31mA3ZKHUqQ=",
        "origin": "https://www.niche.com/",
        "pragma": "no-cache",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-site": "none",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    bundle_info = read_file("../data/true_urls.json")
    have_crawled = len(os.listdir("../reviews/text"))
    all_niche_list = list(bundle_info.values())[have_crawled:]
    for idx, two_id in enumerate(all_niche_list):
        ce_id = two_id[0]
        niche_id = two_id[1]
        textual_result = []
        numerical_result = []
        if niche_id != "":
            temp_rating = None
            for rating in [5, 4, 2, 1]:
                total = 100
                for page in [1, 2, 3]:
                    if page * 20 <= total:
                        url = "https://www.niche.com/api/entity-reviews/?e={}&rating={}&page={}&limit=20".format(
                            niche_id, rating, page)
                        try:
                            response = requests.get(url, headers=headers)
                            if response.status_code == 200:
                                response = json.loads(response.text)

                                # extract # info
                                if rating != temp_rating:
                                    total = response['total']
                                    numerical_result.append([rating, total])
                                    temp_rating = rating

                                # extract textual info
                                reviews = response['reviews']
                                textual_result.extend(
                                    list(map(lambda item: [item['author'], item['rating'], item['body']], reviews)))

                                # stop for a while
                                time.sleep(round(random.uniform(1, 5), 3))
                            else:
                                print("when crawling the {}th school review-> {}, httpcode -> ".format(idx,
                                    response.status_code))
                                # play sound to notify developer to click "I m not a robot"
                                for _ in range(3):
                                    playsound('./busy.mp3')
                                    time.sleep(1)
                                # open browser automatically
                                os.system(
                                    '"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe" https://www.niche.com/api/entity-reviews/?e=e73c0c6b-7b57-4725-ab1b-8f57eaf16faa&rating=5&page=3&limit=10')

                                time.sleep(20)

                        except:
                            print(
                                "when crawling the {}th school review-> {}, something bad happened".format(idx, ce_id))
                            for _ in range(3):
                                playsound('./error.mp3')
                                time.sleep(1)
                            sys.exit(0)

        print("finish {} th school -> {}".format(idx, ce_id))
        save2file(textual_result, "../reviews/text/{}_text.csv".format(ce_id))
        save2file(numerical_result, "../reviews/num/{}_num.csv".format(ce_id))
