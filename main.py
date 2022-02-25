# -*- coding: utf-8 -*-
import json

with open('fin.json', "w") as file:
    json.dump([], file)
pp=0
cp=0
with open('p-com2020.json', "r") as json_data:
    data_dict = json.load(json_data)
    for i in data_dict["features"]:
        #print(i["Circonscription"])
        with open('dsd.json') as json_data2:
            data_dict2 = json.load(json_data2)
            for e in data_dict2:
                #print(e["properties"]["libgeo"])
                if(e["Circonscription"] == i["properties"]["libgeo"]):
                    print("YES")
                    print(e["Circonscription"])
                    print(i["properties"]["libgeo"])
                    pp+=1
                    print(pp)
                    entry = {
	                    "ville": e["Circonscription"],
	                    "dpt": i["properties"]["dep"],
	                    "candidat": e["Candidat"],
                        "x": i["properties"]["xcl4326"],
                        "y": i["properties"]["ycl4326"]
                        }


                    filename = 'fin.json'
                    with open(filename, "r") as file:
                        data = json.load(file)
                    data.append(entry)
                    with open(filename, "w") as file:
                        json.dump(data, file, ensure_ascii=False)
                cp+=1

print(pp)
print(cp)



