__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '11/13/2020 4:54 PM'

import csv
import json
from operator import add

import findspark

findspark.init()

import os

from pyspark import SparkContext, SparkConf


def save2file(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(json.dumps(data))


if __name__ == '__main__':

    conf = SparkConf().setMaster("local[*]") \
        .setAppName("dsci558") \
        .set("spark.executor.memory", "4g") \
        .set("spark.driver.memory", "4g")
    sc = SparkContext(conf=conf)
    sc.setLogLevel("WARN")

    result = {}
    for file in os.listdir('../reviews/raw_tags'):
        ce_id = file.split('_')[0]
        result[ce_id] = {}
        raw_rdd = sc.textFile("../reviews/raw_tags/" + file) \
            .map(lambda line: (line.split(',')[0], int(line.split(',')[1]), line.split(',')[2].split('\\')))

        pos_people_rdd = raw_rdd.filter(lambda item: item[1] >= 4) \
            .map(lambda item: (item[0], 1)).aggregateByKey(0, add, add) \
            .sortBy(lambda kv: kv[1])

        pos_tags_rdd = raw_rdd.filter(lambda item: item[1] >= 4) \
            .flatMap(lambda item: item[2]).filter(lambda item: item != '') \
            .map(lambda tag: (tag, 1)).aggregateByKey(0, add, add) \
            .sortBy(lambda kv: kv[1], ascending=False) \
            .map(lambda kv: {"name": kv[0], "value": kv[1]})

        neg_people_rdd = raw_rdd.filter(lambda item: item[1] <= 2) \
            .map(lambda item: (item[0], 1)).aggregateByKey(0, add, add) \
            .sortBy(lambda kv: kv[1])

        neg_tags_rdd = raw_rdd.filter(lambda item: item[1] <= 2) \
            .flatMap(lambda item: item[2]).filter(lambda item: item != '') \
            .map(lambda tag: (tag, 1)).aggregateByKey(0, add, add) \
            .sortBy(lambda kv: kv[1], ascending=False) \
            .map(lambda kv: {"name": kv[0], "value": kv[1]})

        pos_people_info = pos_people_rdd.collectAsMap()
        pos_amount = sum(list(pos_people_info.values()))
        for key, val in pos_people_info.items():
            pos_people_info[key] = str(round((val / max(pos_amount, 1)) * 100, 1)) + "%"

        neg_people_info = neg_people_rdd.collectAsMap()
        neg_amount = sum(list(neg_people_info.values()))
        for key, val in neg_people_info.items():
            neg_people_info[key] = str(round((val / max(neg_amount, 1)) * 100, 1)) + "%"

        result[ce_id]['positive_info'] = {
            "data": pos_tags_rdd.take(40),
            "people": pos_people_info,
            "percent": str(round((pos_amount / max(neg_amount + pos_amount, 1)) * 100, 1)) + "%",
            "total": str(pos_amount)
        }
        result[ce_id]['negative_info'] = {
            "data": neg_tags_rdd.take(40),
            "people": neg_people_info,
            "percent": str(round((neg_amount / max(neg_amount + pos_amount, 1)) * 100, 1)) + "%",
            "total": str(neg_amount)
        }

    save2file(result, "../reviews/niche_reviews_result.json")
