import os

# # Load in data
#load all the files in the directory

def get_single_file(filename):
    return os.path.join(os.path.dirname(__file__), filename)

def file_loader_dir(text_file_path):

    file_names = []
    text_file_paths = []

    for file in os.listdir(text_file_path):
        if file.endswith(".txt"):
            file_names.append(file)

            text_file_paths.append(os.path.join(text_file_path,file))
        
    return file_names, text_file_paths

def file_loader_single(filename):
    path = get_single_file(filename)
    file_names = []
    text_file_paths = []

    if filename.endswith(".txt"):
            file_names.append(filename)
            text_file_paths.append(os.path.abspath(filename))

    return file_names, text_file_paths
