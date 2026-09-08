import re

with open("preproinsulin-seq.txt", "r") as file:
    text = file.read()

cleaned = re.sub(r"ORIGIN|\d+|//|\s+", "", text)

print("Cleaned text: " + cleaned)

index = 0
lsinsulin = 24
binsulin = 30
cinsulin = 35
ainsulin = 21

# Probably not the most efficient way to get the strings but I'm starting with what I know so far.
print("lsinsulin: ", end="")
while index < lsinsulin:
    print(cleaned[index], end="") 
    index += 1
print()

print("binsulin: ", end="")
while index < lsinsulin + binsulin:
    print(cleaned[index], end="") 
    index += 1
print()

print("cinsulin: ", end="")
while index < lsinsulin + binsulin + cinsulin:
    print(cleaned[index], end="") 
    index += 1
print()

print("ainsulin: ", end="")
while index < lsinsulin + binsulin + cinsulin + ainsulin:
    print(cleaned[index], end="") 
    index += 1
print()