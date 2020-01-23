'''
Created on 2020. 01. 22.
@author: ycoplusone@gmail.com
'''
print( '1. 반복문 :  while')
i = 1
while i <= 10:
    print(i)
    i +=1

print( '반복문 : for')
sum = 0
for i in range(11):
    sum +=i
    print(sum)
print(sum)

list = ['this','is','a','python']
for s in list:
    print(s)

print('break/continue')
i = 0
sum = 0
while True:
    i +=1
    if i ==5:
        continue
    if i>10:
        break
    sum +=1

print(sum)
print('4. range')
numbers = range(2,11,2)
for x in numbers:
    print(x)
print(numbers)

for i in range(10):
    print("%d hello"%(i))