import os
from pathlib import Path
from CheckFolderIsValid import CheckFolderIsValid, CheckInputDir
from CopyMapContents import CopyMapContents
from CopyFile import CopyFile
import multiprocessing
import time
import argparse

if __name__ == '__main__':
    argParser = argparse.ArgumentParser()
    argParser.add_argument('-i', '--input', type=str)
    argParser.add_argument('-o', '--output', type=str)
    argParser.add_argument('-s', '--singlethread', action="store_true", default=False)
    args = argParser.parse_args()


    if args.input is None:
        InputDirStr = input('Where is your input folder, with the subfolder /maps? \n')
    else:
        InputDirStr = args.input
    
    print('Input folder: ', InputDirStr)
    CheckInputDir(InputDirStr)
    
    if args.output is None:
        OutputDirStr = input('Where should your output folder be? Preferrably empty \n')
    else:
        OutputDirStr = args.output
    
    print('Output folder: ', OutputDirStr)
    CheckFolderIsValid(OutputDirStr)

    IsParallel = not args.singlethread

    t0 = time.time() #Starts timer
    InputFolder = Path(InputDirStr)
    TempDir = Path(OutputDirStr)

    #Start by extracting all the map files and putting them into our temporary directory
    MapsFolderStr = os.path.join(InputDirStr, 'maps\\')
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
                CopyFile(file_, src_dir, InputDirStr, OutputDirStr)

    t1 = time.time()
    print('Operation complete in ', round(t1 - t0, 2), ' seconds')
    print('Files ready to be packaged in VPK')
