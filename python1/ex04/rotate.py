import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def transpose_array(arr: np.ndarray) -> np.ndarray:
    """Takes a numpy array and transposes it before returning it"""

    h, w, d = arr.shape
    new_arr = np.zeros((w, h), int)
    for i in range(w):
        for j in range(h):
            new_arr[i, j] = arr[j, i, 0]
    return new_arr


def main():
    """Loads the animal.jpeg image, slices it, prints information about it
    and opens a transposed version"""

    img_array = np.array(ft_load("animal.jpeg"))
    if not (img_array.ndim and img_array.size):
        exit(0)

    sliced_array = img_array[100:500, 450:850, 0:1]
    print(f"The shape of image is: {sliced_array.shape} ", end='')
    h, w, d = sliced_array.shape
    print(f"or ({h}, {w})")
    print(sliced_array)

    trans_array = transpose_array(sliced_array)
    print(f"New shape after Transpose: {trans_array.shape}")
    print(trans_array)

    plt.imshow(trans_array, cmap='gray')
    plt.axis('on')
    plt.show()


if __name__ == "__main__":
    main()
