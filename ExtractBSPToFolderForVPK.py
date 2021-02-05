import os
from pathlib import Path
from CheckFolderIsValid import CheckFolderIsValid
from CheckFolderIsValid import CheckInputDir
from CopyMapContents import CopyMapContents
from CopyFile import CopyFile
import multiprocessing
import time


if __name__ == '__main__':

    #Use this where you want your output folder to be. Preferably empty
    OutputDirStr = input('Where should your output folder be? Preferrably empty \n')
    print('Output folder: ', OutputDirStr)
    CheckFolderIsValid(OutputDirStr)

    #Where the input folder is, with maps/
    InputFolderStr = input('Where is your input folder, with the subfolder /maps? \n')
    t0 = time.time() #Starts timer
    print('Input folder: ', InputFolderStr)
    CheckInputDir(InputFolderStr)

    IsParallelStr = input('Do you wish to turn on parallelization? It makes the program faster, but it can cause some issues. Type \'yes\' or \'no\'\n' )
    IsParallel = True
    if IsParallelStr.lower() == 'no':
        IsParallel = False

    InputFolder = Path(InputFolderStr)
    TempDir = Path(OutputDirStr)

    #Start by extracting all the map files and putting them into our temporary directory
    MapsFolderStr = os.path.join(InputFolderStr, 'maps\\')
    Maps = Path(MapsFolderStr).rglob('*.bsp')
    MapsList = [x for x in Maps]

    Arguments = []
    for m in MapsList:
        if IsParallel:
            Arguments.append((str(m), OutputDirStr))
        else:
            CopyMapContents(str(m), OutputDirStr)

    if IsParallel:
        pool = multiprocessing.Pool()
        pool.starmap(CopyMapContents, Arguments)
        pool.close()

    #Puts the original assets in our folder
    print('Copying original files')
    for src_dir, dirs, files in os.walk(InputFolder):
            for file_ in files:
                CopyFile(file_, src_dir, InputFolderStr, OutputDirStr)

    t1 = time.time()
    print('Operation complete in ', round(t1 - t0, 2), ' seconds')
    print('Files ready to be packaged in VPK')
