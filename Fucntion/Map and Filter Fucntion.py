#Map Functuion........
def shamim(a):
    return a*a

#map function first use function, iterable value like list.......
val = [10,20, 30, 40, 50]
collect = list(map(shamim, val))
print(collect)


#Filter Function........

num = [5,11,23,30,40,50]

result = list(filter(lambda x : x%2==0, num))
print(result)

#Ex.............................................
num = [5,11,23,30,40,50]

for i in num:
    print("loop result : ", i*i)

result = (lambda x : x%2==0)(5)
print(result)