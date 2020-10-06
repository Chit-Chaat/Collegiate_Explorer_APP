__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '10/3/2020 8:27 PM'

import json
import os
import time

import requests
import ujson

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "cache-control": "no-cache",
    "origin": "https://www.collegeconfidential.com/",
    "pragma": "no-cache",
    "referer": "https://www.collegeconfidential.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}
url = "https://schoolsearch-api.collegeconfidential.com/search/school/"


def read_raw_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as input_file:
        return [ujson.loads(line) for line in input_file if line != "\n"]


def process_raw_data(school_info):
    del school_info["unit_id"]
    del school_info["weight"]
    # TODO maybe need to do something on "degree"
    return school_info


def export_2_file(file_path, data):
    with open(file_path, 'wb+') as output_file:
        encoded_item = json.dumps(data, ensure_ascii=False, indent=4)
        output_file.write(encoded_item.encode('utf-8'))


if __name__ == '__main__':
    base_path = "../output/"
    for region in range(7, 10):
        school_json_file = "region_{}.jl".format(region)
        schools = read_raw_data(os.path.join(base_path, school_json_file))
        for school in schools:
            school_url = url + school["_id"]
            try:
                school_detail = json.loads(requests.get(school_url, headers=headers).text)["_source"]
                dir_path = os.path.join(base_path, "region_{}".format(region))
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)
                export_2_file(file_path=os.path.join(dir_path, "{}.jl".format(school["_id"])),
                              data=process_raw_data(school_detail))
                time.sleep(1)
            except:
                print("something wrong when crawl this url -> ", school_url)
