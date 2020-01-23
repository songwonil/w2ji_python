import pandas as pd
 
print('series')
data = [1, 3, 5, 7, 9]
s = pd.Series(data)
print(s)

print('DataFrame')
import pandas as pd
data={
'year' : [2016,2017,2018],
'rate' : [2.8 , 3.1 , 3.0],
'gdp' : ['1.63M' ,'1.73m','1.83m']

}
df = pd.DataFrame(data)
print(data)
print(df)
'''
print('panel')
import pandas as pd
import numpy as np

data = np.random.rand(2,4,5)
p = pd.Panel( data )
print(p)
'''
print('3. 데이터 엑세스')
print(df)
print(df['year'])
print( df[df['year'] > 2016])
print( df['rate'].sum() )
print( df['rate'].mean() )
print( df.describe() )