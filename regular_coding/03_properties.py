class BankAccount:
    def __init__(self, name):
        self.name = name
        # __balance is now private. Can only be accessed from inside the class, its methods and properties
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if isinstance(value, int) and value >= 0:
            self.__balance = value
        else:
            print("Error, parameter must be a postive integer!")

    # def set_balance(self, param1):
    #     if isinstance(param1, int) and param1 >= 0:
    #         self.__balance = param1
    #     else:
    #         print("Error, parameter must be a postive integer!")


adrian_ing = BankAccount("Adrian")
# adrian_ing.set_balance(100)
print(adrian_ing.balance)

adrian_ing.balance = 100

print(adrian_ing.balance)