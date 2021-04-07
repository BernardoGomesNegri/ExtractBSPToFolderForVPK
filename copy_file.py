import os
import shutil
import pathlib

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

    #We need to create the subfolders in our output that do not exist
    output_path_obj = pathlib.Path(dst_file)
    output_parents = output_path_obj.parents
    output_parents_trimmed = []
    output_parents = reversed(output_parents)
    for parent in output_parents:
        if parent.is_relative_to(output):
            output_parents_trimmed.append(parent)
    for p in output_parents_trimmed:
        if not p.exists():
            os.mkdir(p)

    shutil.copy(src_file, dst_file)
    