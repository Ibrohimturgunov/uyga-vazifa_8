import os

folder_path = "D:/Sen_bekorchiman"

def count_folders(path):
    if os.path.exists(path):
        folder_count = sum([len(dirs) for _, dirs, _ in os.walk(path)])
        print(f"{path} manzilida {folder_count} ta papka bor.")
    else:
        print(f"{path} topilmadi.")

count_folders(folder_path)
