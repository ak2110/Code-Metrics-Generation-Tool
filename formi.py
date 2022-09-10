import sys
import os
import p2
user_input = raw_input("Enter the path of your file: ")
assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
f = open(user_input,'r+')
content = f.read()
v = p2.mi_visit(content,True)
print("Maintainability index :")
print(v)

