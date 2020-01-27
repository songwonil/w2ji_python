'''
Created on 2020. 01. 22.
@author: ycoplusone@gmail.com
'''
s1 = ['몽키', '선샤인', '시와', '톰']
s2 = [85, 92, 78, 100]

#print( zip(s1,s2) )
for x,y in zip( s1,s2 ):
    print(x,y)
    
s3 = {
    s1 : s2 for s1, s2 in zip(s1, s2)
}
print(s3)


s4 ={};
for x,y in zip( s1,s2 ):
    s4[x] = y

print(s4) 
