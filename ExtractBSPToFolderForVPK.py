import zipfile
import os
import shutil
from pathlib import Path
import subprocess
import glob
import sys

#Use this where you want your output folder to be. Preferably empty
OutputDirStr = ''

#Where the input folder is, with maps/
InputFolderStr = ''

InputFolder = Path(InputFolderStr)
TempDir = Path(OutputDirStr)

#Start by extracting all the map files and putting them into our temporary directory
MapsFolderStr = os.path.join(InputFolderStr, 'maps\\')
Maps = Path(MapsFolderStr).rglob('*.bsp')
MapsList = [x for x in Maps]
subdirectories = ('cfg', 'maps', 'materials', 'media', 'resource', 'scripts', 'sound', 'models')
progressCount = 0

for map in MapsList:
    try:
        z = zipfile.ZipFile(map)
        fileList = z.namelist()

        for embeddedFile in fileList:

            if(embeddedFile.startswith(subdirectories)):
                #We found an asset file!

                PathToExtract = os.path.join(OutputDirStr)

                z.extract(embeddedFile, PathToExtract)
        
        progressCount = progressCount + 1
        print('Done map ' + str(progressCount) + ' out of ' + str(len(MapsList)))

    except Exception:
        type, value, traceback = sys.exc_info()
        print(value)
        print(traceback)
        print(type)
        print('Could not open' + str(map))
        

#Puts the original assets in our folder
print('Copying original files')
for src_dir, dirs, files in os.walk(InputFolder):
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            src_path = src_file.replace(InputFolderStr, '', 1)
            dst_file = os.path.join(OutputDirStr, src_path)
            shutil.copy(src_file, dst_file)
print('Files ready to be packaged in VPK')