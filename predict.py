#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri sept 23 18:45:05 2020

@author: mahim
"""

import numpy as np
from keras.models import load_model
from keras.preprocessing import image

class dogcat:
    def __init__(self,filename):
        self.filename =filename


    def predictiondogcat(self):
        # load model
        model = load_model('model2.h5')

        # summarize model
        #model.summary()
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)

        if result[0][0] == 1:
            prediction = 'Airplane'
            return [{ "image" : prediction}]
        if result[0][1] >= 0.5:
            prediction = 'Bicycle'
            return [{ "image" : prediction}]
        if result[0][2] >= 0.5:
            prediction = 'Car'
            return [{ "image" : prediction}]
        if result[0][3] >= 0.5:
            prediction = 'Helicopter'
            return [{ "image" : prediction}]
        if result[0][4] >= 0.5:
            prediction = 'Scooter'
            return [{ "image" : prediction}]
        if result[0][5] >= 0.5:
            prediction = 'Yacth'
            return [{ "image" : prediction}]