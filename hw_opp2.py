
## HomeWork opp 2


class Customer:
    def __init__(self,name,email,id):
        self.name= name
        self.email= email
        self.__id= id

    @property # getter -  only see the 'id'
    def id(self):
        return self.__id
    @id.setter # setter - also change the 'id'
    def id(self,value):
        if value > 0:
            self.__id = value
            # confirm reject
        else:
            print( "id change reject")

    def __str__(self): # make a nice and readable print
        return f"Customer: {self.name}, email: {self.email}, id: {self.__id}"

    def __repr__(self):
        return f"Customer({self.name}, {self.email}, {self.__id}"


lior = Customer('lior','lior@gmail',1234)
lior.id = -5
print(lior.email)
print(lior.id)
print(lior) # __str__ print
print(repr(lior))

