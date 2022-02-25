import json
from collections import Counter
cand=[]
candfin=[]
with open('par25.json') as json_data2:
            data_dict2 = json.load(json_data2)
            for e in data_dict2:
                if((e["Nom"][0]+e["Nom"][1])=="DE" and e["Nom"][2]==" "):
                   cand.append(e["Candidat"])

print(Counter(cand).keys())
print(Counter(cand).values())
cand = list(set(cand))

for e in cand:
    candfin.append([e,0])


with open('par25.json') as json_data2:
    data_dict2 = json.load(json_data2)
    for e in data_dict2:
        if ((e["Nom"][0] + e["Nom"][1]) == "DE" and e["Nom"][2] == " "):
            for a in candfin:
                if(a[0]==e["Candidat"]):
                    a[1]+=1
sorted(candfin)
for i in candfin:
    print(str(i[0])+ " : " + str(i[1]))

data=dict(candfin)

data ={k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}
print(data)

with open("particule.json", "w") as file:
    json.dump(data, file, ensure_ascii=False)


