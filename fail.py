import os

def file_collection(path):
    path = os.path.normpath(path)
    result = {"dirs": [], "files": []}
    for path, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            result["dirs"].append(dir)
            for file in filenames:
                result["files"].append(file)
                with open("skiper.txt", "w") as file:
                    file.write("\n{:-<50}\n".format("Directories"))
                    for dir in result["dirs"]:
                        file.write(f"\t{dir}\n")
                        file.write("\n{:-<50}".format("Files"))
                        for files in result["files"]:
                            file.write(f"\t{files}\n")
path = input("Введите путь: ")

if os.path.exists(path) and os.access(path, os.R_OK):
    file_collection(path)
else:
    print("Указанный путь не существует или нет доступа к чтению файлов и директорий.")