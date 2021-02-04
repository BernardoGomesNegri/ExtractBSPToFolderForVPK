import pathlib
import zipfile
import os
import sys

def CopyMapContents(map, output):
    #try:
    print('Trying map ', map, ' to output: ', output)
    z = zipfile.ZipFile(map)
    fileList = z.namelist()
    outputPath = pathlib.Path(output)
    subdirectories = ('cfg', 'maps', 'materials', 'media', 'resource', 'scripts', 'sound', 'models')
    for embeddedFile in fileList:

        if(embeddedFile.startswith(subdirectories)):
            #We found an asset file!

            PathToExtract = os.path.join(outputPath)

            z.extract(embeddedFile, PathToExtract)
        
    print('Done map ' + map)
    """except Exception:
        type, value, traceback = sys.exc_info()
        print(str(value))
        print(str(traceback))
        print(str(type))
        print('Could not open' + str(map))"""
    return