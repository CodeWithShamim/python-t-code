#super class, parent class, base class
class google:
     def call(self):
         print("You can call.")

     def message(self):
         print("You can message.")



#sub class, child class, derived class
class amazon(google):
     #add amazon all method..

     def photo(self):
         print("You can take photo.")



val = amazon()
val.call()
val.message()
val.photo()

'''
#value check
result = issubclass(amazon, google)
print(result)

result = issubclass(google, amazon)
print(result)


'''