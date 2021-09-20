#Number 1 -- 
class student:
     roll : " "
     gpa : " "

     #metod add
     def display(self):
          print(f" Roll : {self.roll}, GPA : {self.gpa}")
       




wazed = student()
wazed.roll = 101
wazed.gpa = 5.00
wazed.display()


alamin = student()
alamin.roll = 102
alamin.gpa = 4.00
alamin.display()

#-----------------------------------------------------------------

#Number 2...
class student:
     roll : " "
     gpa : " "

     #metod add
     def add(self, roll, gpa):
          self.roll = roll
          self.gpa = gpa

     def display(self):
          print(f" Roll : {self.roll}, GPA : {self.gpa}")
       




wazed = student()
wazed.add(103, 2.00)
wazed.display()


alamin = student()
alamin.add(104, 3.00)
alamin.display()
#---------------------------------------------------------------------------------------------

#number 3---Constructor
class student:
     roll : " "
     gpa : " "

     #metod add
     def __init__(self, roll, gpa):
          self.roll = roll
          self.gpa = gpa

     def display(self):
          print(f" Roll : {self.roll}, GPA : {self.gpa}")
       




wazed = student(105, 1.00)
wazed.display()


alamin = student(106, 1.00)
alamin.display()
