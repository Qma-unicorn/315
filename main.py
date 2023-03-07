from datetime import datetime
import os
import hashlib

def main(folder):
    paths = []
    now = str(datetime.now()) + '.txt'
    if not os.path.isdir("scans"):
        os.mkdir("scans")
    outfile = open('scans/' + folder.split('/')[-1] + '_out' + now, 'a')
    outfile.close()
    outfile = open('scans/' + folder.split('/')[-1] + '_out' + now, 'w')

    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            try:
                with open(os.path.join(root, name), 'r') as f:
                    textFile = ''.join(f.read().splitlines())
                    my_hash = hashlib.sha256(textFile.encode('utf-8')).hexdigest()
                outfile.write(os.path.join(root, name) + ': ' + my_hash + ' ' + '\n')
            except:
                print(os.path.join(root, name))
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