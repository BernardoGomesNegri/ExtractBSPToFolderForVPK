import zipfile
import os
import sys

def CopyMapContents(map, output):
    print('Trying map ', map, ' to output: ', output)
    try:
        print('Trying map ', map, ' to output: ', output)
        z = zipfile.ZipFile(map)
        fileList = z.namelist()

        subdirectories = ('cfg', 'maps', 'materials', 'media', 'resource', 'scripts', 'sound', 'models')
        for embeddedFile in fileList:

            if(embeddedFile.startswith(subdirectories)):
                #We found an asset file!

                PathToExtract = os.path.join(output)

                z.extract(embeddedFile, PathToExtract)
        
        print('Done map ' + map)
    except Exception:
        type, value, traceback = sys.exc_info()
        print(value)
        print(traceback)
        print(type)
        print('Could not open' + str(map))
        return map