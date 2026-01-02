"""
try:
    fh=open("testile","r")  #if we change mode of file than except block execute
    try:
        fh.write("this is my test file foe exceptional handling")
    finally:                #finally block are always execute 
        fh.close()
        print("data is writen in to the file and its closed sucessfully")
except IOError:
    print("Error: cant find a file and read data")


"""
def temp_convert(var):
    try:
        return int(var)
    except TypeError as Argument:
        print("The argument does not contain numbers\n",Argument)


temp_convert("xyz")