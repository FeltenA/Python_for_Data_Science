import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received"""

    try:
        if not isinstance(array, np.ndarray) or not isinstance(array, list):
            AssertionError("Bad argument")
    except AssertionError as error:
        print("AssertionError:", error)
        return []
    arr = np.array(array)
    if not (arr.ndim and arr.size):
        return []

    new_arr = 255 - arr
    plt.imshow(Image.fromarray(new_arr))
    plt.axis('off')
    plt.show()
    return new_arr


def ft_red(array) -> np.ndarray:
    """Remove all colors apart from red from the image received"""

    try:
        if not isinstance(array, np.ndarray) or not isinstance(array, list):
            AssertionError("Bad argument")
    except AssertionError as error:
        print("AssertionError:", error)
        return []
    arr = np.array(array)
    if not (arr.ndim and arr.size):
        return []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j][1] = 0
            arr[i][j][2] = 0
    plt.imshow(Image.fromarray(arr))
    plt.axis('off')
    plt.show()
    return arr


def ft_green(array) -> np.ndarray:
    """Remove all colors apart from green from the image received"""

    try:
        if not isinstance(array, np.ndarray) or not isinstance(array, list):
            AssertionError("Bad argument")
    except AssertionError as error:
        print("AssertionError:", error)
        return []
    arr = np.array(array)
    if not (arr.ndim and arr.size):
        return []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j][0] = 0
            arr[i][j][2] = 0
    plt.imshow(Image.fromarray(arr))
    plt.axis('off')
    plt.show()
    return arr


def ft_blue(array) -> np.ndarray:
    """Remove all colors apart from blue from the image received"""

    try:
        if not isinstance(array, np.ndarray) or not isinstance(array, list):
            AssertionError("Bad argument")
    except AssertionError as error:
        print("AssertionError:", error)
        return []
    arr = np.array(array)
    if not (arr.ndim and arr.size):
        return []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j][0] = 0
            arr[i][j][1] = 0
    plt.imshow(Image.fromarray(arr))
    plt.axis('off')
    plt.show()
    return arr


def add_values(a, b, c: float) -> float:
    return a + b + c


def ft_grey(array) -> np.ndarray:
    """Apply a greyscale to the image received"""

    try:
        if not isinstance(array, np.ndarray) or not isinstance(array, list):
            AssertionError("Bad argument")
    except AssertionError as error:
        print("AssertionError:", error)
        return []
    arr = np.array(array)
    if not (arr.ndim and arr.size):
        return []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            val = add_values(arr[i][j][0] / (1000 / 299),
                             arr[i][j][1] / (1000 / 587),
                             arr[i][j][2] / (1000 / 114))
            arr[i][j][0] = arr[i][j][1] = arr[i][j][2] = val
    plt.imshow(Image.fromarray(arr))
    plt.axis('off')
    plt.show()
    return arr
