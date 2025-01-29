from deepface import DeepFace
import cv2
import numpy as np

def verify_face(img1_path, img2_path):
    try:
        result = DeepFace.verify(img1_path, img2_path, model_name='VGG-Face')
        return result["verified"]
    except Exception as e:
        return False
