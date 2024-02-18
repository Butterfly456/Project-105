import os
import shutil
from_dir = "/Users/rinkurazdan/Downloads"
to_dir = "/Users/rinkurazdan/Desktop/BYJU"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name, ext = os.path.splitext(file_name)
    if ext == " ":
        continue
    if ext in ['.txt', '.pdf', '.doc', '.docx']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "df"
        path3 = to_dir + '/' + "df" + '/' + file_name
    if os.path.exists(path2):
        shutil.move(path1, path3)
    else:
        os.makedirs(path2)
        shutil.move(path1, path3)
