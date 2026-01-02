import os
def list_files_inFolder(folder):
    files=os.listdir(folder)
    return files


folders_path=input("Enter list of folder path seprated by spaces: ").split()
for f in folders_path:
    print(f)
