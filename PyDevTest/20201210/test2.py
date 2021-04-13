from numpy.core.defchararray import isnumeric
import re
from numpy.core.fromnumeric import sum

from string import ascii_uppercase

alpha_list = list(ascii_uppercase);
in_list = list()
alpha_cnt = list()


print('2번 문제','-'*50)
s = input('문자를 입력하세요(영문 대문자) => ') # 테스트할 문자열
    
err = ''
for x in s:    
    if not(ord(x) in range(65 , 91) or ord(x) == 32):
        err = '영문 대문자만 입력하세요.'
    elif( ord(x) in range(65 , 91) ):
        in_list.append(x)
        
    

print(err)


if err == '':
    print('빈도수를 세기 위한 리스트')    
    print(alpha_list)
    
    for x in alpha_list:
        cnt = 0;
        for y in in_list:
            if x == y:
                cnt +=1
        alpha_cnt.append(cnt)
    print('문자열의 빈도수')
    print(alpha_cnt)
    
        
    

        
        
    

