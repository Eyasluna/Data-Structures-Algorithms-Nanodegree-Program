import os
def find_files(suffix, path, file= []):
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

    tem = suffix
    if path:
        tem = suffix + '/' + path
    for item in os.listdir(tem):
        tem1 = tem +  '/' + item
        if os.path.isfile(tem1) and tem1.endswith(".c"):
            file.append(tem1)

        elif os.path.isdir(tem1):
            file = find_files(tem, item, file)
    return file

