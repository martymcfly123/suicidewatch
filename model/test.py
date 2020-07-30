from fastai.text import *

learn2 = load_learner(".")

def handle_input(text):
  return learn2.predict(text)
