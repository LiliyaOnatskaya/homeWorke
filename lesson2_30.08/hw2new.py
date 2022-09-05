digit=int(input('Enter 5 digit number - '))
a=(digit%10)*10000
b=(digit//10%10)*1000
c=(digit//100%10)*100
d=(digit//1000%10)*10
e=(digit//10000%10)
print(a+b+c+d+e)
