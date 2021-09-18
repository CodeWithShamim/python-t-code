#Recursion is a type of function that can call itself......
def fact(a):
    if a==1:
        return 1
    else:
        return a * fact(a-1)

#call function....
result = fact(4)
print("Factorial Result is : ", result,end=''"!!!")


