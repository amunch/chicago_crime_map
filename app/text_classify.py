import json
import pickle
import numpy as np

from keras.models import load_model
import keras.preprocessing.text as kpt

import adjust

MODEL = load_model('models/text_classification.h5')

d_fp = open('../analysis/dictionary2.json', 'r')
DICTIONARY = json.load(d_fp)
with open('../analysis/tokenizer2.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

def convert_text_to_index_array(text):
    #print(kpt.text_to_word_sequence(str(text.decode('utf-8'))))
    to_return = []
    for word in kpt.text_to_word_sequence(str(text.decode('utf-8'))):
        if word in DICTIONARY:
            to_return.append(DICTIONARY[word])

    return to_return

def classify(text, geo):
    indices = convert_text_to_index_array(text)
    indices = np.asarray([indices, [1,2]])
    #print(indices)
    model_in = tokenizer.sequences_to_matrix(indices, mode='binary')
    #print(model_in)

    prediction = MODEL.predict(model_in)
    threshold = adjust.adjust_threshold(geo)
    print(prediction)
    print(threshold)
    if prediction[0][0] > threshold:
        return 0
    else:
        return 1
