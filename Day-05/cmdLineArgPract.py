import sys
def addition(num1,num2):
    a=num1+num2
    return a
    #print("Addition = ",  a )

def sub(num1,num2):
    return num1-num2
    #print("substration =",s)

def mul(num1,num2):
    return num1*num2
    #print("multiplication =",m)

num1 =float(sys.argv[1])
operation =sys.argv[2]
num2 =float(sys.argv[3])


if operation=="add":
    print(addition(num1,num2))

if operation=="sub":
    print(sub(num1,num2))

if operation=="mul":
    print(mul(num1,num2))

