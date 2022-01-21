"""
Author - Sanchit Batra
Date - 21/02/22
Purpose - Practise
"""
import os
import shutil

dur = "/Users/sanchitbatra/Downloads"
for f in os.listdir(dur):
    os.chdir("/Users/sanchitbatra/Downloads")
    if os.path.isdir(f):
        check = os.listdir(f)
        while len(check) != 0:
            try:
                shutil.rmtree(f)
                break
            except Exception as e:
                shutil.rmtree(f)
    else:
        os.remove(f)

path = input("Please enter your folder in which you want to sort the extensions: ")

list_ = os.listdir(path)

for file_ in list_:
    name, ext = os.path.splitext(file_)

    ext = ext[1:]

    if ext == '':
        continue

    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + file_, path + '/' + ext + '/' + file_)

    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file_, path + '/' + ext + '/' + file_)
