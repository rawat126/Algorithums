import numpy as np
import cv2
import os

# Gaussian Noise Algorithum function
# image   --->   Input Data
# noise   --->   Noise ratio(to be added...) 
def gaussian_noise(image, noise):    
    typ = image.dtype

    # For GRAY-Scale Images
    if(len(image.shape)==2):
        for i in range(noise):
            val = np.random.randint(0,10,
                [image.shape[0],image.shape[1]])

        for row in range(image.shape[0]):
            for col in range(image.shape[1]):

                if val[row,col] == 0:
                    image[row,col] = 0
                
                elif val[row,col] == image[row,col]:
                    image[row,col] = 255 

    # For RGB Images   
    elif(len(image.shape) == 3):
        for i in range(noise):
            val = np.random.randint(0,10,
            [image.shape[0],image.shape[1],image.shape[2]])

        for cha in range(image.shape[2]):
            for row in range(image.shape[0]):
                for col in range(image.shape[1]):

                    if val[row,col,cha] == 0:
                        image[row,col,cha] = 0
                    
                    elif val[row,col,cha] == image[row,col,cha]:
                        image[row,col,cha] = 255
                    
    image = image.astype(typ)
    return image

# Image Data 
img = cv2.imread(r'E:\flower.png')
print(img.shape)

# Noise Image with gaussian noise 1
noisy_img_1 = gaussian_noise(img,noise = 1)

# Noise Image with gaussian noise 1
noisy_img_4 = gaussian_noise(img,noise = 4)

# Noise Image with gaussian noise 1
noisy_img_7 = gaussian_noise(img,noise = 7)

# Noise Image with gaussian noise 1
noisy_img_11 = gaussian_noise(img,noise = 11)
