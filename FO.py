import custom_sorter as cs
import default_sorter as ds
import universal_functions as uf
import os
import sys

#Use the sys args and a couple of if commands
#to determine which sorter to use and which
#directory to start sorting in

#-f : Config File, if left empty will use default sorter
#-dir: sort directory if left empty will not run
#-s: will sleep the computer after sorting finishes
#-m: Sorter designed for music sorting

arg_lables = ['-f', '-dir', '-s']
args = sys.argv
argument_list = []
sleep = False
for arg in arg_lables:
    if arg in args:
        if arg == '-s':
            sleep = True
            continue
        argument_list.append(args[args.index(arg)+1])
    else:
        argument_list.append('')


if argument_list[1] == '':#Checks for change of directory
    print("No directory given use -dir to specify directory")
    exit()

else:
    if argument_list[0] == '': #Loads config file
        sortingConfig, cfg_dir = uf.initiation()
        sorting_dir = argument_list[1]
        os.chdir(sorting_dir)
        ds.sorting(sortingConfig, cfg_dir, sorting_dir)#starts sorting
    else:
        sortingConfig, cfg_dir = uf.initiation(argument_list[0])
        sorting_dir = argument_list[1]
        os.chdir(sorting_dir)
        cs.customeSorting(sortingConfig, sorting_dir)

if sleep:
    print('Putting computer to sleep...')#puts the computer to sleep if necessary
    if os.name == 'posix':
        os.system("systemctl suspend")
    elif os.name == 'nt':
        os.system("shutdown -s -t 0")
else:
    pass
    
