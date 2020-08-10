import torchvision
import requests
import torch
from torchvision import transforms
from PIL import Image
from torch import tensor

transform_image=transforms.Compose([transforms.Resize(255),
                                    transforms.CenterCrop(244),
                                    transforms.ToTensor(),
                                    transforms.Normalize([0.485, 0.456, 0.406],
                                                            [0.229, 0.224, 0.225])])

response=requests.get("https://post.healthline.com/wp-content/uploads/sites/3/2020/02/322868_1100-1100x628.jpg")
file = open("sample_image.png", "wb")
file.write(response.content)
file.close()
path="sample_image.png"
image=Image.open(path)
image_transform=transform_image(image)
print("ok")
