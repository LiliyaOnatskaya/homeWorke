# lst = [0, 1, 0, 3, 12] #-> [1, 3, 12, 0, 0]
# lst = [0] #-> [0]
# lst = [1, 0, 3, 0, 0, 0, 5] #-> [1, 3, 5, 0, 0, 0, 0]
lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] #-> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
lst1 =[]
lst2 =[]
for el in lst:
    if el != 0:
        lst1.append(el)
    else:
        lst2.append(el)
lst1 += lst2
print(lst1)



