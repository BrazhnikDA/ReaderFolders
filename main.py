import os

path_to_favorite_folder = "C:\\test"
name_file = "\\TRNM"


# Возвращает список папок с полными путями
# dirName - путь до папки с папками
def read_folder(dir_name):
    subFolders = [f.path for f in os.scandir(dir_name) if f.is_dir()]
    for dir_name in list(subFolders):
        subFolders.extend(read_folder(dir_name))
    return subFolders


# Есть - True; Нет - false
def check_isfile(path_to_file):
    return os.path.isfile(path_to_file)


def main():
    result_string = list()
    list_folders = read_folder(path_to_favorite_folder)
    for path in list(list_folders):
        full_path = path + name_file
        if check_isfile(full_path):
            file = open(full_path, "r")
            result_string.append(file.readlines())
            file.close()
    file = open(path_to_favorite_folder + "\\result.txt", "w+")
    for txt in list(result_string):
        print(txt)
        file.writelines(txt)


if __name__ == '__main__':
    main()
