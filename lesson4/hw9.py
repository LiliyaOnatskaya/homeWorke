import random
my_list = []
lst = []
for i in range(random.randint(3, 10)):
    my_list.append(random.randint(1, 10))

lst.append(my_list[0])
lst.append(my_list[2])
lst.append(my_list[len(my_list)-2])
print(my_list)
print(lst)