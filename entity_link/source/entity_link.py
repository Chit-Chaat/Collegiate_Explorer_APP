from pathlib import Path

import sys
import json
import rltk

global g_tokenizer
g_tokenizer = rltk.CrfTokenizer()
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

# RLTK Records
class USNewsRecord(rltk.Record):
    def __init__(self, raw_object):
        super().__init__(raw_object)
        self.name = ''

    @rltk.cached_property
    def id(self):
        return self.raw_object['url']

    @rltk.cached_property
    def school_string(self):
        return self.raw_object['school']

    @rltk.cached_property
    def tuition_fee(self):
        return self.raw_object['tuitionFees']

    @rltk.cached_property
    def accept_rate(self):
        return self.raw_object['acceptRate']

    @rltk.cached_property
    def address(self):
        return self.raw_object['address']

    @rltk.cached_property
    def school_tokens(self):
        global g_tokenizer
        return set(g_tokenizer.tokenize(self.school_string))


class CollegeConfidentialRecord(rltk.Record):
    def __init__(self, raw_object):
        super().__init__(raw_object)
        self.name = ''

    @rltk.cached_property
    def id(self):
        return self.raw_object['url']

    @rltk.cached_property
    def school_string(self):
        return self.raw_object['school']

    @rltk.cached_property
    def tuition_fee(self):
        return self.raw_object['tuitionFee']

    @rltk.cached_property
    def accept_rate(self):
        return self.raw_object['acceptRate']

    @rltk.cached_property
    def address(self):
        return [self.raw_object['address'], self.raw_object['city'], self.raw_object['state']]

    @rltk.cached_property
    def state(self):
        return self.raw_object['state']

    @rltk.cached_property
    def school_tokens(self):
        global g_tokenizer
        return set(g_tokenizer.tokenize(self.school_string))

class DBpediaRecord(rltk.Record):
    def __init__(self, raw_object):
        super().__init__(raw_object)
        self.name = ''

    @rltk.cached_property
    def id(self):
        return self.raw_object['url']

    @rltk.cached_property
    def school_string(self):
        return self.raw_object['school']

    @rltk.cached_property
    def state(self):
        return self.raw_object['state']

    @rltk.cached_property
    def school_tokens(self):
        global g_tokenizer
        return set(g_tokenizer.tokenize(self.school_string))

class QSRankingRecord(rltk.Record):
    def __init__(self, raw_object):
        super().__init__(raw_object)
        self.name = ''

    @rltk.cached_property
    def id(self):
        return self.raw_object['url']

    @rltk.cached_property
    def school_string(self):
        return self.raw_object['school']

    @rltk.cached_property
    def school_tokens(self):
        global g_tokenizer
        return set(g_tokenizer.tokenize(self.school_string))

class NicheRecord(rltk.Record):
    def __init__(self, raw_object):
        super().__init__(raw_object)
        self.name = ''

    @rltk.cached_property
    def id(self):
        return self.raw_object['url']

    @rltk.cached_property
    def school_string(self):
        return self.raw_object['school']

    @rltk.cached_property
    def accept_rate(self):
        return self.raw_object['acceptRate']

    @rltk.cached_property
    def tuition_fee(self):
        return self.raw_object['tuitionFees']

# Similarity Scoring
def state_similarity(r1, r2):
    s1 = r1.state
    s2 = r2.state
    if s1 is not None and s2 is not None:
        if '(' in s1:
            s1 = ' '.join(s1.split('(')[0].split('_')).strip()
            s1 = us_state_abbrev[s1]
        if '_' in s1:
            s1 = ' '.join(s1.split('_')).strip()
        if s1 == s2:
            return 1
    return 0

def school_similarity(r1, r2):
    s1 = r1.school_string[:int(len(r1.school_string) / 2)]
    s2 = r2.school_string[:int(len(r2.school_string) / 2)]

    similarity_score = rltk.jaro_winkler_similarity(s1, s2)
    if s1 == s2:
        return 1
    elif similarity_score > 0:
        return similarity_score
    else:
        return 0

