__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '10/28/2020 4:52 PM'

import re


def format_qs_score(score_str):
    """
    help you generate a qs score
    1 - 100 : 5
    141-200 : 4
    =100: 4
    N/A 3
    :param score_str:
    :return:
    """
    score = 3
    if not score_str or score_str != "N/A":
        try:
            parts = int(list(filter(lambda val: val,
                                    list(re.split('-|=', score_str))))[0])
        except:
            return 3
        score = 5 - int(parts / 100)
        if score > 5 or score < 1:
            return 3
    return score


print(format_qs_score("=100"))

print(list(filter(lambda val: val, re.split('-|=', "=100"))))
