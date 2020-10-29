import json
import uuid
import pandas as pd

cc_dict = {}
usn_dict = {}
dbp_dict = {}
qsr_dict = {}
n_dict = {}


f = open('collegeConfidential.jl', 'r')
for line in f.readlines():
    record = json.loads(line)
    cc_dict[record['url']] = record
f.close()

f = open('usnews.jl', 'r')
for line in f.readlines():
    record = json.loads(line)
    usn_dict[record['url']] = record
f.close()

f = open('dbpedia.jl', 'r')
for line in f.readlines():
    record = json.loads(line)
    dbp_dict[record['url']] = record
f.close()

f = open('qsranking.jl', 'r')
for line in f.readlines():
    record = json.loads(line)
    qsr_dict[record['url']] = record
f.close()

f = open('niche.jl', 'r')
for line in f.readlines():
    record = json.loads(line)
    n_dict[record['url']] = record
f.close()

f = open('entity_links.json', 'r')
entity_link = json.load(f)

data_columns = ['id', 'school_name', 'telephone', 'address', 'city', 'state', 'zip', 'website', 'cc_score', 'avg_ACT',\
           'avg_math_SAT', 'avg_read_SAT', 'avg_write_SAT', 'avg_GPA', 'accept_rate',\
           'undergrad_population', 'graduate_population', 'region', 'usn_popular_majors',\
           'freshman_retention', 'student_faculty_ratio', 'school_type',\
           'school_setting', 'academic_calendar', 'campus_size', 'motto', 'affiliation',\
           'athletics', 'president', 'mascot', 'school_color', 'number_of_students', 'logo',\
           'qs_score', 'qs_rank', 'n_popular_majors', 'median_earn_6_years',\
           'graduation_rate', 'employment_rate', 'average_aid', 'application_fee',\
           'student_athletic_percentage', 'application_deadline', 'application_website', 'sat_range', 'act_range', 'tuition_fees'] 

data_columns_usn = ['school_name', 'usn_category', 'usn_rank']
data_columns_n = ['school_name', 'n_category', 'n_grade']
data_frame = []
data_frame_usn = []
data_frame_n = []
for item in entity_link:
    data = []
    data_usn = []
    data_n = []
    data.append(uuid.uuid4())
    if 'cc' in item:
        cc = item['cc']
        data.append(cc_dict[cc].get('school'))
        data.append(cc_dict[cc].get('phone'))
        data.append(cc_dict[cc].get('address'))
        data.append(cc_dict[cc].get('city'))
        data.append(cc_dict[cc].get('state'))
        data.append(cc_dict[cc].get('zip'))
        data.append(cc_dict[cc].get('website'))
        data.append(cc_dict[cc].get('cc_score'))
        data.append(cc_dict[cc].get('avgACT'))
        data.append(cc_dict[cc].get('avgMathSAT'))
        data.append(cc_dict[cc].get('avgReadSAT'))
        data.append(cc_dict[cc].get('avgWriteSAT'))
        data.append(cc_dict[cc].get('avgGPA'))
        data.append(cc_dict[cc].get('acceptRate'))
        data.append(cc_dict[cc].get('undergradPop'))
        data.append(cc_dict[cc].get('gradPop'))
        data.append(cc_dict[cc].get('region'))
    else:
        for i in range(17):
            data.append('null')
    if 'usn' in item:
        usn = item['usn']
        data.append(':'.join(usn_dict[usn].get('popularMajors')) if usn_dict[usn].get('popularMajors') is not None else 'null')


        for key, value in dict(usn_dict[usn].get('usnewsRank')).items():
            data_usn.append(cc_dict[item['cc']].get('school'))
            data_usn.append(key)
            data_usn.append(value)
            data_frame_usn.append(data_usn)
            data_usn = []

        data.append(usn_dict[usn].get('freshmanRetentionRate'))
        data.append(usn_dict[usn].get('studentFacultyRatio'))
        data.append(usn_dict[usn].get('schoolType'))
        data.append(usn_dict[usn].get('setting'))
        data.append(usn_dict[usn].get('acadmeicCalendar'))
        data.append(usn_dict[usn].get('campusSize'))
    else:
        for i in range(7):
            data.append('null')
    if 'dbp' in item:
        dbp = item['dbp']
        data.append(':'.join(dbp_dict[dbp].get('motto')) if dbp_dict[dbp].get('motto') is not None or len(dbp_dict[dbp].get('motto')) != 0 else "null")
        data.append(':'.join(dbp_dict[dbp].get('affiliation') if dbp_dict[dbp].get('affiliation') is not None else 'null'))
        data.append(':'.join(dbp_dict[dbp].get('athletics') if dbp_dict[dbp].get('athletics') is not None else 'null' ))
        data.append(dbp_dict[dbp].get('president'))
        data.append(dbp_dict[dbp].get('mascot'))
        data.append(':'.join(dbp_dict[dbp].get('schoolColor') if dbp_dict[dbp].get('schoolColor') is not None else "null"))
        data.append(dbp_dict[dbp].get('numberOfStudents'))
    else:
        for i in range(7):
            data.append('null')
    if 'qsr' in item:
        qsr = item['qsr']
        data.append(qsr_dict[qsr].get('logo'))
        data.append(qsr_dict[qsr].get('qs_score'))
        data.append(qsr_dict[qsr].get('qs_rank'))
    else:
        for i in range(3):
            data.append('null')
    if 'n' in item:
        n = item['n']
        data.append(':'.join(n_dict[n].get('popularMajors')) if n_dict[n].get('popularMajors') is not None else "null" )

        for key, value in dict(n_dict[n].get('niche_score')).items():
            data_n.append(cc_dict[item['cc']].get('school'))
            data_n.append(key)
            data_n.append(value)
            data_frame_n.append(data_n)
            data_n = []

        data.append(n_dict[n].get('median_earning_6_years'))
        data.append(n_dict[n].get('graduation_rate'))
        data.append(n_dict[n].get('employment_rate'))
        data.append(n_dict[n].get('averageAid'))
        data.append(n_dict[n].get('application_fee'))
        data.append(n_dict[n].get('varsity_athletes'))
        data.append(n_dict[n].get('application_deadline'))
        data.append(n_dict[n].get('application_website'))
        data.append(n_dict[n].get('sat_range'))
        data.append(n_dict[n].get('act_range'))
        data.append(float(n_dict[n].get('tuitionFees').replace(',', '')))

    else:
        for i in range(12):
            data.append('null')
    for i in range(len(data)):
        if data[i] is None or data[i] == "null" or data[i] == ' ' or data[i] == '':
            data[i] = "N/A"

    data_frame.append(data)
df = pd.DataFrame(data_frame, columns=data_columns)
df_usn = pd.DataFrame(data_frame_usn, columns=data_columns_usn)
df_n = pd.DataFrame(data_frame_n, columns=data_columns_n)

df.to_csv('college_explorer.csv')
df_usn.to_csv('college_explorer_usn_ext.csv')
df_n.to_csv('college_explorer_n_ext.csv')