def entire_school_similarity(r1, r2):
    s1 = r1.school_string
    s2 = r2.school_string

    similarity_score = rltk.jaro_winkler_similarity(s1, s2)
    if s1 == s2:
        return 1
    elif similarity_score > 0:
        return similarity_score
    else:
        return 0

def address_similarity(r_usn, r_cc):
    if r_usn.address is not None and r_cc.address is not None:
        address1 = r_usn.address
        address2 = r_cc.address
        if address1 and address2:
            address1 = list(map(lambda s: s.strip(), r_usn.address.split(',')))
            address1 = address1[:-1] + [address1[-1].split()[0]]
            address1 = [address1[0][:int(len(address1[0]) / 2)]] + address1[1:]
            address2 = [address2[0][:int(len(address2[0]) / 2)]] + address2[1:]
            address1 = ' '.join(address1)
            address2 = ' '.join(address2)
            similarity = rltk.jaro_winkler_similarity(address1, address2)

            if address1 == address2:
                return 1
            elif similarity > 0:
                return similarity
            else:
                return 0
           
    return 0

def tuition_fee_similarity(r_usn, r_cc):
    num1 = r_usn.tuition_fee
    num2 = r_cc.tuition_fee

    def percentage_difference(_num1, _num2):
        if _num1 > _num2:
            return (_num1 - _num2) / _num1
        return (_num2 - _num1) / _num2

    if num1 is not None and num2 is not None and num1 != ''  and num2 != '':
        num1 = int(num1.replace(',', ''))
        num2 = int(num2)
        if num1 != 0 and num2 != 0:
            return percentage_difference(num1, num2)
    return 1


def accept_rate_similarity(r_usn, r_cc):
    num1 = r_usn.accept_rate
    num2 = r_cc.accept_rate

    def percentage_difference(_num1, _num2):
        if _num1 > _num2:
            return (_num1 - _num2) / _num1
        return (_num2 - _num1) / _num2

    if num1 is not None and num2 is not None and num1 != 'N/A' and num2 != 'N/A' and num1 != '' and num2 != '':
        num1 = float(num1)
        num2 = float(num2)
        if num1 != 0 and num2 != 0:
            return percentage_difference(num1, num2)
    return 1

def school_rule(r_usn, r_cc):
    threshold = 0.9
    score_school = school_similarity(r_usn, r_cc)
    total = score_school
    if total > threshold:
        return total > threshold, total
    return False, 0

def address_rule(r_usn, r_cc):
    threshold = 0.9
    score_address = address_similarity(r_usn, r_cc)
    total = score_address
    if total > threshold:
        return total > threshold, total
    return False, 0

def numerical_rule(r_usn, r_cc):
    threshold = 0.01
    score_tuition_fee = tuition_fee_similarity(r_usn, r_cc)
    score_accept_rate = accept_rate_similarity(r_usn, r_cc)
    total = score_tuition_fee + score_accept_rate
    if total < threshold:
        return total < threshold, total
    return False, 1


# Rule Based Methods
def usn_cc_rule_based_method(r_usn, r_cc):
    threshold = 0.75
    _, rule3 = address_rule(r_usn, r_cc)
    _, rule2 = numerical_rule(r_usn, r_cc)
    _, rule1 = school_rule(r_usn, r_cc)

    total = rule1 * 0.7 + rule3 * 0.2 + (1 - rule2) * 0.1
    if total > threshold:
        return total > threshold, total
    return False, 0

def qsr_cc_rule_based_method(r_qsr, r_cc):
    threshold = 0.95
    score_school = entire_school_similarity(r_qsr, r_cc)
    total = score_school
    if total > threshold:
        return total > threshold, total
    return False, 0

