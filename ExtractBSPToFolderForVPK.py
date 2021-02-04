import os
import shutil
from pathlib import Path
from CheckFolderIsValid import CheckFolderIsValid
from CopyMapContents import CopyMapContents
import multiprocessing
import time

if __name__ == '__main__':
    t0 = time.time()
    #Use this where you want your output folder to be. Preferably empty
    #OutputDirStr = input('Where should your output folder should? Preferrably empty \n')
    OutputDirStr = "C:\\Temp\\Test\\"
    print('Output folder: ', OutputDirStr)
    CheckFolderIsValid(OutputDirStr)

    #Where the input folder is, with maps/
    #InputFolderStr = input('Where your input folder is, with the subfolder /maps? \n')
    InputFolderStr = "C:\\Temp\\Test2\\"
    print('Input folder: ', InputFolderStr)
    CheckFolderIsValid(InputFolderStr)

    InputFolder = Path(InputFolderStr)
    TempDir = Path(OutputDirStr)

    #Start by extracting all the map files and putting them into our temporary directory
    MapsFolderStr = os.path.join(InputFolderStr, 'maps\\')
    Maps = Path(MapsFolderStr).rglob('*.bsp')
    MapsList = [x for x in Maps]

    Arguments = []
    for m in MapsList:
        Arguments.append((str(m), OutputDirStr))


    pool = multiprocessing.Pool()
    pool.starmap(CopyMapContents, Arguments)
    pool.close()

    #Puts the original assets in our folder
    print('Copying original files')
    for src_dir, dirs, files in os.walk(InputFolder):
            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                src_path = src_file.replace(InputFolderStr, '', 1)
                dst_file = os.path.join(OutputDirStr, src_path)
                shutil.copy(src_file, dst_file)
    t1 = time.time()
    print('Operation complete in ', round(t1 - t0, 2), ' seconds')
    print('Files ready to be packaged in VPK')