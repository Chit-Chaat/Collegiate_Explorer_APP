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



from datetime import datetime

timestamp = 1601953076680
            # 1601954088226097
           #1601954324654
ss = datetime.now().timestamp()
print(ss)
dt_object = datetime.fromtimestamp(timestamp)

print("dt_object =", dt_object)

# "__cfduid=de35ecc27c5967b11534be4705f663dc31600910359; zabUserId=1600910362328zabu0.4824852002565372; _ga=GA1.2.45828874.1600910362; STYXKEY_first_visit=yes; __gads=ID=b21c474b5e86c1f6:T=1600910362:S=ALNI_Ma90NlVVtwzv035DnSQd9NY9MjtYQ; _fbp=fb.1.1600910365255.1074073799; _mkto_trk=id:335-VIN-535&token:_mch-topuniversities.com-1600910365652-13252; _hjid=b7c7af82-1323-4fa7-8438-c26f431ef67e; hubspotutk=c428a342d5aadd2a574b7856cae7f5ca; messagesUtk=5346d84eeb96482282f2fa9ec10b787a; has_js=1; _gid=GA1.2.1385675015.1601947909; " \
# "" \
# "__hstc=238059679.c428a342d5aadd2a574b7856cae7f5ca.1600910366050.1600910366050.1601947910159.2; __" \
# "hssrc=1; Hm_lvt_d4f650e8b28d910a41791663c4ef9cb3=1600910365,1601947911; _hjIncludedInPageviewSample=1; _hjTLDTest=1; _hjAbsoluteSessionInProgress=0; cookie-agreed=2; home-search-bar=1; zabVisitId=1601948123561zabv0.6312808910573757; Hm_lpvt_d4f650e8b28d910a41791663c4ef9cb3=1601948484; _gat=1"
#
#
#
# "__cfduid=de35ecc27c5967b11534be4705f663dc31600910359; zabUserId=1600910362328zabu0.4824852002565372; _ga=GA1.2.45828874.1600910362; STYXKEY_first_visit=yes; __gads=ID=b21c474b5e86c1f6:T=1600910362:S=ALNI_Ma90NlVVtwzv035DnSQd9NY9MjtYQ; _fbp=fb.1.1600910365255.1074073799; _mkto_trk=id:335-VIN-535&token:_mch-topuniversities.com-1600910365652-13252; _hjid=b7c7af82-1323-4fa7-8438-c26f431ef67e; hubspotutk=c428a342d5aadd2a574b7856cae7f5ca; messagesUtk=5346d84eeb96482282f2fa9ec10b787a; has_js=1; _gid=GA1.2.1385675015.1601947909; " \
# "" \
# "__hssrc=1; Hm_lvt_d4f650e8b28d910a41791663c4ef9cb3=1600910365,1601947911; " \
# "_hjIncludedInPageviewSample=1; _hjTLDTest=1; _hjAbsoluteSessionInProgress=0; cookie-agreed=2; home-search-bar=1; zabVisitId=1601948123561zabv0.6312808910573757; __hstc=238059679.c428a342d5aadd2a574b7856cae7f5ca.1600910366050.1601947910159.1601953079045.3; __hssc=238059679.1.1601953079045; Hm_lpvt_d4f650e8b28d910a41791663c4ef9cb3=1601953079; _gat=1"