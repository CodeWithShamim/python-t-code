'''
.(Dot)(Any character)
^$(Start, End)
*(0 or More)
+(1 or More)
?(0 or 1)
{and}

'''
#Number 1..........................................................
import re

Pattern = r"sh..im"

if re.search(Pattern, "My name is shGGim"):
    print("Nummber 1 : Matched")
else:
    print("Not Matched")


#Number 2..........................................................


Pattern = r"^sh..im$"

if re.search(Pattern, "shGGim"):
    print("Nummber 2 : Matched")
else:
    print("Not Matched")


#Number 3..........................................................


Pattern = r"(klklknbvc)*"

if re.search(Pattern, "My name is shGGim"):
    print("Nummber 3 : Matched")
else:
    print("Not Matched")


#Number 4..........................................................


Pattern = r"s+"

if re.search(Pattern, "My name is shGGim"):
    print("Nummber 4 : Matched")
else:
    print("Not Matched")


#Number 5..........................................................


Pattern = r"Ice(-)?Cream"

if re.search(Pattern, "IceCream"):
    print("Nummber 5 : Matched")
else:
    print("Not Matched")



#Number 6..........................................................


Pattern = r"a{1,3}"

if re.search(Pattern, "shamim"):
    print("Nummber 6 : Matched")
else:
    print("Not Matched")