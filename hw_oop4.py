
class BankAccount:
    __bank_address = "yavne"
    @staticmethod
    def highest(acc1,acc2,acc3):
        l= [acc1.__balance,acc2.__balance,acc3.__balance]
        return max(l)


    def __init__(self,owner: str,balance: float):
        self.__owner = owner
        self.__balance = balance

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount

    def withdrow(self,amount):
        self.__balance -= amount

    def is_rich(self):
        if self.__balance > 1000000:
            return True
        else:
            return False

    @classmethod
    def get_address(cls):
        return cls.__bank_address

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return self.__balance + other.__balance

    def __sub__(self, other):
        if isinstance(other, BankAccount):
            return self.__balance - other.__balance

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.__balance == other.__balance

    def __ne__(self, other):
        if isinstance(other, BankAccount):
            return self.__balance != other.__balance

    def __gt__(self, other):
        if isinstance(other, BankAccount):
            return self.__balance > other.__balance

    def __lt__(self, other):
        if isinstance(other, BankAccount):
            return self.__balance < other.__balance

    def __le__(self, other):
        if isinstance(other, BankAccount):
            return self.__balance <= other.__balance

    def __repr__(self):
        return f"BankAccount(owner='{self.__owner}', balance={self.__balance})"

    def __str__(self):
        return f"Owner: {self.__owner}, Balance: {self.__balance}"

    def __len__(self):
        return len(str(self.__balance))

    def __getitem__(self, key):
        if key == "owner":
            return self.__owner
        elif key == "balance":
            return self.__balance
        else:
            raise KeyError(f"Key '{key}' not found.")

    def __iter__(self):
        return iter((self.__owner, self.__balance))

    # def freeze(self):
    #     return (self.__owner, self.__balance)

a1= BankAccount("lior",10000)
a2= BankAccount("yossi",50000)
a3= BankAccount("yoni",60000)
a1.deposit(50)

print(a1.get_balance())

if a1.is_rich():
    print("Rich")
else:
    print("poor")

print(BankAccount.get_address())

print(BankAccount.highest(a1,a2,a3))
sum_balance = a1 + a2
sub_balance = a1 - a2
eq_balance = a1 == a2
ne_balance = a1 != a2
gt_balance = a1 > a2
lt_balance = a1 < a2

print(f"sum balance a1+a2  {sum_balance}")
print(f"sub balance a1-a2  {sub_balance}")
print(f"equal balance a1 == a2  {eq_balance}")
print(f"ne balance a1 != a2  {ne_balance}")
print(f"gt balance a1 > a2  {gt_balance}")
print(f"lt balance a1 < a2  {lt_balance}")
print(f"Length of balance: {len(a1)}")
print(repr(a1))
print(a1)
print(f"getitem Owner: {a1['owner']}")
print(f"getitem Balance: {a1['balance']}")
print("iter-")
for item in a1:
    print(item)

