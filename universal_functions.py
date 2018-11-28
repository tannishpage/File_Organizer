import os
import datetime
path = 'FO_Default_config.cfg'
def initiation(confile=path):
    try:
        file = open(confile, 'r')
        file.seek(0)
        lines = file.readlines()
    except FileNotFoundError:
        print("Error: Configuration file '{}' not found.".format(confile))
        exit()
    sortingConfig = {}
    for line in lines:
        line = line.rstrip()
        key, value = line.split(":")
        sortingConfig[key] = value
    print("Configuration file loaded..")
    return sortingConfig, os.getcwd()

def new_extentions(new_list, configFile=path):
    confile = open(configFile + '/' + path, 'a')
    for new in new_list:
        confile.write('{}:{}\n'.format(new, input('Folder name for {}: '.format(new))))
    else:
        confile.close()

def sub_folder_create(folders):# This function is to solve Issue #3 opened on GitHub
    folder_path = []
    for x in folders:
        folder_path.append(x)
        try:
            os.mkdir("/".join(folder_path))
        except FileExistsError:
            continue

def makeFolder(folder_list):
    for folder in folder_list:
        try:
            os.mkdir(folder)
        except FileExistsError:
            continue
        except FileNotFoundError:
            sub_folder_create(folder.split("/"))

def Cp(fname, destination, sorting_dir):
    fileOriginal = open(fname, "rb")
    os.chdir(destination) #In this case destination is a full path.
    fileDuplicate = open(fname, "wb")
    fileDuplicate.write(fileOriginal.read())
    fileOriginal.close()
    fileDuplicate.close()
    os.chdir(sorting_dir)
    os.remove(fname)
