import custom_sorter as cs
import default_sorter as ds
import universal_functions as uf
import eyed3
import os
import datetime

def music_pre_sorting_metadata(flist):
    print('Analyzing folder...')
    make_folder_list = []
    albumToArtist = {}
    for file in flist:
        print(file)
        tag = eyed3.load(file)
        albumToArtist[tag.tag.album] = tag.tag.artist
    for album in albumToArtist.keys():
        make_folder_list.append("{}/{}".format(albumToArtist[album], album))
    else:
        print('Making folders...')
        uf.makeFolder(make_folder_list)
    return albumToArtist

def musicSortingMetadata(sorting_dir):
    print('Preparing Environment for sorting...')
    flist = [x for x in os.listdir(os.getcwd()) if os.path.isfile(x)]
    albumToArtist = music_pre_sorting(flist)
    print("Starting sorting...")
    start = datetime.datetime.now()
    for file in flist:
        tag = eyed3.load(file)
        for name in list(albumToArtist.keys()):
            if albumToArtist[name] == tag.tag.artist:
                if name == tag.tag.album:
                    uf.Cp(file, "{}/{}".format(tag.tag.artist, tag.tag.album), sorting_dir)
                    print('{} moved to {}'.format(file, "{}/{}".format(tag.tag.artist, tag.tag.album)))

    else:
        end = datetime.datetime.now()
        sort_time = (end-start).total_seconds()
        print("Sorting done")
        print('Took {} seconds to sort'.format(sort_time))
