import re
Pattern = r"[aeiou]"

if re.search(Pattern, "IceCream"):
    print("Matched")
else:
    print("Not Matched")

#------------------------------------------
Pattern = r"[A-Z][a-z][0-9]"

if re.search(Pattern, "Xa5IceCream"):
    print("Matched")
else:
    print("Not Matched")
    