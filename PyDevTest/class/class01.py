class test1():
    def __init__(self , a ,b ,c):
        self.__a = a
        self.b = b
        self.c = c
    
    def print(self):
        print(self.a , self.b , self.c)


gg = test1(1,2,3)
gg.print()


g1 = test1(11,22,33)
g1.print()