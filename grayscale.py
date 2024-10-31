import numpy as np
import imageio
import matplotlib.pyplot as plt


def convert_to_grayscale(image_path):
    
    image = imageio.imread(image_path)
    
    gray_image = 0.299 * image[:,:,0] + 0.587 * image[:,:,1] + 0.114 * image[:,:,2]
    

    gray_image = gray_image.astype(np.uint8)
    
    return gray_image


image_files = {
    "Daun Pepaya": "C:\Users\user\Downloads\Daun pepaya.jpeg",
    "Daun Singkong": "C:\Users\user\Downloads\Daun singkong.jpeg",
    "Daun Kenikir": "C:\Users\user\Downloads\daun kenikir.jpeg"
}


for name, file in image_files.items():
    gray_image = convert_to_grayscale(file)
    
    
    plt.imshow(gray_image, cmap='gray')
    plt.title(name)
    plt.axis('off')
    plt.show()
