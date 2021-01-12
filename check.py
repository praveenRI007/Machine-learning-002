import tensorflow as tf
import pandas as pd
import numpy as np
import ktrain
from ktrain import text
import tensorflow as tf
import speech_recognition as sr 
r = sr.Recognizer()


##data = ['this movie was horrible, the plot was really boring. acting was okay',
##        'the fild is really sucked. there is not plot and acting was bad',
##        'what a beautiful movie. great plot. acting was good. will see it again']

while True:
    with sr.Microphone() as source:
        print("recording now...")
        audio_data = r.record(source, duration=10)
        print("Recognizing...")
        text = r.recognize_google(audio_data)
        print(text) 
    # read the audio data from the default microphone
    # convert speech to text
    if (input("if text not correct then press 'y' to record  again ")=='y'):
        continue
    else:
        data = []
        data.append(text)
        print(data)
        break
    
predictor_load = ktrain.load_predictor('bert')


print(predictor_load.predict(data))
