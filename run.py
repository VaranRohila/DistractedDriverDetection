import numpy as np 
import pickle
import datetime
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

from keras.utils import to_categorical


from keras.layers.normalization import BatchNormalization
from keras.optimizers import Adam
from keras.optimizers import SGD
from keras.utils import np_utils
from keras.models import model_from_json
# from sklearn.metrics import log_loss
from numpy.random import permutation

import keras
import keras.backend as K 
from keras.models import Model
from keras.layers import Dense, Dropout, Add, Input, BatchNormalization, Activation
from keras.layers import  Conv2D, MaxPooling2D, AveragePooling2D, Flatten
from keras.regularizers import l2

import cv2
import matplotlib.pyplot as plt
import glob

import os
# Any results you write to the current directory are saved as output.

img_rows = 224
img_cols = 224

def load_image(path, rows=None, cols=None, gray=True):
    if gray:
        img = cv2.imread(path,0)
    else:
        img = cv2.imread(path)
    if rows != None and cols != None:
        img = cv2.resize(img,(rows,cols))
        #img = np.reshape(img, (rows, cols,1))
    return img

def load_model():
	# load json and create model
	json_file = open('Model/model.json', 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	# load weights into new model
	loaded_model.load_weights("Model/weights.h5")
	print("Loaded model from disk")
	return loaded_model

def classifier(pred):
	arg = np.argmax(pred)
	return ('c'+str(arg))

if __name__ == '__main__':
	model = load_model()
	image = load_image("image_path.jpg", rows=img_rows, cols=img_cols, gray=False)
	pred = model.predict(image)
	print("Predicted Class: "+classifier(pred))






