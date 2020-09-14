# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:11:49 2020

@author: Vukašin Vasiljević
"""

# Training a Linear Regression Model

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Load data
cars = pd.read_csv('used_carsCleaned.csv')
# Swap columns
columns = ['Brend', 'Model', 'Godiste', 'Gorivo', 'Karoserija', 'Kilometraza',
       'Kubikaza', 'Snaga',  'Naziv', 'Cena']
cars = cars.reindex(columns=columns)

# Import sklearn libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# creating instance of labelencode
labelencoder = LabelEncoder()
# Encoding text variables into numerical
cars['Gorivo'] = labelencoder.fit_transform(cars['Gorivo'])
cars['Karoserija']  = labelencoder.fit_transform(cars['Karoserija'])

# Import LR model
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pickle

# Group cars by brand
brands = cars.groupby('Brend')

row_list=[]
# Iterate through each brand and model
for b, items in brands:
    #print("Brand: {}".format(b))
    model = items.groupby('Model')
    for m, items in  model:
        #print("Model: {}".format(m))
        model_m = cars[cars['Model']==m]
        X = model_m[['Godiste', 'Gorivo', 'Karoserija', 'Kilometraza', 'Kubikaza', 'Snaga']]
        y = model_m[['Cena']]
        
        # Split the data into train/test data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
        lm = LinearRegression()
        lm.fit(X_train,y_train) # Fit the data into Linear Regression model
       
        # Predictions
        predictions = lm.predict(X_test)
        
        # Save ML model
        #directory = "C:\Users\HP\Documents\Diplomski\Models"
        file_name = r"C:\Users\HP\Documents\Diplomski\Models\ " + b + "_" + m+ ".pkl"
        with open(file_name, 'wb') as file:  
            pickle.dump(lm, file)
            
        # Append errors to new dataframe for further analysis
        dict_ = {'Brand':b,'Model':m,'MAE':metrics.mean_absolute_error(y_test, predictions),'MSE':metrics.mean_squared_error(y_test, predictions),'RMSE':np.sqrt(metrics.mean_squared_error(y_test, predictions))}
        row_list.append(dict_)
        
        # Plot predictions and test data if Mean Absolute Error is equal or lower than price mean of the model
        if metrics.mean_absolute_error(y_test, predictions)<=cars[cars['Model']==m]['Cena'].mean() and metrics.mean_absolute_error(y_test, predictions)>0:
            plt.figure()
            plt.scatter(y_test,predictions,color='g')
            plt.xlabel('Y test')
            plt.ylabel('Predicted')
            plt.title('Brand: {} Model: {}'.format(b,m))
            

errors = pd.DataFrame(row_list)


# MSE Distribution
sns.distplot(errors['MSE'], bins=15)

# Load model
file_model = ""
with open(file_model, 'rb') as file:  
    car = pickle.load(file)

score = car.score(X_test, y_test) 
print("Test score: {0:.2f} %".format(100 * score))  

# Model prediction for single feature
parameters=[]
car.predict([parameters])



