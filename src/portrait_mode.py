"""
Module that applies a portrait mode filter
"""
from PIL import Image, ImageDraw
import numpy as np
import face_recognition


def portrait_mode(image: Image, random_argument: bool) -> Image:
    image_np = np.asarray(image)

    faces_locations = face_recognition.face_locations(image_np)

    print(faces_locations)

    faces_images = []
    for face in faces_locations:
        top, left, bottom, right = face

        faces_images.append(image.crop((left, top, right, bottom)))

    return faces_images[0]
