# Classes are useful because they allow manipulation of a set of data using many different functions.
# The class below has class variables balance and name that will be referenced to by all functions in the class.

"""Create a class called account"""
class Account:
    """Initializing some class variables"""
    def __init__(self,name, balance):
        """Assigning class variales values"""
        self.name = name
        self.balance = balance
        print('{}, your account was successfully created!'.format(self.name))

    """A few functions contained within the class"""

    """Withdrawal"""
    def withdraw(self, amount):      # parse the amount to be withdrawn
        """Check whether amount to be withdrawn is available"""
        if amount < self.balance:
            self.new_balance = self.balance - amount
            print('{}, your withdrawal of Ksh{} was successful! Current balance is Ksh{}.'.format(self.name, amount, self.new_balance))
        else:
            print('Transaction cancelled! Insufficient balance!')

    """Deposit"""
    def deposit(self, amount):
        self.balance += amount
        print('{}, Ksh{} has been deposited in your account.'.format(self.name, self.balance))

    def check(self):
        print('{}, your current balance is Ksh{}.'.format(self.name, self.balance))

"""Using the class"""
#customer1 = Account(0)
#customer1.deposit(50000)
#customer1.check()
#customer1.withdraw(10000)

"""New customer"""
#customer2 = Account('Mufasa', 0)
#customer2.deposit(100000)
#customer2.withdraw(500)








