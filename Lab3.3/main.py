f = open("schedule.txt", 'r', encoding='utf-8')

dictionary = {}
for line in f:
    content = line.split()
    content[0] = content[0][:-1]
    number = 0
    for i in range(1, len(content)):
        temp = ""
        for el in content[i]:
            if el.isdigit():
                temp += el
            else:
                break

        number += int(temp)

    dictionary.update({content[0]: number})

f.close()

print("Словарь: ", dictionary)