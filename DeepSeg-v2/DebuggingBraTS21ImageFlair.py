import os,shutil
from tqdm import tqdm

dirF = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/mri-image-segmentation-using-dl-models/DeepSeg-v2/DATASET/dataset_brats21/val_images/image_FLAIR/'
dirT = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/mri-image-segmentation-using-dl-models/DeepSeg-v2/DATASET/dataset_brats21/val_images/image_t1/'

for files in tqdm(os.listdir(dirF)):
    flag = 0
    for fileT in tqdm(os.listdir(dirT)):
        if(files == fileT):
            flag = 1;
    if(flag == 0):
        print(files)
        break;

