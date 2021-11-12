import sys
import os
from PIL import Image

# grab first and second argument
source_folder = sys.argv[1]
destination_folder = sys.argv[2]


# check if new folder exists, if not create it
if not os.path.isdir(destination_folder):
    os.mkdir(destination_folder)

# loop through all images files
filtered_list = list(
    filter(lambda file: file.endswith('.jpg'), os.listdir(source_folder)))

for file in filtered_list:
    name, ext = os.path.splitext(file)
    outfile = name + ".png"
    if file != outfile:
        try:
            with Image.open(f'{source_folder}/{file}') as im:
                # convert from jpg to png
                # save converted images to new folder
                im.save(f'{destination_folder}/{outfile}')
        except OSError:
            print('cannot convert', file)
print('all conversions done')
