import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:,3:13].values
y = dataset.iloc[:,13].values

#encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
label_encoder_X_1 = LabelEncoder()
X[:, 1] = label_encoder_X_1.fit_transform(X[:,1])
label_encoder_X_2 = LabelEncoder()
X[:, 2] =label_encoder_X_2.fit_transform(X[:,2]) 
onehotencoder = OneHotEncoder(categorical_features=[1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_train)

#Making the ANN
import keras
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

#adding the input layer and the first hidden layer
classifier.add(Dense(output_dim = 6, init='uniform',activation='relu', input_dim=11))

classifier.add(Dense(output_dim=6, init='uniform',activation='relu'))
#Out put layer
classifier.add(Dense(output_dim =1, init='uniform',activation='sigmoid'))

classifier.compile(optimizer='adam', loss ='binary_crossentropy', metrics=['accuracy'])

classifier.fit(X_train, y_train, batch_size=10, nb_epoch=100)
# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)