__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '10/3/2020 7:44 PM'

import json


def append_2_file(file_path, data):
    with open(file_path, 'ab+') as output_file:
        for item in data:
            json_item = json.dumps(dict(item), ensure_ascii=False) + "\n"
            output_file.write(json_item.encode("utf-8"))


data = [{'_index': 'schools', '_type': 'school', '_id': 'new-york-university', '_score': 1971.8337,
         '_source': {'in_state_tuition_and_fees': 47750, 'ownership': 1, 'city': 'New York', 'level': 2,
                     'name': 'New York University', 'acceptance_rate': 0.16, 'state': 'NY', 'urbanization': 1,
                     'out_state_tuition_and_fees': 47750, 'unit_id': 193900, 'gpa_avg': 3.69},
         'url': 'https://www.collegeconfidential.com/schools/school/new-york-university'},
        {'_index': 'schools', '_type': 'school', '_id': 'university-at-buffalo-the-state-university-of-new-york',
         '_score': 1825.3728,
         '_source': {'in_state_tuition_and_fees': 10524, 'ownership': 2, 'city': 'Buffalo', 'level': 2,
                     'name': 'University at Buffalo, the State University of New York', 'acceptance_rate': 0.61,
                     'state': 'NY', 'urbanization': 2, 'out_state_tuition_and_fees': 28194, 'unit_id': 196088,
                     'gpa_avg': 91.9},
         'url': 'https://www.collegeconfidential.com/schools/school/university-at-buffalo-the-state-university-of-new-york'},
        {'_index': 'schools', '_type': 'school', '_id': 'temple-university', '_score': 1776.6908,
         '_source': {'in_state_tuition_and_fees': 19748, 'ownership': 2, 'city': 'Philadelphia', 'level': 2,
                     'name': 'Temple University ', 'acceptance_rate': 0.6, 'state': 'PA', 'urbanization': 1,
                     'out_state_tuition_and_fees': 34126, 'unit_id': 216339, 'gpa_avg': 3.54},
         'url': 'https://www.collegeconfidential.com/schools/school/temple-university'},
        {'_index': 'schools', '_type': 'school', '_id': 'the-george-washington-university', '_score': 1772.3741,
         '_source': {'in_state_tuition_and_fees': 50435, 'ownership': 1, 'city': 'Washington', 'level': 2,
                     'name': 'The George Washington University', 'acceptance_rate': 0.41, 'state': 'DC',
                     'urbanization': 1, 'out_state_tuition_and_fees': 50435, 'unit_id': 131469, 'gpa_avg': None},
         'url': 'https://www.collegeconfidential.com/schools/school/the-george-washington-university'},
        {'_index': 'schools', '_type': 'school', '_id': 'penn-state-university-park', '_score': 1769.2577,
         '_source': {'in_state_tuition_and_fees': 18450, 'ownership': 2, 'city': 'University Park', 'level': 2,
                     'name': 'Penn State University Park', 'acceptance_rate': 0.49, 'state': 'PA', 'urbanization': 3,
                     'out_state_tuition_and_fees': 35514, 'unit_id': 214777, 'gpa_avg': 3.58},
         'url': 'https://www.collegeconfidential.com/schools/school/penn-state-university-park'},
        {'_index': 'schools', '_type': 'school', '_id': 'university-of-maryland-college-park', '_score': 1682.9266,
         '_source': {'in_state_tuition_and_fees': 10779, 'ownership': 2, 'city': 'College Park', 'level': 2,
                     'name': 'University of Maryland, College Park', 'acceptance_rate': 0.47, 'state': 'MD',
                     'urbanization': 2, 'out_state_tuition_and_fees': 38846, 'unit_id': 163286, 'gpa_avg': 4.32},
         'url': 'https://www.collegeconfidential.com/schools/school/university-of-maryland-college-park'}]

append_2_file("../output/test.jl", data)
