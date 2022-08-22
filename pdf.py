#importing
import os
import shutil
#declaring the location of from and to folders for transferration
from_dir="/Users/danishgoswami/Desktop/document_files"
to_dir="/Users/danishgoswami/Desktop/py"
files=os.listdir(from_dir)
for i in files:
    name,extensions=os.path.splitext(i)
    if extensions== " ":
        continue
    if extensions in [".txt", "‘.doc’", "‘.docx’", ".pdf"]:
        #source path
        path1=from_dir+'/'+i
        path2=to_dir+'/'+"files"
        #destination path
        path3=to_dir+'/'+"files"+'/'+i
        #checking if the path exists and if it does then directly move the files
        if os.path.exists(path2):
            print("moving"+i+"....")
            shutil.move(path1,path3)
        #if it does not then create the files and then move
        else:
            os.makedirs(path2)
            print("moving"+i+"....")
            shutil.move(path1,path3)
