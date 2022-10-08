import os, shutil


dir1 = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/mri-image-segmentation-using-dl-models/DeepSeg-v2/DATASET/BraTS21_train_preprocessed/MICCAI_BraTS_2021_Data_Training/'
dirFlair = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/mri-image-segmentation-using-dl-models/DeepSeg-v2/DATASET/BraTS21_train_preprocessed/image_flair/'
dirT1 = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/mri-image-segmentation-using-dl-models/DeepSeg-v2/DATASET/BraTS21_train_preprocessed/image_t1/'
dirT2 = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/mri-image-segmentation-using-dl-models/DeepSeg-v2/DATASET/BraTS21_train_preprocessed/image_t2/'
dirT1ce = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/mri-image-segmentation-using-dl-models/DeepSeg-v2/DATASET/BraTS21_train_preprocessed/image_t1ce/'
dirTruth = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/mri-image-segmentation-using-dl-models/DeepSeg-v2/DATASET/BraTS21_train_preprocessed/truth/'


fileformatFlair = 'flair'
fileformatT1 = 't1'
fileformatT2 = 't2'
fileformatT1ce = 't1ce'
fileformatTruth = 'truth'


for files in os.listdir(dir1):
    try:
        # print("I'm here at 22")
        dir3 = dir1+files+'/'
        for f in os.listdir(dir3):
            # print("I'm here at 25")

            # <-------- Run the program Uncommenting out only one segment at a time -------->
            # <---- Segment 1 ---->
            if fileformatFlair in f:
                # print("I'm here at 27")
                shutil.move(dir3+f, dirFlair+f)

            # <---- Segment 2 ---->
            if fileformatT1ce in f:
                # print("I'm here at 33")
                shutil.move(dir3+f, dirT1ce+f)

            # <---- Segment 3 ---->
            if fileformatT1 in f:
                print("I'm here at 28")
                shutil.move(dir3+f, dirT1+f)

            # <---- Segment 4 ---->
            if fileformatT2 in f:
                # print("I'm here at 33")
                shutil.move(dir3+f, dirT2+f)

            # <---- Segment 5 ---->
            if fileformatTruth in f:
                # print("I'm here at 33")
                shutil.move(dir3+f, dirTruth+f)

    except:
        print('Something went wrong!')
        pass


