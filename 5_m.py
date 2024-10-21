import os

file_path = "D:/Sen_bekorchiman/fayl1"

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
        print(f"{path} muvaffaqiyatli o'chirildi.")
    else:
        print(f"{path} topilmadi.")

delete_file(file_path)
