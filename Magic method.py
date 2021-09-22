'''
__init__(self, other) = constractor.....
__str__(self, other)  = object value return....
__lt__(self, other)   = <
__le__(self, other)   = <=
__gt__(self, other)   = >
__ge__(self, other)   = >=
__eq__(self, other)   = ==
__nq__(self, other)   = !=
----------
__add__(self, other)  = +
__sub__(self, other)  = -
__mul__(self, other)  = *
__div__(self, other)  = /
'''
class google:
     def __init__(self, name, place):
        self.name = name
        self.place = place

     def __eq__(self, other):
         return self.name==other.name and self.place==other.place


     def __le__(self, other):
         return self.name==other.name and self.place==other.place

     def __ge__(self, other):
         return self.name==other.name and self.place==other.place
     
     def __str__(self):
        return f"Name : {self.name}, Place : {self.place}"
     def display(self):
        pass
       
      
c = google("COMPANY", "USA")
u = google("COMPANY", "USA")

print(c==u)
print(c<=u)
print(c>=u)