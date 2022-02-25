import json
from collections import Counter
cand=[]
candfin=[]
with open('par25.json') as json_data2:
            data_dict2 = json.load(json_data2)
            for e in data_dict2:
                cand.append(e["Candidat"])




cand=list(Counter(cand).keys())
nb=list(Counter(cand).values())

for a in cand:
