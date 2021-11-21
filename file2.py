from file1 import hashlooping
#hashlooping("hello", 600, 1, 2, "256")

v1 = hashlooping("hello", 600, 1, "r", "256")
#v2 = hashlooping("hello", 600, -1, 1, "-1")
#print(v1)

file = "text-testing.txt"

f = open(file, "w")
f.close()
#f = open(file, "r")
#print(f.read())