import os

def find_files(suffix, path):

    files_found = []

    if os.path.isfile(path):
        if path.endswith(suffix):
            files_found.append(path)
    elif os.path.isdir(path):
        for _file in os.listdir(path):
            files_found.extend(find_files(suffix, os.path.join(path, _file)))
    return files_found

print(find_files('.c', '/Users/shehryarbajwa/desktop/testdir'))