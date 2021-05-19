from keras.layers.core import Dropout
import pandas as pd
from pandas.core.frame import DataFrame
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split
import numpy as np

EPOCH = 150
BATCH_SIZE = 32


def load_csv(file_name) -> DataFrame:
    df = pd.read_csv(file_name)
    print(df)
    return df

def generate_sequential_model():
    '''
    model = Sequential()
    model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(1, activation='sigmoid'))

    # try using different optimizers and different optimizer configs
    model.compile(loss='binary_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])
    '''
    model = Sequential()
    model.add(LSTM(units=256,return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=128,return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=64,return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))

    model.compile(optimizer='adam',loss='mean_squared_error')
    
    return model

df = load_csv('examples/XOM_2010_with_nyse_TA_wti_nlp.csv')
print("Data Frame Shape : " + str(df.shape))
x_train, x_test, y_train, y_test = train_test_split(
		df.drop(labels=['date', 'open', 'high', 'low', 'close', 'volume'], axis='columns'),
		df['close'],
		test_size=0.33,
		random_state=0)

# Reshape.
x_train, x_test = np.array(x_train), np.array(x_test)
print("x_train Shape : " + str(x_train.shape))
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))


y_train, y_test = np.array(y_train), np.array(y_test)
'''
y_train = np.reshape(y_train, (y_train.shape[0], y_train.shape[1], 1))
y_test = np.reshape(y_test, (y_test.shape[0], y_test.shape[1], 1))
'''

model = generate_sequential_model()

print('Train...')
model.fit(x_train, y_train,
          batch_size=BATCH_SIZE,
          epochs=EPOCH,
          validation_data=(x_test, y_test))
results = model.evaluate(x_test, y_test, batch_size=BATCH_SIZE)
print(str(results))

#print('Test score:', score)
#print('Test accuracy:', acc)

