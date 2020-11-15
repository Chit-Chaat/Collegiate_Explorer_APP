__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '11/12/2020 10:11 PM'

import csv


def gen_url(name_str: str):
    name_str = name_str.lower()
    name_str = name_str.replace('\'', '')
    name_str = name_str.replace('&', '-and-')
    words = name_str.split(' ')
    if 'at' in words:
        index = words.index('at')
        words[index] = '-'
    return "https://www.niche.com/colleges/" + "-".join(words)

def read_file(filepath):
    with open(filepath, encoding='utf-8') as file:
        raw_data = csv.reader(file)
        next(raw_data)
        id_name_url_tuple = list(map(lambda val: [val[1], val[2], gen_url(val[2])], raw_data))
        return id_name_url_tuple


def save2file(data, filepath):
    with open(filepath, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


if __name__ == '__main__':
    bundle_info = read_file("../data/college_explorer.csv")
    bundle_info[1653][2] = "https://www.niche.com/colleges/laboure-college/"
    bundle_info[1877][2] = "https://www.niche.com/colleges/university-of-phoenix---utah"
    bundle_info[1427][2] = "https://www.niche.com/colleges/university-of-phoenix-philadelphia"
    bundle_info[1400][2] = 'https://www.niche.com/colleges/university-of-puerto-rico---mayaguez'
    bundle_info[414][2] = 'https://www.niche.com/colleges/escuela-de-artes-plasticas-de-puerto-rico'
    bundle_info[251][2] = "https://www.niche.com/colleges/citadel-military-college-of-south-carolina/"

    save2file(bundle_info, "../data/temp.csv")
