'''
unit 09-2 혈액형 비율 표현하기
'''
file_path = 'C:\\git\\w2ji_python\\PyDevTest\\EveryDataAnlysis\\data\\gen.csv'

import matplotlib.pyplot as plt
import random
size = [ random.randint(1,100) , random.randint(1,100) , random.randint(1,100) , random.randint(1,100) ]
label = ['a' , 'b' , 'ab' ,'o']
plt.pie( size , labels = label )
plt.axis('equal' )
plt.show()
