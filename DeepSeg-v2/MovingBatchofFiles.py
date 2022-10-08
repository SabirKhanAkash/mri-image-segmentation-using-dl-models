import os,shutil
from tqdm import tqdm

src = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/mri-image-segmentation-using-dl-models/DeepSeg-v2/DATASET/BraTS21_train_images/truth/'
dest = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/mri-image-segmentation-using-dl-models/DeepSeg-v2/DATASET/dataset_brats21/truth/'

for files in tqdm(os.listdir(src)):
    try:
        dir3 = src+files+'/'
        for f in os.listdir(dir3):
            shutil.move(dir3+f,dest+f)

    except:
        print('Something went wrong!')
        pass
