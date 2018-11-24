import universal_functions as uf
import os
import datetime

def endsWith(filename):
    extention_r = []
    for x in filename[::-1]:
        if x != '.':
            extention_r.append(x)
        else:
            extention_r.append('.')
            break
    extention = [x for x in extention_r[::-1]]
    return ''.join(extention)

def pre_sorting(flist, sortingConfig, cfg_dir):
    new_extention = []
    make_folder_list = []
    print('Analyzing folder for new extentions...')
    for file in flist:
        if endsWith(file) in list(sortingConfig.keys()):
            if sortingConfig[endsWith(file)] not in make_folder_list:
                make_folder_list.append(sortingConfig[endsWith(file)])
        else:
            if endsWith(file) not in new_extention:
                new_extention.append(endsWith(file))

    print('Making folders...')
    uf.makeFolder(make_folder_list)
    print('Adding new extentions to list...')
    uf.new_extentions(new_extention, cfg_dir)

def sorting(sortingConfig, cfg_dir, sorting_dir): #this function takes a dictionary as its argument
    print('Preparing environment for sorting...')
    flist = [x for x in os.listdir(os.getcwd()) if os.path.isfile(x)]
    pre_sorting(flist, sortingConfig, cfg_dir)
    print('Sorting started...')
    start = datetime.datetime.now()
    for file in flist:
        if endsWith(file) in list(sortingConfig.keys()):
            uf.Cp(file, sortingConfig[endsWith(file)], sorting_dir)
            print('{} moved to {}'.format(file, sortingConfig[endsWith(file)]))
    end = datetime.datetime.now()
    sort_time = (end-start).total_seconds()
    print('Sorting done')
    print('Took {} seconds to sort'.format(sort_time))
