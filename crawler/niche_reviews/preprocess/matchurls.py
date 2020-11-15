__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '11/12/2020 10:11 PM'

import csv
import json


def read_file(filepath, index1=1, index2=2):
    with open(filepath, encoding='utf-8') as file:
        raw_data = csv.reader(file)
        next(raw_data)
        id_name_url_tuple = list(map(lambda val: [val[index1], val[index2]], raw_data))
        return id_name_url_tuple


def save2file(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(data)


def do_last_save(cc_name):
    manual_dict = {
        "Alabama Agricultural and Mechanical University": "Alabama A&M University",
        "American University of Puerto Rico - Bayamon": "Inter American University of Puerto Rico - Bayamon",
        "Anderson University ": "Anderson University - Indiana",
        "Anderson University": "Anderson University - South Carolina",
        "Assumption University": "Assumption College",
        "Aquinas College MI": "Aquinas College - Michigan",
        "Arizona State University at the Downtown Phoenix campus": "Arizona State University - Downtown Phoenix Campus",
        "Augustana College": "Augustana College - Illinois",
        "Alliant International University - San Diego": "Alliant International University",
        "American College for Medical Careers":"American College of Healthcare",
        "Bennett College": "Bennett College for Women",
        "Berkeley College-Woodland Park Campus": "Berkeley College - Woodland Park",
        "Bethany College WV": "Bethany College - West Virginia",
        "Bethel College KS": "Bethel College - Kansas",
        "Bethel University IN": "Bethel University - Indiana",
        "Bethel University MN": "Bethel University - Minnesota",
        "Bethel University TN": "Bethel University - Tennessee",
        "Brigham Young University-Hawaii": "Brigham Young University - Hawaii",
        "Brigham Young University-Idaho": "Brigham Young University - Idaho",
        "Bryn Athyn College of the New Church": "Bryn Athyn College",
        "Bryan College": "Bryan College - Tennessee",
        "California State University Channel Islands": "California State University - Channel Islands",
        "California State University, Dominguez Hills ": "California State University - Dominguez Hills",
        "California State University, Northridge ": "California State University - Northridge",
        "Cascadia College": "Cascadia Community College",
        "Calumet College of Saint Joseph": "Calumet College of St. Joseph",
        "Columbus College of Art & Design": "Columbus College of Art & Design",
        "Indiana University East": "Indiana University - East",
        "Indiana University South Bend": "Indiana University - South Bend",
        "Indiana University Northwest": "Indiana University - Northwest",
        "Indiana University-Purdue University Indianapolis": "Indiana University-Purdue University - Indianapolis (IUPUI)",
        "Indiana University Bloomington": "Indiana University - Bloomington",
        "Indiana University Southeast": "Indiana University - Southeast",
        "University of Minnesota Rochester": "University of Minnesota - Rochester",
        "Arizona State University at the West campus": "Arizona State University - West Campus",
        "Arizona State University at the Polytechnic campus":"Arizona State University - Polytechnic Campus"

    }
    # still has 400 school not match
    if cc_name in manual_dict.keys():
        return manual_dict.get(cc_name, "")
    else:
        return ""


if __name__ == '__main__':
    # load data
    bundle_info = read_file("../data/college_explorer.csv")
    true_info = read_file("../data/Sheet 1.csv", index1=0, index2=1)

    # convert list 2 dict
    true_id_dict = {}
    for niche_name, niche_id in true_info:
        true_id_dict[niche_name] = niche_id

    all_niche_names = list(map(lambda val: val
                               .replace('&', 'and')
                               .lower(), list(true_id_dict.keys())))
    count = 0
    result_dict = {}
    for ce_id, ce_name in bundle_info:
        result_dict[ce_name] = [ce_id]
        index = None
        try:
            index = all_niche_names.index(ce_name.replace(',', ' -').lower())
            niche_name, niche_id = true_info[index]
            result_dict[ce_name].append(niche_id)
        except:
            niche_name = do_last_save(ce_name)
            if niche_name != "":
                niche_id = true_id_dict[niche_name]
                result_dict[ce_name].append(niche_id)
            else:
                count += 1
                result_dict[ce_name].append("")
                print("cannot find this school -> ", ce_name)

    print(count)

    save2file(json.dumps(result_dict), "../data/true_urls.json")
