#Use sub function for search and replace...
import re
Pattern = r"shamim"
text = "My name is shamim. My name is shamim. My name is shamim"
replace = re.sub(Pattern, "S" ,text, count=2)
print(replace)
