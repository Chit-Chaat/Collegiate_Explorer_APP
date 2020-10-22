import json
import uuid
from rdflib import Graph, URIRef, Literal, XSD, Namespace, RDF

# Namespace
rdf = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
rdfs = Namespace('http://www.w3.org/2000/01/rdf-schema#')
xml = Namespace('http://www.w3.org/XML/1998/namespace')
xsd = Namespace('http://www.w3.org/2001/XMLSchema#')
schema = Namespace('http://schema.org/')
collegex = Namespace('http://collegex.org/collegiate-explorer-ns#')

# Graph and Bind Namespace
my_kg = Graph()
my_kg.bind('rdf', rdf)
my_kg.bind('rdfs', rdfs)
my_kg.bind('xml', xml)
my_kg.bind('xsd', xsd)
my_kg.bind('schema', schema)
my_kg.bind('collegex', collegex)

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

for item in entity_link:
    node_uri = URIRef(collegex + '/' + '_'.join(cc_dict[item['cc']].get('school').split()))
    my_kg.add((node_uri, schema['identifier'], Literal(uuid.uuid4())))
    if 'dbp' in item:
        dbp = item['dbp']
        my_kg.add((node_uri, schema['slogan'], Literal(dbp_dict[dbp].get('motto'))))
        my_kg.add((node_uri, collegex['affiliation'], Literal(dbp_dict[dbp].get('affiliation'))))
        my_kg.add((node_uri, collegex['athletics'], Literal(dbp_dict[dbp].get('athletics'))))
        my_kg.add((node_uri, collegex['president'], Literal(dbp_dict[dbp].get('president'))))
        my_kg.add((node_uri, collegex['mascot'], Literal(dbp_dict[dbp].get('mascot'))))
        my_kg.add((node_uri, collegex['schoolColor'], Literal(dbp_dict[dbp].get('schoolColor'))))
        my_kg.add((node_uri, collegex['numberStudents'], Literal(dbp_dict[dbp].get('numberOfStudents'))))

    if 'cc' in item:
        cc = item['cc']
        my_kg.add((node_uri, schema['name'], Literal(cc_dict[cc].get('school'))))
        my_kg.add((node_uri, schema['telephone'], Literal(cc_dict[cc].get('phone'))))
        my_kg.add((node_uri, schema['location'], Literal(cc_dict[cc].get('address')) + ', ' + Literal(cc_dict[cc].get('city')) + ', ' + Literal(cc_dict[cc].get('zip'))))
        my_kg.add((node_uri, schema['sameAs'], Literal(cc_dict[cc].get('website'))))

        my_kg.add((node_uri, collegex['cc_score'], Literal(cc_dict[cc].get('cc_score'))))
        my_kg.add((node_uri, collegex['avgACT'], Literal(cc_dict[cc].get('avgACT'))))
        my_kg.add((node_uri, collegex['avgMathSAT'], Literal(cc_dict[cc].get('avgMathSAT'))))
        my_kg.add((node_uri, collegex['avgReadSAT'], Literal(cc_dict[cc].get('avgReadSAT'))))
        my_kg.add((node_uri, collegex['avgWriteSAT'], Literal(cc_dict[cc].get('avgWriteSAT'))))
        my_kg.add((node_uri, collegex['avgGPA'], Literal(cc_dict[cc].get('avgGPA'))))
        my_kg.add((node_uri, collegex['acceptRate'], Literal(cc_dict[cc].get('acceptRate'))))
        my_kg.add((node_uri, collegex['undergradPop'], Literal(cc_dict[cc].get('undergradPop'))))
        my_kg.add((node_uri, collegex['gradPop'], Literal(cc_dict[cc].get('gradPop'))))
        my_kg.add((node_uri, collegex['region'], Literal(cc_dict[cc].get('region'))))

    if 'usn' in item:
        usn = item['usn']
        my_kg.add((node_uri, collegex['usn_popularMajors'], Literal(usn_dict[usn].get('popularMajors'))))
        my_kg.add((node_uri, collegex['categoryRank'], Literal(usn_dict[usn].get('usnewsRank'))))
        my_kg.add((node_uri, collegex['freshmanRetention'], Literal(usn_dict[usn].get('freshmanRetentionRate'))))
        my_kg.add((node_uri, collegex['freshmanRetention'], Literal(usn_dict[usn].get('freshmanRetentionRate'))))
        my_kg.add((node_uri, collegex['studentFacultyRatio'], Literal(usn_dict[usn].get('studentFacultyRatio'))))
        my_kg.add((node_uri, collegex['schoolType'], Literal(usn_dict[usn].get('schoolType'))))
        my_kg.add((node_uri, collegex['schoolSetting'], Literal(usn_dict[usn].get('setting'))))
        my_kg.add((node_uri, collegex['academicCalendar'], Literal(usn_dict[usn].get('academicCalendar'))))
        my_kg.add((node_uri, collegex['campusSize'], Literal(usn_dict[usn].get('campusSize'))))

    if 'n' in item:
        n = item['n']
        my_kg.add((node_uri, collegex['n_popularMajors'], Literal(n_dict[n].get('popularMajors'))))
        my_kg.add((node_uri, collegex['n_score'], Literal(n_dict[n].get('niche_score'))))
        my_kg.add((node_uri, collegex['medianEarn6years'], Literal(n_dict[n].get('median_earning_6_years'))))
        my_kg.add((node_uri, collegex['graduationRate'], Literal(n_dict[n].get('graduation_rate'))))
        my_kg.add((node_uri, collegex['employmentRate'], Literal(n_dict[n].get('employment_rate'))))
        my_kg.add((node_uri, collegex['averageAid'], Literal(n_dict[n].get('averageAid'))))
        my_kg.add((node_uri, collegex['applicationFee'], Literal(n_dict[n].get('application_fee'))))
        my_kg.add((node_uri, collegex['studentAthleticPercentage'], Literal(n_dict[n].get('varsity_athletes'))))
        my_kg.add((node_uri, collegex['applicationDeadline'], Literal(n_dict[n].get('application_deadline'))))
        my_kg.add((node_uri, collegex['applicationWebsite'], Literal(n_dict[n].get('application_website'))))










    if 'qsr' in item:
        qsr = item['qsr']
        my_kg.add((node_uri, schema['logo'], Literal(qsr_dict[qsr].get('logo'))))
        my_kg.add((node_uri, collegex['qs_score'], Literal(qsr_dict[qsr].get('qs_score'))))
        my_kg.add((node_uri, collegex['qs_rank'], Literal(qsr_dict[qsr].get('qs_rank'))))

my_kg.serialize('college_triples.ttl', format='turtle')
