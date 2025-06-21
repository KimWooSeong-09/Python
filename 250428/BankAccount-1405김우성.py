class BankAccount:
    def __init__(self, acnt):
        self.acnt = acnt
        self.balance = 0 
    
    def deposit(self, amt):
        self.balance += amt
        print(f'{self.acnt} 통장에 {amt}원이 입금됨.')
        print(f'{self.acnt} 현재 잔액은 {self.balance}원')

    def withdraw(self, amt):
        self.balance -= amt
        print(f'{self.acnt} 통장에서 {amt}원이 출금됨.')
        print(f'{self.acnt} 현재 잔액은 {self.balance}원')

# 사용 예시
a = BankAccount('123-456')
a.deposit(10000) 
a.withdraw(5000)

b = BankAccount('456-789')
b.deposit(2000)



