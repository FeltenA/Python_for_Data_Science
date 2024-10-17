from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """Loads the animal.jpeg image, prints information about it
    and opens a zoomed version"""

    img_array = ft_load("animal.jpeg")
    if not len(img_array):
        exit(0)
    print(img_array)

    sliced_array = img_array[100:500, 450:850, 0:1]
    print(f"New shape after slicing: {sliced_array.shape} ", end='')
    h, w, d = sliced_array.shape
    print(f"or ({h}, {w})")
    print(sliced_array)

    plt.imshow(sliced_array, cmap='gray')
    plt.axis('on')
    plt.show()


if __name__ == "__main__":
    main()
