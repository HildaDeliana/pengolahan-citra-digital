import numpy as np
import imageio.v3 as image
import matplotlib.pyplot as plt

def display_image(image, title):
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()

def green_channel(image):
    green_image = np.zeros_like(image)
    green_image[:, :, 1] = image[:, :, 1]  
    return green_image

image_paths = {
    "Daun Pepaya": "C:\Users\user\Downloads\Daun pepaya.jpeg",
    "Daun Singkong":"C:\Users\user\Downloads\Daun singkong.jpeg",
    "Daun Kenikir": "C:\Users\user\Downloads\daun kenikir.jpeg"
}



for name, path in image_paths.items():
    my_image = image.imread(path)
    green_image = green_channel(my_image)
    display_image(green_image, f"Saluran Hijau - {name}")
