# Copyright (c) 2019 Ramy Zeineldin
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#|<------------Dependencies---------->|
# python 3.7
# keras 2.6.0
# keras-Applications 1.0.8
# keras-Preprocessing 1.1.2
# tensorflow 2.6.0
# tensorflow-gpu 2.6.0
# tensorflow-gpu-estimator 2.3.0
# tensorflow-estimator 2.6.0
# h5py 3.1.0
# imgaug 0.4.0
# opencv-python 4.5.3.56
# numpy 1.18.5
# nipype 1.6.1
# nibabel 3.2.1
# CUDA 11.2
# cuDNN 8.1

import numpy as np
import glob, os
import itertools
import random
from keras.optimizers import adam_v2
from keras import backend as K

K.set_image_data_format('channels_last')
if K.image_data_format() == 'channels_first':
    IMAGE_ORDERING = 'channels_first'
elif K.image_data_format() == 'channels_last':
    IMAGE_ORDERING = 'channels_last'

config = dict()
path = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/mri-image-segmentation-using-dl-models/DeepSeg-v2/'

####### These variables should be modified to your local path #######
# dataset paths
config['brats_path'] = path+'DATASET/MICCAI_BraTS_2021_Data_Training/' # path to the original BraTS 2019
config['preprocessed_brats'] = path+'DATASET/BraTS21_train_preprocessed/' # path to the output preprocessed BraTS 2019 (after preprocess.py)
config['preprocessed_brats_imgs'] = path+'DATASET/BraTS21_train_images/' # path to the output preprocessed 2D images (after preprocess_2d_images.py)
config['dataset_path'] = path+'DATASET/dataset_brats21/' # path to the dataset containing 2d images (train_images, train_segmentation, ... etc)
#####################################################################

# model configuration
config['encoder_name'] = 'DenseNet121' # name of the encoder: UNet-Mod, VGG16, ResNet50, MobileNet, MobileNetV2, Xception, NASNetMobile, DenseNet121
config['decoder_name'] = 'UNet-Mod' # name of the decoder: UNet-Mod
config['project_name'] = config['encoder_name'] + '_' + config['decoder_name']

config['all_modalities'] = ["image_FLAIR/", "image_t1/", "image_t1ce/", "image_t2/"]
config['train_modality'] = "image_FLAIR/"
config['n_modalities'] = len(config['train_modality'])
config['label_type'] = '' # _complete, _core, _enhancing, _l1, _l2, _l3
config['train_label'] = 'truth/' + config['label_type']

config['classes'] = [0,1] # 0 for the background, 1 for the tumor
config['n_classes'] = len(config['classes'])
# default value for one modality is 3, otherwise equals the number of modalities
config['model_depth'] = 3 if config['n_modalities']==1 else config['n_modalities']
#config['up_layer'] = True # for models VGG16, ResNet50, MobileNet, MobileNetV2, Xception, NASNetMobile, DenseNet121

#config['up_layer_models'] = ["", "", "", "", ""]
config['up_layer'] = False if config['encoder_name']=="UNet" or config['encoder_name']=="UNet-Mod" or config['encoder_name']=="VGG16" else True

# paths
config['verify_dataset'] = True
config['validate'] = False # use the validation set
config['train_images'] = config['dataset_path'] + 'train_images/'
config['train_annotations'] = config['dataset_path'] + 'train_segmentation/' + config['train_label']
config['val_images'] = config['dataset_path'] + 'val_images/'
config['val_annotations'] = config['dataset_path'] + 'val_segmentation/' + config['train_label']
config['weight_dir'] = path+'weights/'
config['log_dir'] = path+'logs'
config['model_checkpoints'] = os.path.join(config['weight_dir'] + config['project_name'], config['project_name'])
config['tensorboard_path'] = path+'logs_tensor_board/' + config['project_name']

#####################################################################
### Hyper parameter: ###
config['batch_size'] = 16
config['val_batch_size'] = 16
config['filter_size'] = 32 # number of basic filters
config['optimizer_lr'] = 1e-3
config['optimizer_name'] = adam_v2.Adam(config['optimizer_lr'])
config['weights_arr'] = np.array([0.05, 1.0]) # 2 Classes
#####################################################################

# training parameters
config['input_height'] = 224 # 240, 256
config['input_width'] = 224
config['output_height'] = 224
config['output_width'] = 224
config['epochs'] = 30	# number of training epochs
config['load_model'] = False # for training --> False ||| For Predictions --> True
config['load_model_path'] = path + "paper_weights/"+config['encoder_name']+"_"+config['decoder_name']+".hdf5" # specifiy the loaded model path or None |||  if config['load_model']==False None; else pathofWeight
# config['load_model_path'] = None
# config['load_model_path'] = config['weight_dir'] + config['project_name'] + "/" + config['encoder_name']+"_"+config['decoder_name']+".001-0.00001.hdf5"

config['model_num'] = '30' # load model by the number of training epoch if config['load_model_path'] = None
config['initial_epoch'] = 0  # continue training config['model_num'] if config['load_model'] else
config['trainable'] = True # make the top layers of the model trainable or not (for transfer learning)

