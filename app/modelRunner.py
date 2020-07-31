from fastai.text import *

learn2 = load_learner(".")

def model(text):
  return learn2.predict(text)
