li = list(range(1,11))
print(li)

li.sort(key=lambda x:x%2==0, reverse=True )
a = lambda x:x%2==0
print(li)
print(a(3))