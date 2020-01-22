'''
Created on 2020. 01. 22.
@author: ycoplusone@gmail.com
'''
print('python 간단한 프로그램 작성')
a = 1;
b = 2;
c = a+b;
print(c);


print('※ phython 코딩 의 기초')
print('1. 코딩블럭 들여쓰기(identation)')
x =0;
if x>0:
    a= 1
    b=2
    c = a+b
else:
    a=-1
    b=-2
    c=a-b

print(c)


print('2. 파이썬 표준 라이브러리')
import math
n = math.sqrt(9.0)
print(n)


print('3. 코멘트')
#코멘트
print(1)
print(2) #코멘트2

print('4. pep')
print('개선 제안서이다.')

print('기본 데이터 \n 1.python 기본 데이터 타임')
print( int(3.5) )
print( 2e3 )
print( "1.6" )
print( float("inf") )
print( float("-inf") )
print( bool(0) )
print( bool(-1) )
print( bool("False") )
a = None
print( a )
print( a is None )

print( 2*3 )
print( 2**3 )

s = '''aaaa
bbbb
cccc
'''
print(s)

print('이름 : %s , 나이 : %s , 성별 : %s' %('이름이다','18','시발'))
x= 9
if x < 10:
    print('한자리')
    print(x)

if x < 100:print(x)


if x < 10:
    print('한자리')
elif x < 100:
    print()