def dbp_cc_rule_based_method(r_dbp, r_cc):
    threshold = 0.85
    score_school = entire_school_similarity(r_dbp, r_cc)
    score_state = state_similarity(r_dbp, r_cc)
    total = score_school * 0.9 + score_state * 0.1
    if total > threshold:
        return total > threshold, total
    return False, 0

def n_cc_rule_based_method(r_n, r_cc):
    threshold = 0.7
    score_school = entire_school_similarity(r_n, r_cc)
    _, rule2 = numerical_rule(r_n, r_cc)
    total = score_school * 0.75 + (1 - rule2) * 0.25
    if total > threshold:
        return total > threshold, total
    return False, 0 

# Blocking Validation
def create_dataset(input_file: str, rcrd_class: rltk.Record) -> rltk.Dataset:
    assert Path(input_file).suffix == ".jl"
    return rltk.Dataset(reader=rltk.JsonLinesReader(input_file), record_class=rcrd_class, adapter=rltk.MemoryKeyValueAdapter())

def create_token_blocks(dataset_1: rltk.Dataset, dataset_2: rltk.Dataset) -> rltk.block:
    tBG = rltk.TokenBlockGenerator()
    nGT = rltk.NGramTokenizer()
    block_1 = tBG.block(dataset_1, function_=lambda r: nGT.basic(r.school_tokens, 1))
    block_2 = tBG.block(dataset_2, function_=lambda r: nGT.basic(r.school_tokens, 1))
    block = tBG.generate(block_1, block_2)
    if block:
        return block
    return None

def evaluate_blocking(ds1_file: str, ds2_file: str, gt_file: str):
    dataset_1: rltk.Dataset = create_dataset(ds1_file, USNewsRecord)
    dataset_2: rltk.Dataset = create_dataset(ds2_file, CollegeConfidentialRecord)

    gt_set = get_ground_truth(gt_file, dataset_1, dataset_2)
    blocks = create_token_blocks(dataset_1, dataset_2)
    reduction_ratio(dataset_1, dataset_2, blocks, gt_set)
    pairs_completeness(dataset_1, dataset_2, blocks, gt_set)
    return blocks

def reduction_ratio(dataset_1, dataset_2, block_set, gt_set):
    pairs = rltk.get_record_pairs(dataset_1, dataset_2, block=block_set, ground_truth=gt_set)
    
    set_candidates_size = len(list(pairs))
    ds1_size = len(dataset_1.generate_dataframe())
    ds2_size = len(dataset_2.generate_dataframe())

    rr = (1 - float((set_candidates_size)/(ds1_size*ds2_size)))
    print(f'Reduction Ratio    = 1 - ({set_candidates_size}/{ds1_size}*{ds2_size}) = {rr:.06f}')
    return rr


def pairs_completeness(dataset_1, dataset_2, block_set, gt_set):
    gt_dict = dict()
    cand_matches = 0

    for id_r1, id_r2, label in gt_set:
        if label:
            gt_dict[id_r1] = id_r2
    gt_matches = len(gt_dict)

    for key, r1_id, r2_id in block_set.pairwise(dataset_1, dataset_2):
        if r1_id in gt_dict and gt_dict[r1_id] == r2_id:
            cand_matches += 1
            del gt_dict[r1_id]

    pc = float(cand_matches)/gt_matches
    print(f'Pairs Completeness = {cand_matches}/{gt_matches} = {pc:.06f}')
    return pc

def get_ground_truth(input_file: str, ds1: rltk.Dataset, ds2: rltk.Dataset) -> rltk.GroundTruth:
    devset_file_handle = open(input_file, "r")
    devset_data = json.load(devset_file_handle)
    gt = rltk.GroundTruth()
    for item in devset_data:
        r_usn = ds1.get_record(item['usnews'])
        r_cc  = ds2.get_record(item['cc']) 
        gt.add_positive(r_usn.raw_object['url'], r_cc.raw_object['url'])
    return gt

def eval_block():
    ds1_file = "./usnews.jl"
    ds2_file = "./collegeConfidential.jl"
    gt1_file = "./usn_cc.dev.json"

    evaluate_blocking(ds1_file, ds2_file, gt1_file)



