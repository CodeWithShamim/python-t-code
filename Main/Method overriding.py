
#Method not overriding...........
class google:
     def __init__(self):
         print("Result 1 : Hello, programmer!!.")


class amazon(google):
     #add amazon all method..
     pass


val = amazon()

#------------------------------------------------------------------
#Method overriding...........
class google:
     def __init__(self):
         print("Hello, programmer!!.")


class amazon(google):
     #add amazon all method..
     def __init__(self):
         print("Result 2 : Hello, Python programmer!!.")


val = amazon()
#-------------------------------------------------------------------------

class google:
     def __init__(self):
         print("Result 3 : Hello, programmer!!.")


class amazon(google):
     #add amazon all method..
     
     def __init__(self):
         super().__init__()
         print("Result 3 : Hello, Python programmer!!.")


val = amazon()