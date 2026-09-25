import os
import shutil
from os.path import isfile, join
from concurrent.futures import ThreadPoolExecutor

# path to the images
mypath = ''
dest_path = os.path.join(mypath, 'sortedDir')

images = [
    f for f in os.listdir(mypath)
    if isfile(join(mypath, f))
]


def move_file(filename):
    year = filename[4:8]

    destination = os.path.join(dest_path, year)
    os.makedirs(destination, exist_ok=True)

    print(f'Moving {filename} -> {destination}')

    shutil.copy2(
        os.path.join(mypath, filename),
        os.path.join(destination, filename)
    )


with ThreadPoolExecutor(max_workers=16) as executor:
    futures = [
        executor.submit(move_file, image)
        for image in images
    ]

    for future in futures:
        future.result()
