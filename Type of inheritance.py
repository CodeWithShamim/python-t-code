#Hierarchical inheritance........
class shape:
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2

    def area(self):
        pass

class Triangle(shape):
     #add shape all method..
     def area(self):
        area = 0.5 * self.d1 * self.d2
        print("Triangle result : ", area)

class Rectangle(shape):
     #add shape all method..
     def area(self):
        area = self.d1 * self.d2
        print("Rectangle result : ", area)
        print("Hierarchical end!!!!\n")

t = Triangle(10, 20)
t.area()

r = Rectangle(20, 30)
r.area()

#----------------------------------------------------------------------------------------

#Multi_level inheritance........
class shape:
    def result1(self):
        print("shape class.")

    

class Triangle(shape):
     #add shape all method..
     def result2(self):
         print("Triangle class.")

class Rectangle(Triangle):
     #add Triangle all method..
     def result3(self):
         super().result1()
         super().result2()
         print("Rectangle class.")
         print("Multi-level end.!!!!\n")


r = Rectangle()
r.result3()

#-----------------------------------------------------------------------------

#Multiple inheritance........
class shape:
    def result(self):
        print("shape class.")

    

class Triangle():
     #add shape all method..
     def result(self):
         print("Triangle class.")

class Rectangle(shape, Triangle):
     #add shape, Triangle all method..
     def result3(self):
         super().result()
         super().result()
         print("Rectangle class.")
         print("Multiple end.!!!!\n")


r = Rectangle()
r.result3()


        