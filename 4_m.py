import os


folder_path = "D:/Men_bekorchiman"



def delete_folder(path):
    if os.path.exists(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as e:
                print(f"Xatolik: {e}")

        os.rmdir(path)
        print(f"{path} muvaffaqiyatli o'chirildi.")
    else:
        print(f"{path} topilmadi.")


delete_folder(folder_path)
