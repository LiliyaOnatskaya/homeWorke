# lst = [1, 2, 3, 4, 5, 6]  # => [[1, 2, 3], [4, 5, 6]]
lst = [1, 2, 3] #=> [[1, 2], [3]]
# lst = [1, 2, 3, 4, 5] #=> [[1, 2, 3], [4, 5]]
# lst = [1] #=> [[1], []]
# lst = [] #=> [[], []]
a = int((len(lst) / 2) + 0.5)
first_list = lst[:a]
second_list = lst[a:]
lst1 = [first_list, second_list]
print(lst1)
