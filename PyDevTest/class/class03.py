class Account:
    def __init__(self, name, money):
           self.user = name
           self.__balance = money
   
    def get_balance(self):
        return self.__balance
   
    def set_balance(self, money):
        if money < 0:
            return 
        self.__balance = money
   
if __name__ == '__main__':
       my_acnt = Account("greg", 5000)
       my_acnt.__balance = -3000
   
       print('1',my_acnt.get_balance())
       print('2',my_acnt.set_balance(6000))
       print('3',my_acnt.get_balance())
       print('4',my_acnt.__dict__)
       my_acnt._Account__balanceff = 567
       print('5',my_acnt.__dict__)