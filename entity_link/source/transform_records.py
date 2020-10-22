import json



f = open('link.json', 'r')
entity_link = json.load(f)

links = []
for key, values in entity_link.items():
    record = {}
    record['cc'] = key
    for uri in values:
        if 'https://www.usnews.com' in uri:
            record['usn'] = uri
        if 'http://dbpedia.org' in uri:
            record['dbp'] = uri
        if 'https://www.topuniversities.com' in uri:
            record['qsr'] = uri
        if 'https://www.niche.com' in uri:
            record['n'] = uri
    links.append(record)


with open('entity_links.json', 'w') as g:
    json.dump(links, g, indent=4) 
