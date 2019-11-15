import os

def find_files(suffix, path):
    files_found = []

    if os.path.exists(path):
        if os.path.isfile(path):
            if path.endswith(suffix):
                files_found.append(path)
        elif os.path.isdir(path):
            for _file in os.listdir(path):           
                files_found.extend(find_files(suffix, os.path.join(path, _file)))
        return files_found
    else:
        return 'Path doesnot exist'

#Test case 1
print(find_files('.c', '/Users/shehryarbajwa/desktop/testdir'))
#['/Users/shehryarbajwa/desktop/testdir/subdir3/subsubdir1/b.c', '/Users/shehryarbajwa/desktop/testdir/t1.c', '/Users/shehryarbajwa/desktop/testdir/subdir5/a.c', '/Users/shehryarbajwa/desktop/testdir/subdir1/a.c']

#Test case 2
print(find_files('.py', 'users/named_user/name'))
#Path doesnt exist

#Test case 3
print(find_files('hello', '/Users/shehryarbajwa/desktop/testdir'))
#[]