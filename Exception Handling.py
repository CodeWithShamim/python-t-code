#Method 11
try:
    list1 = [10, 20, 30]
    list2 = [0, 5, 50, 60]

    result = list1[0] / list2[0]
    print(result)
except ZeroDivisionError:
     print("Last : Some problem!!")
finally:
      print("Done\n\n")


#Method 22
try:
    list1 = [10, 20, 30]
    list2 = [0, 5, 50, 60]

    result = list1[0] / list2[1]
    print("Again : ", result)

except IndentationError:
     print("Some problem!!")

#finally always print...................
finally:
      print("Value !!! Successful\n\n")



#-------------------------------------------------------------------------------------

try:
    list1 = [10, 20, 30]
    list2 = [0, 5, 50, 60]

    #error-1
    result = list1[0] / list2[0]
    print("Again : ", result)

    #error-1
    list = ["shamim"]
    resulst = list[7]
    print(result)

except (IndexError, ValueError, SyntaxError, TypeError, ZeroDivisionError, IndentationError):
     print("You have entered incorrect input!!")


finally:
      print("Successful!!!")
#---------------------------------------------------------------------------------------------

def voter(age):
    if age<18:
       raise ValueError("Invalid voter&&&.")

    return "You are allowed to vote."

try:
    
    print(voter(19))
    print(voter(17))

#Use as change error name....
except ValueError as v:
    print(v)