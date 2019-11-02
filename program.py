print("Hello World")
intN=3
floatB=5
print(intN)
print(floatB)
name=input("please enter your name:")
print("your name is "+ "%s" %(name))
nameLen=len(name)
if nameLen<10:
    print("name length is less than 10")
elif nameLen>10 and nameLen<20:
    print("name length is greater than 10")
else:
    print("very large name")