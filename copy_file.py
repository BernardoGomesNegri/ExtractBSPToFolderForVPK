import os
import shutil


def copy_file(file_, src_dir, input, output):

    src_file = os.path.join(src_dir, file_)

    #Make it relative
    src_path = src_file.replace(input, '', 1)

    #Remove the starting slash or else Python will think the starting slash means "start at root" or "start at c drive"
    if os.name == 'posix':
        src_path = src_file.replace(input, '', 1).replace('/', '', 1)
    else:
        src_path = src_file.replace(input, '', 1).replace('\\', '', 1)

    dst_file = os.path.join(output, src_path)
    shutil.copy(src_file, dst_file)
    