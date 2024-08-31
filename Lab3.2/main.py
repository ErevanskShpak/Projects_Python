f = open("store.txt", 'r', encoding='utf-8')

average = 0
number = 0
print("Товары от 10 до 50 рублей\n")
for line in f:
    content = line.split()
    price = int(content[-1])
    if 10 <= price <= 50:
        print(line, end="")
        average += price
        number += 1

f.close()

print("\n\nСредняя цена товаров: ", average/number)
