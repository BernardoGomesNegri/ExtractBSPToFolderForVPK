import os
import shutil
import pathlib

def copy_file(file_: str, src_dir: str, input_dir: str, output_dir: str) -> None:

    src_file = os.path.join(src_dir, file_)

    #Make it relative
    src_path = os.path.relpath(src_file, input_dir)

    dst_file = os.path.join(output_dir, src_path)

    #We need to create the subfolders in our output that do not exist
    output_path_obj = pathlib.Path(dst_file)
    output_parents = output_path_obj.parents
    output_parents_trimmed = []
    output_parents = reversed(output_parents)
    for parent in output_parents:
        if parent.is_relative_to(output_dir):
            output_parents_trimmed.append(parent)
    for p in output_parents_trimmed:
        if not p.exists():
            os.mkdir(p)

    shutil.copy(src_file, dst_file)
