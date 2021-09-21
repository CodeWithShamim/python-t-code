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