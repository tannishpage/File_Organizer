import universal_functions as uf
import os
import datetime

def Custome_pre_sorting(flist, sortingConfig):
    print('Analyzing folder...')
    make_folder_list = []
    for file in flist:
        for name in list(sortingConfig.keys()):
            if name in file:
                make_folder_list.append(sortingConfig[name])
    else:
        print('Making folders...')
        uf.makeFolder(make_folder_list)

def customeSorting(sortingConfig, sorting_dir):
    print('Preparing Environment for sorting...')
    flist = [x for x in os.listdir(os.getcwd()) if os.path.isfile(x)]
    Custome_pre_sorting(flist, sortingConfig)
    print('Sorting started...')
    start = datetime.datetime.now()
    for file in flist:
        for name in list(sortingConfig.keys()):
            if name in file:
                uf.Cp(file, sortingConfig[name], sorting_dir)
                print('{} moved to {}'.format(file, sortingConfig[name]))

    else:
        end = datetime.datetime.now()
        sort_time = (end-start).total_seconds()
        print("Sorting done")
        print('Took {} seconds to sort'.format(sort_time))
