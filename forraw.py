import sys
import os
import p3
user_input = raw_input("Enter the path of your file: ")
assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
f = open(user_input,'r+')
content = f.read()
from p3 import analyze
print("Raw metrics for code are:")
print(analyze(content))
