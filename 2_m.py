import os

folder_path = r"D:\Men_bekorchiman"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"{folder_path} papka yaratildi.")
else:
    print(f"{folder_path} papka allaqachon mavjud.")

for i in range(1, 5):
    file_path = os.path.join(folder_path, f"fayl{i}.txt")
    with open(file_path, 'w') as f:
        f.write("")
    print(f"{file_path} yaratildi.")
