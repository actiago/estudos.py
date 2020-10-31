from dirsync import sync

source_path = '/home/tiago/Desktop/download-csv/data'
target_path = '/home/tiago/Desktop/download-csv/cache'

sync(source_path, target_path, 'sync') #for syncing one way
sync(target_path, source_path, 'sync') #for syncing the opposite way
