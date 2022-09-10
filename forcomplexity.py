import sys
import os
import p1
user_input = raw_input("Enter the path of your file: ")
assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
f = open(user_input,'r+')
content = f.read()
from p1 import ComplexityVisitor
v = ComplexityVisitor.from_code(content)
print("Cyclomatic Complexity for code is:")
print(v.functions)
