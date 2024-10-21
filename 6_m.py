from pathlib import Path

folder_path = Path("D:/Sen_bekorchiman/Men_bekorchiman")

def delete_empty_folder(path):
    if path.exists() and path.is_dir():
        try:
            path.rmdir()
            print(f"{path} muvaffaqiyatli o'chirildi.")
        except OSError as e:
            print(f"{path} bo'sh emas yoki o'chirib bo'lmadi. Xatolik: {e}")
    else:
        print(f"{path} topilmadi yoki bu papka emas.")

delete_empty_folder(folder_path)
