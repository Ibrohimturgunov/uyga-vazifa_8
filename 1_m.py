import os

# folder_path = r"D:\Men_bekorchiman"
#
# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)
#     print(f"{folder_path} papka yaratildi.")
# else:
#     print(f"{folder_path} papka allaqachon mavjud.")

my_cwd = os.getcwd()
new_dir = r"D:\Maan beqorchiman"
path = os.path.join(my_cwd, new_dir)
os.mkdir(path)
print(os.listdir())