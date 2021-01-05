import os
from os import path
import shutil
import datetime

Source_Path = '/home/tiago/Desktop/download-csv/cache'
Destination = '/home/tiago/Desktop/download-csv/dest'

Current_Date = datetime.datetime.today().strftime ('%d-%b-%Y')

#dst_folder = os.mkdir(Destination)


def main():
    for count, filename in enumerate(os.listdir(Source_Path)):
        dst =  "relatorios_" + Current_Date + "_" + str(count) + ".jpg"

        # rename all the files
        os.rename(os.path.join(Source_Path, filename),  os.path.join(Destination, dst))


# Driver Code
if __name__ == '__main__':
    main()

