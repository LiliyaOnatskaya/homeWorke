# lst = [12, 3, 4, 10]  # => [10, 12, 3, 4]
# lst = [1] #=> [1]
lst = []  # => []
if len(lst) > 0:
    b = lst.pop()
    lst.insert(0, b)
print(lst)
