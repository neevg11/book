import os


path = 'd:\\books'

def dir_file(path, level=1):
    for i in os.listdir(path):
        if os.path.isfile(path+'\\'+i):
            x = path+'\\'+i
            print(x.split('\\'))
            #print(x.split('\\')[3])
            print('Путь у файлу: ' + x)

    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i):
            dir_file(path+'\\'+i)


dir_file(path)
