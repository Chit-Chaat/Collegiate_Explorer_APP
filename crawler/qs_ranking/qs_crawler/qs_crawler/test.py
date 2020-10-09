__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '10/8/2020 7:56 PM'

import json

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as input_file:
        return json.load(input_file)


result = read_json_file("../../output/qs_ranking_world_2021.jl")

raw_infos = dict()
for item in result:
    raw_infos[item['url'].split('/')[-1]] = item

print(raw_infos)
