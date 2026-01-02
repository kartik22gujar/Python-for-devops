try:
    fh = open("testile","w")  #if we change mode of file than error handle 
    fh.write("this is test file for exceptionl handling")

except IOError:
    print("Error: cant open an file and read a data")

else:
    print("writen content in the file successfuly")
    fh.close()