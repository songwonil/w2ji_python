def func1():
    ''' 1. 개요 '''
    str = '''
    pandas 설치  pip install pandas
    '''
    print( str )

def func2():
    '''2. pandas 사용법
    - 1차원  pandas.Series( data ) 
    '''
    import pandas as pd
    data = range(1,6)
    print(data , type(data))
    s = pd.Series(data)
    print( s , type(s) )

def func3():
    '''3. 2. pandas 사용법
    - 2차원 pandas.dataFrame( data )
    '''
    import pandas as pd
    data = {
    'year': [2016, 2017, 2018],
    'rate': [2.8, 3.1, 3.0],
    'gdp': ['1.637M', '1.73M', '1.83M']
    } 
    df = pd.DataFrame(data)
    print( df )
    print( df[{'rate','year'}] )

def func4():
    '''3. 2pandas 사용법 : 사용하지 않음
    - 3차원 panel
     '''
    import pandas as pd
    import numpy as np
    data = np.random.rand(2,3,4)
    print(data)
    #p = pd.Panel( data )
    #print( p )
    print( help( pd.Panel ) )


def func5():
    '''3. 데이타 엑세스 '''
    import pandas as pd
    
    








    
