try:
    list1 = [10, 20, 30]
    list2 = [0, 50, 60]

    result = list1[0] / list2[0]

except ZeroDivisionError:
     print("Some problem!!")


finally:
      print("Successful")


#print type error problem........input string value...
try:
    num = input("Enter your number : ")

    result = 50 / num

except TypeError:
     print("Some problem!!")


finally:
      print("Successful")





