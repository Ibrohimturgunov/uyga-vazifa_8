import shutil
import os


manba_papka = r"D:\Men_bekorchiman"


maqsad_papka = r"D:\Sen_bekorchiman"


if not os.path.exists(maqsad_papka):
    os.makedirs(maqsad_papka)

shutil.copytree(manba_papka, os.path.join(maqsad_papka, os.path.basename(manba_papka)))

print(f"{manba_papka} papkasi muvaffaqiyatli nusxalandi {maqsad_papka} ga.")
