import numpy as np
import imageio
import matplotlib.pyplot as plt

def display_image(image, title):
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()

def red_channel(image):
    red_image = np.zeros_like(image)
    red_image[:, :, 0] = image[:, :, 0]
    return red_image

image_paths = {
    "Daun Pepaya": "C:\Users\user\Downloads\Daun pepaya.jpeg",
    "Daun Singkong":"C:\Users\user\Downloads\Daun singkong.jpeg",
    "Daun Kenikir": "C:\Users\user\Downloads\daun kenikir.jpeg"
}

for name, path in image_paths.items():
    image = imageio.imread(path)
    red_image = red_channel(image)
    display_image(red_image, f"Saluran Merah - {name}")