print(config['initial_epoch'])

config['n_train_images'] = len(glob.glob(config['train_images'] + 'image_FLAIR/*')) # 13779
config['n_valid_images'] = len(glob.glob(config['val_images'] + 'image_FLAIR/*')) # 3445
#
# config['steps_per_epoch'] = config['n_train_images'] // config['batch_size'] # 512 for fast testing
# config['validation_steps'] = config['n_valid_images'] // config['val_batch_size'] # 200 for fast testing

config['steps_per_epoch'] = 200
config['validation_steps'] = 200

# data augmentation parameters
config['do_augment'] = True
config['flip_H'] = 0.5
config['flip_V'] = 0.5
config['scale_X'] = (0.8, 1.2)
config['scale_Y'] = (0.8, 1.2)
config['translate_X'] = (-0.2, 0.2)
config['translate_Y'] = (-0.2, 0.2)
config['rotate'] = (-25, 25)
config['shear'] = (-8, 8)
config['elastic'] = (720, 24) # alpha=720, sigma=24
config['random_order'] = True # apply augmenters in random order

# prediction and evaluation
config['sample_output'] = True # show a sample output from brats_19
# config['sample_path'] = 'Brats18_TCIA08_436_1-76'   #for BraTS18
# config['sample_path'] = 'BraTS19_TCIA02_151_1-90'   #for BraTS19
# config['sample_path'] = 'BraTS20_Training_006-75'     #for BraTS20
config['sample_path'] = 'BraTS2021_01537-75'   #for BraTS21
config['pred_path'] = path+'preds/' + config['project_name'] + '/'
config['evaluate_path'] = path+'evaluations/' # + config['project_name'] + '/'
config['evaluate_val'] = True # evaluate the entire validation set
config['evaluate_val_nifti'] = False # evaluate the validation set as nifti images
config['evaluate_keras'] = True # evaluate using keras evaluate_generator()
config['save_csv'] = True # save the evaluations as .csv file
config['save_plot'] = True # save the evaluations plot
config['predict_val'] = True # predict the entire validation set
config['predict_val_nifti'] = False # save the predicted validation set as nifti images
config['pred_path_nifti_240'] = path+"preds/" +  config['project_name'] + '_nifti_240/'
config['val_cases_file'] = path+"data/valid_cases_unique.txt" # path to the validation cases file
config['valid_cases_dir'] = path+"valid_cases/"

# create folders
if not os.path.exists(config['log_dir']):
    os.mkdir(config['log_dir'])
if not os.path.exists(config['weight_dir'] + config['project_name']):
    os.makedirs(config['weight_dir'] + config['project_name'])
if not os.path.exists(config['tensorboard_path']):
    os.makedirs(config['tensorboard_path'])
if not os.path.exists(config['pred_path']):
    os.makedirs(config['pred_path'])
if not os.path.exists(config['evaluate_path']):
    os.makedirs(config['evaluate_path'])
if not os.path.exists(config['pred_path_nifti_240']):
    os.makedirs(config['pred_path_nifti_240'])

# print configs
print("\n\n####################################################################")
print("Please cite the following paper when using DeepSeg :")
print("Zeineldin, Ramy Ashraf, et al. \"DeepSeg: Deep Neural Network Framework for Automatic Brain Tumor Segmentation using Magnetic Resonance FLAIR Images. (2020)\".\n\n")

print("Project name is:", config['project_name'])
print("Dataset path:", config['dataset_path'])
print("Encoder name:", config['encoder_name'])
print("Decoder name:", config['decoder_name'])
print("Training modalities:", config['train_modality'])
print("Training classes:", config['classes'])
print("Training batch size:", config['batch_size'])
print("Validation batch size:", config['val_batch_size'])
print("####################################################################\n\n")

#<-----FOR TENSORFLOW v1------>

# # limit the GPU usage
# import tensorflow as tf
# from keras.backend.tensorflow_backend import set_session
#
# gpu_id = 0 # for multi-gpu environment
# os.environ["CUDA_VISIBLE_DEVICES"] = str(gpu_id)
# gpu_config = tf.ConfigProto(allow_soft_placement=True)
# gpu_config.gpu_options.allow_growth = True
# set_session(tf.Session(config=gpu_config))
# print(tf.test.is_gpu_available())
# print(tf.test.gpu_device_name())


#<-----FOR TENSORFLOW v2------>

# limit the GPU usage
import tensorflow as tf
tf.config.run_functions_eagerly(True)

gpu_id = 0 # for multi-gpu environment
os.environ["CUDA_VISIBLE_DEVICES"] = str(gpu_id)
gpu_config = tf.compat.v1.ConfigProto(log_device_placement=True)
gpu_config.gpu_options.allow_growth = True
K.set_session(tf.compat.v1.Session())
print(tf.test.is_gpu_available())
print(tf.test.gpu_device_name())
print(tf.config.list_physical_devices('GPU'))