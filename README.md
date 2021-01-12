# Machine-learning-002
ML model for classifying movie reviews trained using BERT from IMDB review dataset 
step 1 : open 'nlp_with_bert_for_sentiment_analysis.ipynb' using jupyter or google colab (best preferred)
step 2 : in order to setup google colab setup a gmail account
step 3 : start training the model by running 'nlp_with_bert_for_sentiment_analysis.ipynb' and model gets saved in  file named bert
step 4 : It takes quite sometime for the model to train ...
step 5 : now run check.py
step 6 : now say some review about a movie (time duration of 10s for recording #it can be changed)
step 7 :if you have said incorrectly press 'y' to record again or else press any other key
step 8 :after a few moments u get a voila moment of the model predicting [pos] or [neg] for movie review .

necessary packages to setup in python env :
1.ktrain 2.tensorflow 3.pandas 4.numpy

from training the model we get a value accuracy of 94% (precisely) for the IMDB reviews dataset

NOTE: if you want to test for a series of reviews then set reviews in variable called data in check.py and comment out the python audio to speech code in it
