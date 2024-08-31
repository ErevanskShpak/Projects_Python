my_cort = (1, 2, -1, -5, 6, 8)
print("Кортеж до удаления: ", my_cort)

my_cort = list(my_cort)
for it in my_cort:
    if it < 0:
        my_cort.remove(it)
        break

print("Кортеж после удаления: ", tuple(my_cort))
