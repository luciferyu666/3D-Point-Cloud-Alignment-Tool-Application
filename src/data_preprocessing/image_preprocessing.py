import cv2
import numpy as np

def adjust_brightness(image, value=30):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return image

def denoise_image(image, filter_strength=10):
    return cv2.fastNlMeansDenoisingColored(image, None, filter_strength, filter_strength, 7, 21)

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = adjust_brightness(image)
    image = denoise_image(image)
    return image
