import pathlib
import zipfile
import os
import sys

def copy_map_contents(map, output):
    try:
        print('Trying map ', map, ' to output: ', output)
        z = zipfile.ZipFile(map)
        file_list = z.namelist()
        output_path = pathlib.Path(output)

        #Make a list of subdirectories that should be extracted
        subdirectories = ('cfg', 'maps', 'materials', 'media', 'resource', 'scripts', 'sound', 'models')

        for embeddedFile in file_list:
            #embeddedFile is a string
            if(embeddedFile.startswith(subdirectories)):
                #We found an asset file!

                path_to_extract = os.path.join(output_path)
                
                #Extracting creates folders if necessary.
                z.extract(embeddedFile, path_to_extract)
            
        print('Done map ' + map)
    except Exception:
        type, value, traceback = sys.exc_info()
        print(str(value))
        print(str(traceback))
        print(str(type))
        print('Could not open' + str(map))
    return
