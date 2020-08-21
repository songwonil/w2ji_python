from numpy.core.defchararray import isnumeric
import re
from numpy.core.fromnumeric import sum

 
def makesum(nums):
    ss = 0;
    for x in nums:
        ss = ss +  x
    return ss

print('1번 문제','-'*50)
s = input('숫자를 입력하세요 => ') # 테스트할 문자열

    
err = ''
for x in s:        
    if not(ord(x) in range(48 , 58) or ord(x) == 32):
        err = '숫자와 띄어쓰기만 입력 가능합니다.'

print(err)
if err == '':
    numbers = re.findall("\d+", s)
    numbers = list(map(int, numbers))
    print('정수 리스트 : ',numbers )
    print('정수 합계 : ',makesum(numbers))        
        
    

