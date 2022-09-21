import keyword
import string

str = input('Enter name -> ')
result = False

if len(str) > 0:
    if not str[0].isnumeric():
        if not str.isdigit():
            if not keyword.iskeyword(str):
                signs = string.punctuation.replace('_', "")
                for el in str:
                    if el.isupper() or el in signs:
                        result = False
                        break
                    else:
                        result = True
print(result)