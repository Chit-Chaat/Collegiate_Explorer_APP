__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '11/13/2020 1:54 PM'

import csv
import os
import spacy


def read_file(filepath):
    with open(filepath, encoding='utf-8') as file:
        raw_data = list(csv.reader(file))
        return raw_data


def save2file(data, filepath):
    with open(filepath, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def do_nlp(model, content):
    doc = model(content)
    result = []
    adjs = [(token.lemma_, token.i) for token in doc if token.pos_ == "ADJ"]
    for adj_str, index in adjs:

        if doc[index - 1].pos_ == 'ADV' \
                or doc[index - 1].pos_ == 'VERB' \
                or doc[index - 1].pos_ == 'ADJ' \
                or doc[index - 1].pos_ == 'PART':
            adj_str = doc[index - 1].lemma_ + " " + adj_str

        if index + 1 < len(doc):
            if doc[index + 1].pos_ == 'NOUN':
                adj_str = adj_str + " " + doc[index + 1].lemma_
        if index + 2 < len(doc):
            if doc[index + 2].pos_ == 'NOUN':
                adj_str = adj_str + " " + doc[index + 2].lemma_

        result.append(adj_str)

    return "\\".join(result)


def group_user(user_identifier: str):
    user_identifier = user_identifier.lower()
    if user_identifier == "niche user'":
        return "other"
    elif user_identifier == "freshman" \
            or user_identifier == "sophomore" \
            or user_identifier == "junior" \
            or user_identifier == "senior" \
            or user_identifier == 'alum':
        return user_identifier
    elif user_identifier == 'graduate student':
        return "senior"
    elif user_identifier == 'college freshman':
        return "freshman"
    elif user_identifier == 'college sophomore':
        return "sophomore"
    elif user_identifier == 'college junior':
        return "junior"
    elif user_identifier == 'college senior':
        return "senior"
    elif user_identifier == 'recent alumnus':
        return "alum"
    else:
        return "other"


if __name__ == '__main__':
    spacy.prefer_gpu()
    nlp = spacy.load("en_core_web_sm")
    # load review text
    all_files = os.listdir('../reviews/text')
    processed_files = os.listdir('../reviews/raw_tags')
    processed_ce_ids = list(map(lambda path: path.split("_")[0], processed_files))

    for file in all_files:
        ce_id = file.split("_")[0]
        if ce_id not in processed_ce_ids:
            result = []
            raw_data = read_file("../reviews/text/" + file)
            for review_item in raw_data:
                noun_adjs = do_nlp(nlp, review_item[2])
                result.append([group_user(review_item[0]), int(review_item[1]), noun_adjs])

            save2file(result, "../reviews/raw_tags/{}_tags.csv".format(ce_id))
            print("(*^▽^*) | finished parse school -> ", ce_id)
        else:
            print("╮(╯▽╰)╭ | have parsed this school -> ", ce_id)
