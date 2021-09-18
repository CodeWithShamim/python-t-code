#11
num = [5,11,23,30,40,50]

#use list comprehensions....ex>> expresion for num i list:........
result = [x*x for x in num]
print(result)



'''
num = [5,11,23,30,40,50]

result = list(filter(lambda x : x%2==0, num))
print(result)
'''
#22
num = [5,11,23,30,40,50]

result = [x*x for x in num if x%2==0]
print(result)