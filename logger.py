import os
import hashlib
from datetime import datetime

def main(folder):
    scansFolder = 'scans'
    newFile = []
    now = str(datetime.now()) + '.txt'
    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            try:
                with open(os.path.join(root, name), 'r') as f:
                    textFile = ''.join(f.read().splitlines())
                    my_hash = hashlib.sha256(textFile.encode('utf-8')).hexdigest()
                    newFile.append(str(os.path.join(root, name) + ': ' + my_hash + ' ' + '\n'))
                    f.close()
            except:
                print(os.path.join(root, name))

    log = 0
    for file in os.listdir(scansFolder):
        if folder.split('/')[-1] + '_out' in file:
            log = os.path.join(scansFolder, file)
    oldFile = open(log, 'r').readlines()

    change = set([i.split(':')[0] for i in oldFile]) & set([i.split(':')[0] for i in newFile])
    if not os.path.isdir("logs"):
        os.mkdir("logs")
    outfile = open('logs/' + folder.split('/')[-1] + '_log' + now, 'a')
    outfile.close()
    if oldFile == newFile:
        print('success')
        outfile = open('logs/' + folder.split('/')[-1] + '_log' + now, 'w')
        outfile.write('success')
        outfile.close()
    else:
        print('error')
        print(oldFile)
        print(newFile)
        print('\n')
        noeq = {}
        outfile = open('logs/' + folder.split('/')[-1] + '_log' + now, 'w')
        outfile.write('удалено' + ':' + '\n')
        for i in (set(oldFile) - set(newFile)):
            if not i.split(':')[0] in change:
                outfile.write(i + '\n')
                oldFile.pop(oldFile.index(i))
        outfile.write('создано' + ':' + '\n')
        for i in set(newFile) - set(oldFile):
            if not i.split(':')[0] in change:
                outfile.write(i + '\n')
                newFile.pop(newFile.index(i))
        outfile.write('измененно' + ':' + '\n')
        for i in range(len(newFile)):
            if newFile[i] != oldFile[i]:
                noeq[oldFile[i]] = newFile[i]
                outfile.write(oldFile[i] + ' = '+ newFile[i] + '\n')
        print(oldFile)
        print(newFile)
        outfile.close()

start = datetime.now()
file_name = "folder.txt"
file_path = os.path.join(os.getcwd(), file_name)

if os.path.isfile(file_path):
    with open(file_name, 'r') as f:
        path_to_target_file = f.readline().strip()
    main(path_to_target_file)
else:
    print('целевая дериктория не указана')
    print('создать файл ' + file_name)
    print('укажите целую дерикторию')
    outfile = open(file_name, 'a')
    outfile.close()
print(datetime.now() - start)