#Build in polymorphic function..
print(len("shamim"))
print(len([10, 20, 30]))
print("END!\n")

#user-define polymorphic function..
def sum(a, b, c=0):
    s = a+b+c
    return s

print(sum(10, 20))
print(sum(20, 30, 40))


#other polymorphic function...
'''
from abc import ABC,abstractmethod

class shape:
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2
    @abstractmethod
    def area(self):
        pass

class Triangle(shape):
     #add shape all method..

     #add abstrac aread method
     def area(self):
        area = 0.5 * self.d1 * self.d2
        print("Triangle result : ", area)


t = Triangle(10, 20)
t.area()
'''