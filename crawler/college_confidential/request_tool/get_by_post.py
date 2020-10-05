__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '10/3/2020 5:27 PM'

import json
import time
import random

import requests

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "cache-control": "no-cache",
    "content-length": "5560",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.collegeconfidential.com/",
    "pragma": "no-cache",
    "referer": "https://www.collegeconfidential.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}
url = "https://schoolsearch-api.collegeconfidential.com/searchkit/_search"
payload = {"post_filter": {"term": {"region": "2"}}, "aggs": {
    "majors.degrees.title.keyword4": {"filter": {"match_all": {}}, "aggs": {"inner": {"nested": {"path": "majors"},
                                                                                      "aggs": {
                                                                                          "majors.degrees.title.keyword": {
                                                                                              "terms": {
                                                                                                  "field": "majors.degrees.title.keyword",
                                                                                                  "size": 5000,
                                                                                                  "order": {
                                                                                                      "_term": "asc"},
                                                                                                  "min_doc_count": 0}}}}}},
    "state.keyword5": {"filter": {"match_all": {}}, "aggs": {"state.keyword": {
        "terms": {"field": "state.keyword", "size": 100, "order": {"_term": "asc"}, "min_doc_count": 0}}}},
    "region6": {"filter": {"match_all": {}}, "aggs": {"region": {
        "terms": {"field": "region", "size": 100, "order": {"_term": "asc"}, "exclude": [0, -3], "min_doc_count": 0}}}},
    "ownership7": {"filter": {"match_all": {}}, "aggs": {
        "ownership": {"terms": {"field": "ownership", "size": 100, "order": {"_term": "asc"}, "min_doc_count": 0}}}},
    "level8": {"filter": {"match_all": {}}, "aggs": {
        "level": {"terms": {"field": "level", "size": 100, "order": {"_term": "asc"}, "min_doc_count": 0}}}},
    "sat-math9": {"filter": {"term": {"region": "2"}}, "aggs": {"sat-math": {"range": {"field": "sat_math_midpoint",
                                                                                       "ranges": [{
                                                                                           "key": "Mean SAT Math (100 - 200)",
                                                                                           "from": 100,
                                                                                           "to": 200}, {
                                                                                           "key": "Mean SAT Math (201 - 300)",
                                                                                           "from": 201,
                                                                                           "to": 300}, {
                                                                                           "key": "Mean SAT Math (301 - 400)",
                                                                                           "from": 301,
                                                                                           "to": 400}, {
                                                                                           "key": "Mean SAT Math (401 - 500)",
                                                                                           "from": 401,
                                                                                           "to": 500}, {
                                                                                           "key": "Mean SAT Math (501 - 600)",
                                                                                           "from": 501,
                                                                                           "to": 600}, {
                                                                                           "key": "Mean SAT Math (601 - 700)",
                                                                                           "from": 601,
                                                                                           "to": 700}, {
                                                                                           "key": "Mean SAT Math (701 - 800)",
                                                                                           "from": 701,
                                                                                           "to": 800}]}}}},
    "sat-rw10": {"filter": {"term": {"region": "2"}}, "aggs": {"sat-rw": {"range": {"field": "sat_reading_midpoint",
                                                                                    "ranges": [{
                                                                                        "key": "Mean SAT Writing (100 - 200)",
                                                                                        "from": 100,
                                                                                        "to": 200}, {
                                                                                        "key": "Mean SAT Writing (201 - 300)",
                                                                                        "from": 201,
                                                                                        "to": 300}, {
                                                                                        "key": "Mean SAT Writing (301 - 400)",
                                                                                        "from": 301,
                                                                                        "to": 400}, {
                                                                                        "key": "Mean SAT Writing (401 - 500)",
                                                                                        "from": 401,
                                                                                        "to": 500}, {
                                                                                        "key": "Mean SAT Writing (501 - 600)",
                                                                                        "from": 501,
                                                                                        "to": 600}, {
                                                                                        "key": "Mean SAT Writing (601 - 700)",
                                                                                        "from": 601,
                                                                                        "to": 700}, {
                                                                                        "key": "Mean SAT Writing (701 - 800)",
                                                                                        "from": 701,
                                                                                        "to": 800}]}}}},
    "act-composite11": {"filter": {"term": {"region": "2"}}, "aggs": {"act-composite": {
        "range": {"field": "act_midpoint", "ranges": [{"key": "Mean ACT (0 - 5)", "from": 0, "to": 5},
                                                      {"key": "Mean ACT (6 - 10)", "from": 6, "to": 10},
                                                      {"key": "Mean ACT (11 - 15)", "from": 11, "to": 15},
                                                      {"key": "Mean ACT (16 - 20)", "from": 16, "to": 20},
                                                      {"key": "Mean ACT (21 - 25)", "from": 21, "to": 25},
                                                      {"key": "Mean ACT (26 - 30)", "from": 26, "to": 30},
                                                      {"key": "Mean ACT (31 - 36)", "from": 31, "to": 36}]}}}},
    "gpa-avg12": {"filter": {"term": {"region": "2"}}, "aggs": {"gpa-avg": {"range": {"field": "gpa_avg", "ranges": [
        {"key": "GPA (0 - 2.0)", "from": 0, "to": 2}, {"key": "GPA (2.1 - 3.0)", "from": 2.1, "to": 3},
        {"key": "GPA (3.0 - 3.5)", "from": 3, "to": 3.5}, {"key": "GPA (3.5 - 4.0)", "from": 3.5, "to": 4},
        {"key": "GPA (4.0 - 4.3)", "from": 4, "to": 4.3}]}}}},
    "acceptance-rate13": {"filter": {"term": {"region": "2"}}, "aggs": {"acceptance-rate": {
        "range": {"field": "acceptance_rate", "ranges": [{"key": "Open Admission", "from": 0.9, "to": 1},
                                                         {"key": "Less Selective", "from": 0.76, "to": 1},
                                                         {"key": "Somewhat Selective", "from": 0.5, "to": 0.75},
                                                         {"key": "Very Selective", "from": 0.25, "to": 0.5},
                                                         {"key": "Most Selective", "from": 0, "to": 0.25}]}}}},
    "tuition14": {"filter": {"bool": {
        "must": [{"term": {"region": "2"}}, {"range": {"out_state_tuition_and_fees": {"gte": 10000, "lte": 70000}}}]}},
        "aggs": {"tuition": {"cardinality": {"field": "out_state_tuition_and_fees"}}}},
    "school-size15": {"filter": {"term": {"region": "2"}}, "aggs": {"school-size": {
        "range": {"field": "enrollment_total", "ranges": [{"key": "Small (< 5,000)", "from": 0, "to": 4999},
                                                          {"key": "Medium (5,000 - 20,000)", "from": 5000, "to": 20000},
                                                          {"key": "Large (> 20,000)", "from": 20001, "to": 200000}]}}}},
    "urbanization16": {"filter": {"match_all": {}},
                       "aggs": {"urbanization": {"terms": {"field": "urbanization", "size": 50, "min_doc_count": 0}}}},
    "life_radio17": {"filter": {"bool": {"must": [{"term": {"region": "2"}}, {"term": {"life_radio": "1"}}]}}},
    "life_news18": {"filter": {"bool": {"must": [{"term": {"region": "2"}}, {"term": {"life_news": "1"}}]}}},
    "life_drama19": {"filter": {"bool": {"must": [{"term": {"region": "2"}}, {"term": {"life_drama": "1"}}]}}},
    "life_band20": {"filter": {"bool": {"must": [{"term": {"region": "2"}}, {"term": {"life_band": "1"}}]}}},
    "life_chorus21": {"filter": {"bool": {"must": [{"term": {"region": "2"}}, {"term": {"life_chorus": "1"}}]}}},
    "sororities22": {"filter": {"bool": {"must": [{"term": {"region": "2"}}, {"term": {"sororities": "1"}}]}}},
    "fraternities23": {"filter": {"bool": {"must": [{"term": {"region": "2"}}, {"term": {"fraternities": "1"}}]}}},
    "rotc24": {"filter": {"bool": {"must": [{"term": {"region": "2"}}, {"term": {"rotc": "1"}}]}}},
    "study_abrd25": {"filter": {"bool": {"must": [{"term": {"region": "2"}}, {"term": {"study_abrd": "1"}}]}}},
    "srvc_psych26": {"filter": {"bool": {"must": [{"term": {"region": "2"}}, {"term": {"srvc_psych": "1"}}]}}},
    "srvc_health27": {"filter": {"bool": {"must": [{"term": {"region": "2"}}, {"term": {"srvc_health": "1"}}]}}},
    "srvc_wmn_ctr28": {"filter": {"bool": {"must": [{"term": {"region": "2"}}, {"term": {"srvc_wmn_ctr": "1"}}]}}},
    "srvc_veterans29": {"filter": {"bool": {"must": [{"term": {"region": "2"}}, {"term": {"srvc_veterans": "1"}}]}}},
    "career_services30": {
        "filter": {"bool": {"must": [{"term": {"region": "2"}}, {"term": {"career_services": "1"}}]}}},
    "career_stud_alumni_net31": {
        "filter": {"bool": {"must": [{"term": {"region": "2"}}, {"term": {"career_stud_alumni_net": "1"}}]}}},
    "esl32": {"filter": {"bool": {"must": [{"term": {"region": "2"}}, {"term": {"esl": "1"}}]}}}}, "size": 6,
           "from": 0, "sort": [{"_score": "desc"}],
           "_source": ["id", "name", "ownership", "gpa_avg", "acceptance_rate", "urbanization",
                       "in_state_tuition_and_fees", "out_state_tuition_and_fees", "level", "city", "state", "unit_id"],
           "query": {"function_score": {
               "functions": [{"field_value_factor": {"field": "weight", "factor": 1.2, "missing": 1}}]}}}

total_item_per_region = 100
step = 6


# since cc website divided US into 9 region
def process_raw_data(school_list):
    for school in school_list:
        school["url"] = "https://www.collegeconfidential.com/schools/school/" + school["_id"]
        del school["_index"]
    return school_list


def append_2_file(file_path, data):
    with open(file_path, 'ab+') as output_file:
        for item in data:
            json_item = json.dumps(dict(item), ensure_ascii=False) + "\n"
            output_file.write(json_item.encode("utf-8"))


for region in range(1, 10):
    payload["post_filter"]["term"]["region"] = str(region)
    start = 0
    while start < total_item_per_region + step:
        payload["from"] = start
        results = requests.post(url, data=json.dumps(payload), headers=headers).text
        json_res = json.loads(results)
        schools_info = process_raw_data(json_res["hits"]["hits"])
        total_item_per_region = int(json_res["hits"]["total"])
        append_2_file(file_path="../output/region_{}.jl".format(region),
                      data=schools_info)
        print("crawling region {} schools - {}%".format(region, round(100 * start / total_item_per_region, 3)))
        start += step
        time.sleep(random.randint(1, 3))
    print("region {} finished! (got {} records)".format(region, total_item_per_region))
