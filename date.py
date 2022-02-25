import json
date=[]
datefin=[]
with open('par25.json') as json_data2:
            data_dict2 = json.load(json_data2)
            for e in data_dict2:
                date.append(e["DatePublication"])


date = list(set(date))

for e in cand:
    candfin.append([e,0])


with open('par25.json') as json_data2:
    data_dict2 = json.load(json_data2)
    for e in data_dict2:
        for a in candfin:
            if(a[0][8]+a[0][9]==(e["DatePublication"][8] + e["DatePublication"][9])):
                a[1]+=1
sorted(candfin)
for i in candfin:
    print(str(i[0])+ " : " + str(i[1]))

data=dict(candfin)

data ={k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}
print(data)

with open("particule.json", "w") as file:
    json.dump(data, file, ensure_ascii=False)


