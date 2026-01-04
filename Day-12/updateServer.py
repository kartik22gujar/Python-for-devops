
def update_server(files_path,key,value):
    with open(files_path,"r")as file:
        lines=file.readlines()
    with open(files_path,"w")as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + str(value)+ "\n")
            else:
                file.write(line)

update_server("server.config","MAX_CONNECTIONS",200)