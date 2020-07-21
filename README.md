# Fake News Classifier Web
News articles influences people's ideas and opinion on the certain topics.Misleading articles and hoax articles could trigger extreme reactions from the public.Hence,it is very important to factcheck and use reliable sources for following the latest news affairs.
This website uses an ML model to understand news articles and tries to predict if the given article is fake or not.

This model classifies news articles as fake or not using TFIDF and Logistic Regression and had a 95% accuracy when classifying dataset from kaggle.com/fake-news.
More information about the model can be found from the ***FinalProject.ipynb*** file.

##### DISCLAIMER : This model is not perfect but could aide in checking reliability of an article.
#### Dependencies
NLTK \
Sklearn \
Joblib \
Pickle \
BeautifulSoup 

#### Instructions for using the model in webpage
Clone this repository 
```
git clone https://github.com/ViharDevalla/fakenews-classifier.git
```
Install the requirement files from pip or similar 
```python
pip3 install -r requirements.txt
```
Run app.py 
```
python3 app.py
```
If ngrok doesnt work, comment it will run in localhost instead
```
#run_with_ngrok(app)
```
