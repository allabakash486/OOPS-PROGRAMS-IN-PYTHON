class ATM():
    print('Welcome to our Atm bank')
    ATM_brnach = 'Begaluru'
    Atm_name = 'Our ATM'
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
                print(f'{value} is credited successfull.....')
                print(f'Available balance is {self.bal} RS' )
            else:
                print('Insufficent funds....')
        else:
            print('Invalid pin...')
    @staticmethod
    def takepin():
        password = int(input('Enter the pin:'))
        return password
user1 = ATM('shaik',1234,93563,20,'male')
user1.Withdraw()
