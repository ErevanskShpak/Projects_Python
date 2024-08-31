my_dict = {'a': 12, 'b': 13, 'c': 56, 'd': 400, 'e': 58, 'f': 20}

max1 = 'a'
max2 = 'a'
max3 = 'a'
for key in my_dict:
    if my_dict[key] > my_dict[max1]:
        max3 = max2
        max2 = max1
        max1 = key
    elif my_dict[key] > my_dict[max2]:
        max3 = max2
        max2 = key
    elif my_dict[key] > my_dict[max3]:
        max3 = key

print("Ключ с самым высоким значением в словаре: ", max1)
print("Ключ сл значением на 2 месте в словаре : ", max2)
print("Ключ сл значением на 3 месте в словаре : ", max3)
