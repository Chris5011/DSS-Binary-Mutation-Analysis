#!/usr/bin/pyhton3
# Author: Christoph Chris5011 Dorner
# Date: 22. Jan 2024
# Desc: This file is used to scrape all files in the /usr/bin and /usr/sbin directories hash them using nilsimsa, TLSH
# and SSDEEP and save the Hashes and save them in the the corresponding named files.
import importlib
import socket
import os
import platform

import NilsimsaHasher

current_host = str(socket.gethostname())
scraping_dir = '/usr/bin/'


def get_files_from_directory(scraping_dir):
    found_files = []
    for filename in os.listdir(scraping_dir):
        if os.path.isfile(filename) or platform.system() == 'Darwin':
            found_files.append(os.path.join(scraping_dir, filename))
    return found_files



def main():

    hasher_list = ['NilsimsaHasher', 'TLSHHasher']

    data_path = './data/' + current_host

    if not os.path.exists(data_path) or not os.path.isdir(data_path):
        os.mkdir(data_path)
    else:
        print('Directory already exsists!')

    if not os.path.exists(scraping_dir):
        print(f"The supplied Directory ({scraping_dir}) does not exist on this machine!")
        exit(1)

    file_list = get_files_from_directory(scraping_dir)
    file_list = file_list[:10]
    #print(file_list)


    for file in file_list:
        # print(file)
        # Creating the empty text-file to save the hashes to:
        file_name = file.split('/')[-1:][0]
        # print(type(file_name))
        save_file_path = os.path.join(data_path, file_name)
        # print(f'aaaaa: {save_file_path}')
        if not os.path.isfile(save_file_path):
            with open(save_file_path, 'w') as fp:
                pass
        try:
            fp = open(save_file_path, 'w', newline='\n')

            for hasher in hasher_list:
                # instance the hashers from the previously defined list:
                current_hasher = getattr(importlib.import_module(hasher), hasher)()

                # write the hashes to the file:
                bin_hash = current_hasher.hash_binary(file)
                fp.write(f'{str(current_hasher)},{bin_hash}\n')

        except IOError:
           print("An IO-Error occured, have fun finding the location where it is thrown xd")




if __name__ == '__main__':
    main()

