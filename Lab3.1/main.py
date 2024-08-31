f1 = open("f1.txt", 'w', encoding='utf-8')

print("Введите текст для записи в файл F1")
while True:
    string = input()
    if string == "":
        break
    f1.write(string)
    f1.write("\n")

f1.close()

f1 = open("f1.txt", 'r', encoding='utf-8')
f2 = open("f2.txt", 'w', encoding='utf-8')

for line in f1:
    temp = line.split()
    if len(temp) != 1 and temp.count(temp[1]) > 1:
        f2.write(line)

f1.close()
f2.close()

f2 = open("f2.txt", 'r')
content = f2.readlines()[-1]
f2.close()

number = 0
for el in content:
    if el.isdigit():
        number += 1

print("Количество цифр в последней строке f2:", number)
