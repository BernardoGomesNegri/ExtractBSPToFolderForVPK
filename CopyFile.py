import os
import shutil


def CopyFile(file_, src_dir, input, output):
    pass
    src_file = os.path.join(src_dir, file_)
    src_path = src_file.replace(input, '', 1)
    dst_file = os.path.join(output, src_path)
    shutil.copy(src_file, dst_file)