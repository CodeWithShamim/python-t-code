'''
# r for readble, w for writable, r+ for read/write, a for append.............
#use readable..
file = open("name.txt", "r")
#check vale true or false....................
s = file.readable()
print(s)
result = file.read()
print(result)
file.close()




#when use writable then remove all text file..
file = open("name.txt", "w")
result = file.write("\nSalman islam joy-106")
print(result)
file.close()



#use append..
file = open("name.txt", "a")
result = file.write("\nSalman islam joy-106")
print(result)
file.close()


#create new text file......
file = open("name111.txt", "r")
result = file.read()
print(result)
file.close()

'''
file = open("name.txt", "r")
#when use readlines then all text print list...........
result = file.readlines()[0]
print(result)
file.close()
file = open("name.txt", "r")



#use loop ....................
file = open("name.txt", "r")
for i in file:
    print(i)




#html tag use 
file = open("hello.html", "w")
result = file.write("\n<h1>Hello everyone<h1>")
print(result)