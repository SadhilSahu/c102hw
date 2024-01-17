import os
import shutil

from_dir="C:\\Users\\Samiya and Sadhil\\Downloads"
to_dir="C:\\Users\\Samiya and Sadhil\\OneDrive\\Sadhil\\coding\\Class hw\\c102hw"

list_of_files=os.listdir(from_dir)
#print the list of files 
print(list_of_files)
for filename in list_of_files: 
    name,extension=os.path.splitext(filename)
    print(name)
    print(extension)
    if extension=="":
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1=from_dir+"\\"+filename
        path2=to_dir+"\\"+"Class 102 hw move file"
        path3=to_dir+"\\"+"Class 102 hw move file"+"\\"+filename
        if os.path.exists(path2):
            print("Moving" + filename + ".....")
            
            #move from path1 to path3
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving" + filename + ".....")
            shutil.move(path1, path3)


