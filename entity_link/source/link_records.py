import json


f = open('usn_cc_record_linkage.json', 'r')
g = open('qsr_cc_record_linkage.json', 'r')
h = open('dbp_cc_record_linkage.json', 'r')
i = open('n_cc_record_linkage.json', 'r')
data = json.load(f)


links = dict()
for record in data:
     if 'cc_url' in record and record['cc_url'] is not None:
         links[record['cc_url']] = [record['usn_url']]

data = json.load(g)
for record in data:
    if 'cc_url' in record and record['cc_url'] is not None:
        if record['cc_url'] in links:
            links[record['cc_url']].append(record['qsr_url'])
        else:
            links[record['cc_url']] = [record['qsr_url']]

data = json.load(h)
for record in data:
    if 'cc_url' in record and record['cc_url'] is not None:
        if record['cc_url'] in links:
            links[record['cc_url']].append(record['dbp_url'])
        else:
            links[record['cc_url']] = [record['dbp_url']]


data = json.load(i)
for record in data:
    if 'cc_url' in record and record['cc_url'] is not None:
        if record['cc_url'] in links:
            links[record['cc_url']].append(record['n_url'])
        else:
            links[record['cc_url']] = [record['n_url']]


with open('link.json', 'w') as f:
    f.write(json.dumps(links, indent=4))

