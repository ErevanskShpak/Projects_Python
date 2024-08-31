import json


f = open("firms.txt", 'r')

dictionary = {}
average = 0
number = 0
for line in f:
    content = line.split()
    profit = int(content[2]) - int(content[3])
    if profit > 0:
        average += profit
        number += 1
    dictionary.update({content[0]: profit})

f.close()

data = [dictionary, {"average_profit": average / number}]
print("Список: ", data)

fjson = open("data.json", 'w')
json.dump(data, fjson)
fjson.close()
