import numpy as np
import imageio.v3 as image
import matplotlib.pyplot as plt

def display_image(image, title):
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()

def blue_channel(image):
    blue_image = np.zeros_like(image)
    blue_image[:, :, 2] = image[:, :, 2] 
    return blue_image


image_paths = {
   import numpy as np
import imageio.v3 as image
import matplotlib.pyplot as plt

def display_image(image, title):
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()

def blue_channel(image):
    blue_image = np.zeros_like(image)
    blue_image[:, :, 2] = image[:, :, 2]  
    return blue_image

image_paths = {
    "Daun Pepaya": "path/to/daun_pepaya.jpg",
    "Daun Singkong": "path/to/daun_singkong.jpg",
    "Daun Kenikir": "path/to/daun_kenikir.jpg"
}

for name, path in image_paths.items():
    my_image = image.imread(path)
    blue_image = blue_channel(my_image)
    display_image(blue_image, f"Saluran Biru - {name}")


for name, path in image_paths.items():
    my_image = image.imread(path)
    blue_image = blue_channel(my_image)
    display_image(blue_image, f"Saluran Biru - {name}")
