import os

pathToFavoriteFolder = "C:\\test"

# Возвращает список папок с полными путями
# dirName - путь до папки с папками
def fast_scandir(dirName):
    subFolders = [f.path for f in os.scandir(dirName) if f.is_dir()]
    for dirName in list(subFolders):
        subFolders.extend(fast_scandir(dirName))
    return subFolders


def main():
    print(fast_scandir(pathToFavoriteFolder))


if __name__ == '__main__':
    main()
