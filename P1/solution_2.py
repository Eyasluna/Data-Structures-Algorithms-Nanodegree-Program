import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix == '':
        return []

    if len(os.listdir(path)) == 0:
        return []

    path_elem = os.listdir(path)
    path_file = [item for item in path_elem if '.' + suffix in item]
    path_folder = [item for item in path_elem if '.' not in item]

    for item in path_folder:
        path_file.extend(find_files(suffix=suffix, path=path + '/' + item))

    return path_file


path_base = os.getcwd() + '/testdir'

# Normal Cases:
print(find_files('c', path_base))
# ['t1.c', 'a.c', 'a.c', 'b.c']

print(find_files('h', path_base))
# ['t1.h', 'a.h', 'a.h', 'b.h']

print(find_files('z', path_base))
# []

# Edge Cases:
print(find_files('', path_base))
# []