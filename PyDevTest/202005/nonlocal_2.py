

def outer():
    
    a=2
    b=3
    print('locals in outer : a={} , b={} '.format(a,b))
    def inner():
        nonlocal a        
        a=100
        print('locals in outer : a={} , b={} '.format(a,b))
    inner()    
    print('locals in outer : a={} , b={} '.format(a,b))

if __name__ =="__main__":
    outer()