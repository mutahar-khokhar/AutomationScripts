import os
#set the path to the directory where you want folders to be renamed
directory_path = r'C:\Users\--'
#text file which conatins names for folders
with open('what-file.txt', 'r') as file:
    folder_names = file.readlines()

folder_names = [name.strip() for name in folder_names]

folder_list = os.listdir(directory_path)

if len(folder_names) != len(folder_list):
    print("Number of folders and names do not match.")
else:
    for i, folder in enumerate(folder_list):
        if os.path.isdir(os.path.join(directory_path, folder)):
            new_name = folder_names[i]
            os.rename(os.path.join(directory_path, folder), os.path.join(directory_path, new_name))