'''
1. 클래스
'''
class Member():
    name = ''
    # 생성자
    def __init__(self , str):
        self.name = str    
    def showMsg(self ):
        
        print( 'member.name : ' , Member.name )
        print( 'self.name : ' , self.name )
    
    def aaa(self):
        print( 'member.name : ' , Member.name )
        print( 'self.name : ' , self.name )
        

class PowerMember(Member):
    mail = ''
    def __init__(self,str1 , str2):
        self.name = str1
        self.mail = str2
    
    def showMsg(self):
        print( 'self.name' , self.name)
        print( 'self.mail', self.mail)


a = Member('song won il')
a.showMsg()

b=  PowerMember('song','choi')
b.showMsg()