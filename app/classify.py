import json
import pickle
import numpy as np

import adjust

from keras.models import load_model
import keras.preprocessing.text as kpt

MODEL = load_model('models/text_classification.h5')

d_fp = open('../analysis/dictionary2.json', 'r')
DICTIONARY = json.load(d_fp)
with open('../analysis/tokenizer2.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

def convert_text_to_index_array(text):
    return [DICTIONARY[word] for word in kpt.text_to_word_sequence(text)]

def classify(text, geo):
    indices = convert_text_to_index_array(text)
    indices = np.asarray(indices)
    model_in = tokenizer.sequences_to_matrix(indices, mode='binary')

    prediction = MODEL.predict(model_in)
    threshold = adjust.adjust_threshold(geo)
    if prediction[0][0] > thresh:
        return 0
    else:
        return 1
