import json
import csv
from itertools import groupby
from operator import itemgetter

f = open('FinalResult.json')
data = json.load(f)
f.close()

f = csv.writer(open('result_CSV.csv', 'wb+'))

for item in data:
    f.writerow([item['name'], item['gender'], item['polite']])

f = csv.writer(open('resultAVG_CSV.csv', 'wb+'))
grouper = itemgetter("name", "gender")
result = []
for key, grp in groupby(sorted(data, key=grouper), grouper):
    temp_dict = dict(zip(["name", "gender"], key))
    temp_list = [float(item["polite"]) for item in grp]
    temp_dict["politeAVG"] = sum(temp_list) / len(temp_list)
    result.append(temp_dict)
    f.writerow([temp_dict["name"], temp_dict["gender"], temp_dict["politeAVG"]])

