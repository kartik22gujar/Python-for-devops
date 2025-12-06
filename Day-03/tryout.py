#variable Global & local
####################
#global variables
num1=10
num2=20

def adition():
    #loacl variable 
    num3=30
    print(num1+num2+num3) #num3 accses local variable

def sub():
    print(num1-num2)

adition()
sub()   