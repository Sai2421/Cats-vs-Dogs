# Cats-vs-Dogs
Flask app to predict given image is a dog or cat
Project Description:
"CATS OR DOGS PREDICTOR"

Abstract:
This is a Flask based application which takes a url of an image of either a dog or cat
and is sent to a trained deeplearning model built using Pytorch and returns to front-end the
final prediction.

Explanation:
-A clean data set of cats vs dogs is selected and trained into a Jupyter Notebook using Pytorch library.
Then the trained model is serialized into a pickle file which makes it easier to deserialize into
any python application.
-PIL library is used in this project which takes any image input and converts it into numerical data
which is then transformed as per the requirements for the input to the model.
-Python requests library helps to fetch photo from its given URL.
-A flask application is developed to serve incoming requests which is the url of image and processes the 
image to model and serves the user with the final prediction.

Where to access the project?
>>Go the the site "saisaran.live" or "ec2-100-26-153-220.compute-1.amazonaws.com" and paste any dog or cat's image url in the text box and click predict.

Note:The Repo doesn't contain the pkl file, please download it from the link: https://drive.google.com/file/d/1osIjz0vD6HYV46tPPTXZ6ZIwg1gPSR3U/view?usp=sharing
