#cats vs dogs ,, Classifier
import pickle
import torchvision
import torch
from torchvision import transforms
from PIL import Image
from torch import tensor
import requests
from flask import Flask,render_template,request
app=Flask(__name__)


def load_image(url):
    transform_image=transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(244),
                                        transforms.ToTensor(),
                                        transforms.Normalize([0.485, 0.456, 0.406],
                                                                [0.229, 0.224, 0.225])])
    response=requests.get(url)
    file = open("sample_image.png", "wb")
    file.write(response.content)
    file.close()
    path="sample_image.png"
    image=Image.open(path)
    image_transform=transform_image(image)
    input_image=image_transform.view(1,3,244,244)
    return input_image

def predict(input_image):
    with open("cpu_model.pkl","rb") as f:
        model=pickle.load(f)
    ps=torch.exp(model(input_image))
    top_k,top_class=ps.topk(1,dim=1)
    prediction_value=top_class.item()
    if prediction_value==1:
        return "Dog"
    else:
        return "Cat"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def prediction():
    if request.method=='POST':
        url=request.form['url']
        image=load_image(url)
        prediction=predict(image)
        print(prediction)
    return render_template('index.html',pred=[prediction,url])

if __name__ == '__main__':
    app.run(host="127.0.0.1",port="5000",debug=True)
    
                               




