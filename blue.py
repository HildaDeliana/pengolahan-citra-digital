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
  "Daun Pepaya": "C:\Users\user\Downloads\Daun pepaya.jpeg",
    "Daun Singkong":"C:\Users\user\Downloads\Daun singkong.jpeg",
    "Daun Kenikir": "C:\Users\user\Downloads\daun kenikir.jpeg"

for name, path in image_paths.items():
    my_image = image.imread(path)
    blue_image = blue_channel(my_image)
    display_image(blue_image, f"Saluran Biru - {name}")


for name, path in image_paths.items():
    my_image = image.imread(path)
    blue_image = blue_channel(my_image)
    display_image(blue_image, f"Saluran Biru - {name}")
