# Splitting Files

import splitfolders  # or import split_folders

input_folder = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/mri-image-segmentation-using-dl-models/DeepSeg-v2/DATASET/dataset_brats21/'
output_folder = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/mri-image-segmentation-using-dl-models/DeepSeg-v2/DATASET/dataset_brats21/val/'
# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
splitfolders.ratio(input_folder, output=output_folder, seed=42, ratio=(.75, .25), group_prefix=None)
