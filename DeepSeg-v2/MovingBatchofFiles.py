import os,shutil
from tqdm import tqdm

src = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/DeepSeg/DATASET/BraTS18_train_images/image_t1ce/'
dest = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/DeepSeg/DATASET/dataset_brats18/image_t1ce/'

for files in tqdm(os.listdir(src)):
    try:
        dir3 = src+files+'/'
        for f in os.listdir(dir3):
            shutil.move(dir3+f,dest+f)

    except:
        print('Something went wrong!')
        pass
