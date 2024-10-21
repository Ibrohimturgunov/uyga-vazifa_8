import os

folder_path = "D:/Sen_bekorchiman"

def count_files(path):
    if os.path.exists(path):
        file_count = sum([len(files) for _, _, files in os.walk(path)])
        print(f"{path} papkasida {file_count} ta fayl bor.")
    else:
        print(f"{path} topilmadi.")

count_files(folder_path) 
