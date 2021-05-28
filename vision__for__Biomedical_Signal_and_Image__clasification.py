# -*- coding: utf-8 -*-
"""vision_ for_ Voice _clasification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uzGiW96v4cdqWRGZrd1o_lti353CIJh5
"""

!pip install tensorflow-addons==0.12

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]="2"
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from model import VisionTransformer

"""
import vision transformer
num_layers=12, # 8, number of encoder Transformer
d_model=512, # 64,embedding dimension for multi head attension
"""
img_height = 128
img_width = 128
batch_size =32

model = VisionTransformer(
        image_size=128,
        patch_size=32, # 16
        num_layers=12, 
        num_classes=4,
        d_model=512, 
        num_heads=16,
        mlp_dim=1024,
        channels=3,
        dropout=0.1,
    )

"""**First method  to import custom Dataset**"""

#Using dataset_from_directory

ds_train = tf.keras.preprocessing.image_dataset_from_directory(
    '/content/drive/MyDrive/Vision-Transformer-main/vision-transformer-master/To mike Gen/Generated 128x128x3/OS8',
    labels='inferred',
    label_mode = "int",
    color_mode='rgb',
    batch_size=batch_size,
    image_size=(img_height, img_width),
    shuffle = True,
    seed =124,
    validation_split=0.20,
    subset="training"   
)


ds_validation = tf.keras.preprocessing.image_dataset_from_directory(
    '/content/drive/MyDrive/Vision-Transformer-main/vision-transformer-master/To mike Gen/Generated 128x128x3/OS8',
    labels='inferred',
    label_mode = "int",
    color_mode='rgb',
    batch_size=batch_size,
    image_size=(img_height, img_width),
    shuffle = True,
    seed =124,
    validation_split=0.20,
    subset="validation",
)

# ImageDataGenerator and flow_from_ directory
datagen = ImageDataGenerator(
    rescale = 1./255,
    dtype = tf.float32,
    validation_split = 0.20,
    )
train_generator = datagen.flow_from_directory(
    '/content/drive/MyDrive/Vision-Transformer-main/vision-transformer-master/To mike Gen/Generated 128x128x3/OS8',
    target_size = (img_height, img_width),
    batch_size = batch_size,
    color_mode='rgb',
    class_mode ='sparse',
    shuffle=True, 
    validation_split = 0.20,
    subset = 'training',
    seed = 123,

)

datagen2 = ImageDataGenerator(
    rescale = 1./255,
)
validation_generator = datagen2.flow_from_directory(
    '/content/drive/MyDrive/Vision-Transformer-main/vision-transformer-master/To mike Gen/Generated 128x128x3/OS8',
    target_size = (img_height, img_width),
    batch_size = batch_size,
    color_mode='rgb',
    class_mode ='sparse',
    shuffle=True,
    validation_split = 0.20,
    subset = 'validation',
    seed = 123,
)

len(ds_validation)

"""**Second method to Import custom Dataset**"""

import tensorflow_addons as tfa
model.compile(
        loss=tf.keras.losses.SparseCategoricalCrossentropy(
            from_logits=True
        ),
        optimizer=tfa.optimizers.AdamW(
            learning_rate=3e-4, weight_decay=1e-4
        ),
        metrics=["accuracy"],
    )

model.fit(
    train_generator,
    validation_data=validation_generator,

    epochs=100,
    # verbose=2,

)

import tensorflow_addons as tfa
model.compile(
        loss=tf.keras.losses.SparseCategoricalCrossentropy(
            from_logits=True
        ),
        optimizer=tfa.optimizers.AdamW(
            learning_rate=3e-4, weight_decay=1e-4
        ),
        metrics=["accuracy"],
    )

model.fit(
    ds_train,
    validation_data=ds_validation,
    epochs=100,
    verbose=2,

)

