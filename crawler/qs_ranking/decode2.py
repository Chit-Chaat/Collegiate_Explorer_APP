__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '10/6/2020 11:56 AM'

import json


def export_2_file(file_path, data):
    with open(file_path, 'wb+') as output_file:
        encoded_item = json.dumps([dict(item) for item in data], ensure_ascii=False, indent=4)
        output_file.write(encoded_item.encode('utf-8'))


if __name__ == '__main__':
    processed_data = []
    with open("./output/945030.txt", 'r', encoding='utf-8') as input_file:
        data = json.load(input_file)
        for item in data['data']:
            del item['guide']
            del item['stars']
            del item['core_id']
            item['logo'] = item['logo'].split('"')[1]
            item['url'] = "https://www.topuniversities.com" + item['url']
            processed_data.append(item)

    export_2_file('./output/qs_ranking_us_2021.jl', processed_data)
