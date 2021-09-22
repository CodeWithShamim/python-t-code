#Regular expressions using the re module....
import re
from typing import Pattern

Pattern = r"shamim"

if re.match(Pattern, "My name is shamim"):
    print("Matched")
else:
    print("Not Matched")

#-----------------------

Pattern = r"shamim"

if re.search(Pattern, "My name is shamim"):
    print("Matched")
else:
    print("Not Matched")

#-----------------------

Pattern = r"shamim"

print(re.findall(Pattern, "My name is shamim. My name is shamim. My name is shamim"))

#-----------------------

Pattern = r"sha"

print(re.findall(Pattern, "My name is shamim. My name is shamim. My name is shamim"))


#-----------------------

Pattern = r"shamim"
text = "My name is shamim"
match = re.search(Pattern, text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())