import os
import shutil

path = input('Name of the directory to be soted: ')
list = os.listdir(path)

for file in list:
    name,ext=os.path.splitext(file)

    ext=ext[1:]
    if ext=='':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path + '/' + file, path + '/' + ext ,'/' + file)
    else:
        os.makedirs(path + '/' + ext )
        shutil.move(path + '/' + file, path + '/' + ext ,'/' + file)