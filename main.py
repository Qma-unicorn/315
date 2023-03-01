from datetime import datetime
import os
import hashlib

def main(folder):
    paths = []
    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            paths.append(os.path.join(root, name))
    if '..' in folder:
        folder = folder[3:]
    now = str(datetime.now()) + '.txt'
    if not os.path.isdir("scans"):
        os.mkdir("scans")
    outfile = open('scans/' + folder + '_out' + now, 'a')
    outfile.close()
    outfile = open('scans/' + folder + '_out' + now, 'w')

    for path in paths:
        with open(path, 'r') as f:
            textFile = ''.join(f.read().splitlines())
            my_hash = hashlib.sha256(textFile.encode('utf-8')).hexdigest()
        outfile.write(path + ': ' + my_hash + ' ' + '\n')
    outfile.close()

    # logs = []
    # for file in os.listdir('scans'):
    #     if folder + '_out' in file:
    #         logs.append('scans/' + os.path.join(file))
    # if len(logs) >= 2:
    #     files = sorted(logs)[-2:len(logs)]
    #     oldFile = open(files[0], 'r').readlines()
    #
    #     newFile = open(files[1], 'r').readlines()
    #     change = set([i.split(':')[0] for i in oldFile]) & set([i.split(':')[0] for i in newFile])
    #     if oldFile == newFile:
    #         print('success')
    #     else:
    #         print('error')
    #         noeq = {}
    #         new = []
    #         delete = []
    #         if not os.path.isdir("logs"):
    #             os.mkdir("logs")
    #         outfile = open('logs/' + folder + '_log' + now, 'a')
    #         outfile.close()
    #         outfile = open('logs/' + folder + '_log' + now, 'w')
    #         outfile.write('удалено' + ':' + '\n')
    #         for i in (set(oldFile) - set(newFile)):
    #             if not i.split(':')[0] in change:
    #                 outfile.write(i + '\n')
    #                 oldFile.pop(oldFile.index(i))
    #         outfile.write('создано' + ':' + '\n')
    #         for i in set(newFile) - set(oldFile):
    #             if not i.split(':')[0] in change:
    #                 outfile.write(i + '\n')
    #                 newFile.pop(newFile.index(i))
    #         outfile.write('измененно' + ':' + '\n')
    #         for i in range(len(newFile) - 1):
    #             if newFile[i] != oldFile[i]:
    #                 noeq[oldFile[i]] = newFile[i]
    #                 outfile.write(oldFile[i] + ' = '+ newFile[i] + '\n')
    #         outfile.close()

if __name__ == '__main__':
    main(input('folder: '))