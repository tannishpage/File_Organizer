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

def makeFolder(folder_list):
    for folder in folder_list:
        try:
            os.mkdir(folder)
        except FileExistsError:
            continue
        except FileNotFoundError:
            os.mkdir(folder.split("/")[0])
            os.mkdir(folder)

def Cp(fname, destination, sorting_dir):
    fileOriginal = open(fname, "rb")
    os.chdir(destination) #In this case destination is a full path.
    fileDuplicate = open(fname, "wb")
    fileDuplicate.write(fileOriginal.read())
    fileOriginal.close()
    fileDuplicate.close()
    os.chdir(sorting_dir)
    os.remove(fname)