# Main functions for each blocking
def cc_usn():
    ds1_file = "./usnews.jl"
    ds2_file = "./collegeConfidential.jl"

    ds_usn = create_dataset(ds1_file, USNewsRecord)
    ds_cc = create_dataset(ds2_file, CollegeConfidentialRecord)
    linkage_records = []
    for r_usn in ds_usn:
        threshold = 0.75
        cc_url = ""
        result = False
        for r_cc in ds_cc:
            result, confidence = usn_cc_rule_based_method(r_usn, r_cc)
            if result and confidence > threshold:
                threshold = confidence
                cc_url = r_cc.id
        if cc_url:
            linkage_records.append({'cc_url': cc_url, 'usn_url': r_usn.id})
        else:
            linkage_records.append({'cc_url': None, 'usn_url': r_usn.id})

    with open('usn_cc_record_linkage.json', 'w') as f:
        f.write(json.dumps(linkage_records, indent=4))

def cc_qsr():
    ds2_file = "./collegeConfidential.jl"
    ds4_file = "./qsranking.jl"
    ds_qsr = create_dataset(ds4_file, QSRankingRecord)
    ds_cc = create_dataset(ds2_file, CollegeConfidentialRecord)

    linkage_records = []
    for r_qsr in ds_qsr:
        threshold = 0.95
        cc_url = ""
        result = False
        for r_cc in ds_cc:
            result, confidence = qsr_cc_rule_based_method(r_qsr, r_cc)
            if result and confidence > threshold:
                threshold = confidence
                cc_url = r_cc.id
        if cc_url:
            linkage_records.append({'cc_url': cc_url, 'qsr_url': r_qsr.id})
        else:
            linkage_records.append({'cc_url': None, 'qsr_url': r_qsr.id})

    with open('qsr_cc_record_linkage.json', 'w') as f:
        f.write(json.dumps(linkage_records, indent=4))
  
def cc_dbp():
    ds2_file = "./collegeConfidential.jl"
    ds3_file = "./dbpedia.jl"
    ds_dbp = create_dataset(ds3_file, DBpediaRecord)
    ds_cc = create_dataset(ds2_file, CollegeConfidentialRecord)

    linkage_records = []
    for r_dbp in ds_dbp:
        threshold = 0.85
        cc_url = ""
        result = False
        for r_cc in ds_cc:
            result, confidence = dbp_cc_rule_based_method(r_dbp, r_cc)
            if result and confidence > threshold:
                threshold = confidence
                cc_url = r_cc.id
        if cc_url:
            linkage_records.append({'cc_url': cc_url, 'dbp_url': r_dbp.id})
        else:
            linkage_records.append({'cc_url': None, 'dbp_url': r_dbp.id})
 
    with open('dbp_cc_record_linkage.json', 'w') as f:
        f.write(json.dumps(linkage_records, indent=4))


def cc_n():
    ds2_file = "./collegeConfidential.jl"
    ds5_file = "./niche.jl"
    ds_n = create_dataset(ds5_file, NicheRecord)
    ds_cc = create_dataset(ds2_file, CollegeConfidentialRecord)
    linkage_records = []
    for r_n in ds_n:
        threshold = 0.7
        cc_url = ""
        result = False
        for r_cc in ds_cc:
            result, confidence = n_cc_rule_based_method(r_n, r_cc)
            if result and confidence > threshold:
                threshold = confidence
                cc_url = r_cc.id
        if cc_url:
            linkage_records.append({'cc_url': cc_url, 'n_url': r_n.id})
        else:
            linkage_records.append({'cc_url': None, 'n_url': r_n.id})

    with open('n_cc_record_linkage.json', 'w') as f:
        f.write(json.dumps(linkage_records, indent=4))

if __name__ == "__main__":
    #cc_usn()
    #cc_qsr()
    #cc_dbp()
    #cc_n()
    
