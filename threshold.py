import numpy as np
import imageio
import matplotlib.pyplot as plt


def convert_to_binary(image_path, threshold=128):
    
    image = imageio.imread(image_path)
    
    gray_image = 0.299 * image[:,:,0] + 0.587 * image[:,:,1] + 0.114 * image[:,:,2]
    
   
    binary_image = np.where(gray_image > threshold, 255, 0)
    
    
    binary_image = binary_image.astype(np.uint8)
    
    return binary_image


image_files = {
    "Daun Pepaya": "C:\Users\user\Downloads\Daun pepaya.jpeg",
    "Daun Singkong": "C:\Users\user\Downloads\Daun singkong.jpeg",
    "Daun Kenikir": "C:\Users\user\Downloads\daun kenikir.jpeg"
}


for name, file in image_files.items():
    binary_image = convert_to_binary(file)
    
    
    plt.imshow(binary_image, cmap='gray')
    plt.title(name)
    plt.axis('off')
    plt.show()
