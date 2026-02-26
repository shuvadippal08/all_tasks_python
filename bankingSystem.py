from ABC import abstractmethod

class BankAccount(ABC):
    def __init__(self,account_number, customer_name,date_of_birth,balence):
        self.name = customer_name
        self.__dob = date_of_birth
        self.__account_number = account_number
        self.__balence = balence
    def _get_account_number(self):
        return self.__account_number
    def _get_balence(self):
        return self.__balence
    def get_balence(self):
        return self.__balence
    def get_name(self):
        return self.name
    def get_dob(self):
        return self.__dob
    def _set_balence(self, balence):
        self.__balence = balence
    
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def display_account_details(self):
        print("Account Number:", self.__account_number)
        print("Customer Name:", self.customer_name)
        print("Date of Birth:", self.__date_of_birth)
        print("Balance:", self.__balance)

class SavingsAccount(BankAccount):
    def __init__(self,account_number, customer_name,date_of_birth, balence, min_balence = 1000):
        super().__init__(account_number, customer_name,date_of_birth,balence)
        self.min_balence = min_balence
    def deposit(self, amount):
        if amount > 0:
            new_balence = self._get_balence()+amount
            self._set_balence(new_balence)
            print("Diposited: ",amount)
        else:
            return "Enter a valid amount please"
    def withdraw(self,amount):
        if amount < 0:
            return "cannot withdraw negative amount"
        elif amount < self._get_balence():
            self._set_balence(self._get_balence()-amount)
            print("withdrawn: ",amount)
            print("current balence: ",self._get_balence()-amount)
        else:
            return "Entered amount is invalid"
class CurrentAccount(BankAccount):
    def __init__(self,account_number, customer_name,date_of_birth, balence, overdraft = 2000):
        super().__init__(account_number, customer_name,date_of_birth,balence)
        self.overdraft = overdraft
    def deposit(self, amount):
        if amount > 0:
            new_balance = self.get_balance() + amount
            self._set_balance(new_balance)
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")
