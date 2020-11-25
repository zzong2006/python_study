"""
    Apriori Algorithm
    Used 'Groceries Market Basket Dataset' : https://www.kaggle.com/irfanasrullah/groceries
"""

import csv
from collections import defaultdict
import json


def read_csv_file(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        user_list = []
        max_val = 0
        next(reader)  # skip the first line a CSV file
        for row in reader:
            user_list.append(row)
            max_val = max(int(user_list[-1][0]), max_val)
        print('the maximum number of items {} '.format(max_val))

    return user_list


def get_unique_items(users):
    items = defaultdict(set)
    n = len(users[-1])
    for user in users:
        for k in range(1, n):  # 0 index is number of items
            if user[k] != '':
                items[k].add(user[k])
            else:
                items[k].add('None')
    return items


path = '../input/groceries - groceries.csv'
threshold = 0.01
users = read_csv_file(path)
item_types = get_unique_items(users)

possible_combs = [()]
output = dict()
output[()] = users
total = len(users)
result = dict()

for key in sorted(item_types.keys()):
    new_possible_combs = []
    new_dict = dict()
    for comb in possible_combs:
        for item in item_types[key]:
            if item != 'None':
                temp_list = []
                for user in output[comb]:
                    if user[key] == item:
                        temp_list.append(user)

                new_dict[tuple(list(comb) + [item])] = temp_list

        # threshold 미만 조합들은 제거
        before_remove = len(new_dict.keys())
        going_to_remove = []
        for k in new_dict.keys():
            support_val = len(new_dict[k])/total
            if support_val < threshold :
                going_to_remove.append(k)
            elif k not in result:
                result[k] = support_val
        for k in going_to_remove:
            del new_dict[k]
        # print('threshold {} 보다 작은 key 조합 {}개 제거'.format(threshold, before_remove - len(new_dict.keys())))

        for k in new_dict.keys():
            new_possible_combs.append(k)
    output = new_dict
    possible_combs = new_possible_combs


# support 최종 결과 출력
for k in result.keys():
    print('key:{} / support value: {}'.format(k, result[k]))