import os
import numpy as np
from PIL import Image, UnidentifiedImageError


def ft_load(path: str) -> np.ndarray:
    """Takes an image file path as argument and prints its shape
    and returns an array equivalent to the image"""

    try:
        if not isinstance(path, str):
            raise AssertionError("Bad Argument")
        elif not os.path.isfile(path):
            raise AssertionError("File does not exist")
        elif not path.lower().endswith((".jpg", ".jpeg")):
            raise AssertionError("File does not have the right file extension")
        img = Image.open(path)
    except AssertionError as error:
        print("AssertionError:", error)
        return []
    except UnidentifiedImageError as error:
        print("UnidentifiedImageError:", error)
        return []

    data = np.asarray(img)
    print(f"The shape of image is: {data.shape}")
    print(data)
    return data
