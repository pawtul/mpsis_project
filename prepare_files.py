import json

for i in range(5, 46):
    filename = "data/cutMatrix{}.json".format(i)
    data = json.load(open(filename))
    data["d"] = 4
    json.dump(data, open(filename, 'w'))
