import string

str = 'Python Community' #-> #PythonCommunity
# str = 'i like python community!' #-> #ILikePythonCommunity
# str = 'Should, I. subscribe? Yes!' #-> #ShouldISubscribeYes

for el in str:
    if el in string.punctuation:
        str = str.replace(el, "")
str = "#" + str.title().replace(" ", "")

if len(str) > 140:
    str = str[:140]
print(str)
