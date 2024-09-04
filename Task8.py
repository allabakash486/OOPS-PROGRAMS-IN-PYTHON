class Bank():
    print('Welcome to our bank')
    Bank_brnach = 'Begaluru'
    Bank_name = 'Our Bank'
    def __init__(self,name,pin,bal,Age,Gender):
        self.name = name
        self.pin = pin
        self.bal = bal
        self.Age = Age
        self.Gender = Gender
    def Withdraw(self):
        if self.pin == self.takepin():
            value = int(input('Enter the withdraw amount:'))
            if value <= self.bal:
                self.bal -= value
                print(f'{value} is Debited successfull.....')
                print(f'Available balance is {self.bal} RS' )
            else:
                print('Insufficent funds....')
        else:
            print('Invalid pin...')
    def deposite(self):
        if self.pin == self.takepin():
            value = int(input('Enter the Deposite amount:'))
            self.bal += value
            print(f'{value} is credited successfull.....')
            print(f'Available balance is {self.bal} RS' )
        else:
            print('Invalid pin...')
    def check_balance(self):
        if self.pin == self.takepin():
            print(f'Available balance is {self.bal} RS' )
        else:
            print('Invalid pin...')
    @staticmethod
    def takepin():
        password = int(input('Enter the pin:'))
        return password
user1 = Bank('shaik',1234,93563,20,'male')
user2 = Bank('shaik',1111,93563,20,'male')
user3 = Bank('shaik',2222,93563,20,'male')
user1.Withdraw()
user3.deposite()
user2.check_balance()
