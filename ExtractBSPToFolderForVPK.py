import os
import shutil
from pathlib import Path
from CheckFolderIsValid import CheckFolderIsValid
from CopyMapContents import CopyMapContents
from CopyFile import CopyFile
import multiprocessing
import time


if __name__ == '__main__':
    t0 = time.time()
    #Use this where you want your output folder to be. Preferably empty
    OutputDirStr = input('Where should your output folder should? Preferrably empty \n')
    print('Output folder: ', OutputDirStr)
    CheckFolderIsValid(OutputDirStr)

    #Where the input folder is, with maps/
    InputFolderStr = input('Where your input folder is, with the subfolder /maps? \n')
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
    Args2 = list()
    for src_dir, dirs, files in os.walk(InputFolder):
            for file_ in files:
                Args2.append([file_, src_dir, InputFolderStr, OutputDirStr])

    pool2 = multiprocessing.Pool()
    pool2.starmap(CopyFile, Args2)
    pool2.close()

    t1 = time.time()
    print('Operation complete in ', round(t1 - t0, 2), ' seconds')
    print('Files ready to be packaged in VPK')