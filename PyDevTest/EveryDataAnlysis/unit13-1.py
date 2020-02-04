'''
unit 13 숫자 데이터를 쉽게 다루게 돕는 numpy 라이브러리
'''

def func1():
    '''1. matplotlib 홈페이지'''
    import matplotlib.pyplot as plt
    import numpy as np
    t = np.arange( 0. , 5. , 0.2 )
    print(t)
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.show()   
    
def func2():
    '''numpy 두번째 '''
    import matplotlib.pyplot as plt
    t= []
    p2 = []
    p3 = []
    for i in range(0,50,2):
        t.append(i/10)
        p2.append((i/10)**2)
        p3.append((i/10)**3)
    
    print(t)
    print(p2)
    print(p3)
    plt.plot(t, t, 'r--', t, p2, 'bs', t, p3, 'g^')
    plt.show()

def func3():
    '''2. numpy 라이브러리 시작하기'''
    import numpy as np
    print(np.sqrt(4))# 2의 제곱근
    print( np.pi ) #파이
    print( np.sin(0) )
    print( np.cos(np.pi))
    a = np.random.rand(5)
    print( a[0] )
    print( type(a)  )
    print( np.random.choice(6,10) )
    print( np.random.choice(10,6,replace=False) )
    print(np.random.choice(6, 10, p=[0.5, 0.1, 0.1, 0.1, 0.1, 0.1]))

def func4():
    '''3. numpy 라이브러리를 활용해 그래프 그리기 '''
    import numpy as np
    import matplotlib.pyplot as plt
    dice = np.random.choice(6 , 10000)
    plt.hist(dice , bins=6)
    plt.show()

def func5():
    ''' numpy 확률을 '''
    import numpy as np
    import matplotlib.pyplot as plt
    dice = np.random.choice(6,1000 , p=[0.1,0.2,0.3,0.2,0.1,0.1] )
    plt.hist(dice , bins=6)
    plt.show()

def func6():
    '''numpy 를 사용한 버블 차트 그리기 코드 '''
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.random.randint( 10 , 100 , 200 )
    y = np.random.randint( 10 , 100 , 200 )
    size =np.random.rand(100)*100 
    print(x)
    print(y)
    print(size)
    plt.scatter(x, y, s=size , c=x , cmap='jet' , alpha=0.7)
    plt.colorbar()
    plt.show()

def func7():
    ''' unit 10 에서 사용하한 버블 차트 그리기 코드'''
    import matplotlib.pyplot as plt
    import random
    x = []
    y = []
    size = []     
    for i in range(200) :
        x.append(random.randint(10,100))
        y.append(random.randint(10,100))
        size.append(random.randint(10,100))
     
    plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
    plt.colorbar()
    plt.show()

def func8():
    ''' 4. numpy array 생성하기 '''
    import numpy as np
    a = np.array([1,2,3,4])
    print(a)
    b = np.array([1,2,'3',4])
    print(b)
    c = np.zeros(10)
    print(c)
    d = np.ones(10)
    print(d)
    e = np.eye(3)
    print(e)
    
    print( np.arange(3) )
    print( np.arange(3,7) )
    print( np.arange(3,7,2) )
    

def func9():
    ''' numpy array의 다양한 활용 '''
    import numpy as np
    a = np.zeros(10)+5
    print(a)

def func10():
    ''' numpy 라이브러리를 사용하여 재미있는 버블 차트 그리기 '''
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.random.randint( -100,100,1000 ) #-100 에서 100사이 값 1000개 추출
    y = np.random.randint( -100,100,1000 )  
    size = np.random.rand(100)*100
    mask1 = abs(x) > 50
    mask2 = abs(y) > 50
    x = x[ mask1 + mask2 ]
    y = y[ mask1 + mask2 ]
    plt.scatter(x, y, s=size, c=x, cmap='jet' , alpha=0.7)
    plt.colorbar()
    plt.show()

func10()
      














          

