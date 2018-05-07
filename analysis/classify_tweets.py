import json
import keras
import keras.preprocessing.text as kpt
from keras.preprocessing.text import Tokenizer
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

import adjust

import pickle
import sys


seed = 16
np.random.seed(seed)

x = []
y = []

geo = []
for line in open('../data/crime_geo.txt'):
    stripped = line.strip().split('\'')
    geo.append((stripped[1], stripped[3]))

for line in open('../data/crime_text.txt'):
    x.append(line.strip())
    y.append(1)

num_train = len(x)
 
count = 0
for line in open('../data/noncrime_geo.txt'):
    stripped = line.strip().split('\'')
    geo.append((stripped[1], stripped[3]))
    count += 1
    if count > num_train:
        break

count = 0
for line in open('../data/noncrime_text.txt'):
    x.append(line.strip())
    y.append(0)
    count += 1
    if count > num_train:
        break

x_df = pd.DataFrame(x, columns=['text'])
y_df = pd.Series(y)

# Split the data into training and testing data.
x_train, x_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.2)

max_words = 10000

tokenizer = Tokenizer(num_words=max_words)
# feed our tweets to the Tokenizer

x_train = x_train['text']

tokenizer.fit_on_texts(x_train)

with open('tokenizer2.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

dictionary = tokenizer.word_index

with open('dictionary2.json', 'w') as dictionary_file:
    json.dump(dictionary, dictionary_file)

def convert_text_to_index_array(text):
    # one really important thing that `text_to_word_sequence` does
    # is make all texts the same length -- in this case, the length
    # of the longest text in the set.
    return [dictionary[word] for word in kpt.text_to_word_sequence(text)]

allWordIndices = []
# for each tweet, change each token to its ID in the Tokenizer's word_index
for text in x_train:
    wordIndices = convert_text_to_index_array(text)
    allWordIndices.append(wordIndices)

allWordIndices = np.asarray(allWordIndices)

# create one-hot matrices out of the indexed tweets
train_x = tokenizer.sequences_to_matrix(allWordIndices, mode='binary')
# treat the labels as categories
train_y = keras.utils.to_categorical(y_train, 2)

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation

model = Sequential()
model.add(Dense(512, input_shape=(max_words,), activation='relu'))
model.add(Dropout(0.5))
#model.add(Dense(256, activation='sigmoid'))
#model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))

model.compile(loss='categorical_crossentropy',
  optimizer='adam',
  metrics=['accuracy'])

model.fit(train_x, train_y,
  batch_size=32,
  epochs=10,
  verbose=1,
  shuffle=True)

model.save('../app/models/text_classification.h5')

# Test the model and adjust the threshold.

def convert_text_to_index_2(text):
    to_return = []
    for word in kpt.text_to_word_sequence(text):
        if word in dictionary:
            to_return.append(dictionary[word])

    return to_return

count = 0

correct = 0
incorrect = 0

print('Testing Model without adjustment...')

for i, row in x_test.iterrows():
    indices = convert_text_to_index_2(row['text'])
    indices = np.asarray([indices, [1,2]])
    try:
        model_in = tokenizer.sequences_to_matrix(indices, mode='binary')
    except:
        continue
    
    count += 1

    prediction = model.predict(model_in)
    threshold = 0.5
    if prediction[0][0] > threshold:
        if y_test[i] == 0:
            correct += 1
        else:
            incorrect += 1
    else:
        if y_test[i] == 1:
            correct += 1
        else:
            incorrect += 1

print(count, correct/count, incorrect/count)

print('Testing model with location adjustment...')

count = 0
correct = 0
incorrect = 0

for i, row in x_test.iterrows():
    indices = convert_text_to_index_2(row['text'])
    indices = np.asarray([indices, [1,2]])
    try:
        model_in = tokenizer.sequences_to_matrix(indices, mode='binary')
    except:
        continue
    
    count += 1

    prediction = model.predict(model_in)
    threshold = adjust.adjust_threshold(geo[i])
    if prediction[0][0] > threshold:
        if y_test[i] == 0:
            correct += 1
        else:
            incorrect += 1
    else:
        if y_test[i] == 1:
            correct += 1
        else:
            incorrect += 1

print(count, correct/count, incorrect/count)
