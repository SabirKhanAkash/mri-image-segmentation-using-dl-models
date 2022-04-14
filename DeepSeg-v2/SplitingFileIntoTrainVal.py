# Splitting Files

import splitfolders  # or import split_folders

input_folder = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/DeepSeg/DATASET/dataset_brats18/'
output_folder = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/DeepSeg/DATASET/dataset_brats18/val/'
# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
splitfolders.ratio(input_folder, output=output_folder, seed=42, ratio=(.75, .25), group_prefix=None)
