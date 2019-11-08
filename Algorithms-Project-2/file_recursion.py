import os


# print(os.listdir('/Users/shehryarbajwa/algorithms-challenges/Algorithms-Project-2'))
# print(os.path.isfile("./file_recursion.py"))
# print("./ex.py".endswith(".py"))

#The idea of the algorithm is very simple
#We provide it the path and the suffix
#The suffix refers to the type of file to iterate over
#The path refers to the path we are searching over

#Find files will check whether the path is a file or a path
#If it is a file, then we check whether the file ends in the .py or the suffix format
#If it is a directory, then we iterate over each element in the directory since os.listdir(path) returns a list
#For each element in the directory, we have to check the child elements of the directory
#Within the directory, there could be another directory
#Thus we can use recursion to check this
#We recurse on each _child of the list 
#We have to join the path with the child of the list
#For example the path is /Users and the child is /file_recursion.py or /projects_directory which is file
#Then we can run the function again and check if its a file we append it, if its a directory we find its children and keep repeating till we have exhausted our search

def find_files(suffix, path):

    found_files = []

    if os.path.isfile(path):
        if path.endswith(suffix):
            found_files.append(path)
    elif os.path.isdir(path):
        for _file in os.listdir(path):
            print(_file)
            found_files.extend(find_files(suffix, os.path.join(path, _file)))
    return found_files

print(find_files('.py', '/Users/shehryarbajwa/algorithms-challenges/Algorithms-Project-2'))
