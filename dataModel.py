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

from sklearn.preprocessing import LabelEncoder

# creating instance of labelencode
labelencoder = LabelEncoder()
# Encoding text variables into numerical
cars['Gorivo'] = labelencoder.fit_transform(cars['Gorivo'])
cars['Karoserija']  = labelencoder.fit_transform(cars['Karoserija'])

# Encoded labels show
le_name_mapping = dict(zip(labelencoder.classes_, labelencoder.transform(labelencoder.classes_)))
df = pd.DataFrame.from_dict(le_name_mapping, orient='index')
df

# Import LR model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import pickle

def get_models():
    
    # Group cars by brand
    brands = cars.groupby('Brend')

    # Iterate through each brand and model
    for b, items in brands:
        #print("Brand: {}".format(b))
        model = items.groupby('Model')
        for m, items in  model:
            #print("Model: {}".format(m))
            model_m = cars[cars['Model']==m]
            X = model_m[['Godiste', 'Gorivo', 'Karoserija', 'Kilometraza', 'Kubikaza', 'Snaga']]
            y = model_m[['Cena']]
            
            ml_model = [linear_model,decision_tree_model, random_forest_model, ridge_model]
            
            for func in ml_model:
                y_test, predictions = func(b,m,X,y)

                # Plot ral and predicted values
                fig, ax = plt.subplots()
                ax.scatter(y_test, predictions, edgecolors=(1, 0, 0))
                ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
                ax.set_xlabel('Real values')
                ax.set_ylabel('Predicted')
                ax.set_title("Brend: {} Model: {} ML: {}".format(b,m, func))
                plt.show()
            


def model_metrics(y_test,predictions):
    mae = metrics.mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(metrics.mean_squared_error(y_test,predictions))
    r2 = metrics.r2_score(y_test,predictions)
    print("Mae is: {}".format(mae))
    print("RMSE is: {}".format(rmse))
    print("R2 score is: {}".format(r2))

def save_model(b, m, model, directory):
    # Save ML model
    directory = '\\path_to_models\\' + directory + '\\'
    file_name = directory + '' + b+ '_' +m + '_L'+'.pkl'
    with open(file_name, 'wb') as file:  
        pickle.dump(model, file)

def linear_model(b, m, X, y):
    # Split the data into train/test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    lm = LinearRegression()
    lm.fit(X_train,y_train)
    # Predictions
    predictions = lm.predict(X_test)
    
    # Print metrics
    model_metrics(y_test, predictions)
    
    # Save model
    directory = 'LinearModels'
    save_model(b, m, lm, directory)
    
    return y_test, predictions
    
def decision_tree_model(b, m, X, y):
    # Split the data into train/test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)        
    dtree = DecisionTreeClassifier()
    dtree.fit(X_train,y_train)
    
    # Predictions
    predictions = dtree.predict(X_test)
    
    # Print metrics
    model_metrics(y_test, predictions)
    
    # Save model
    directory = 'DecisionTreeModels'
    save_model(b, m, dtree, directory)
    
    return y_test, predictions
        
def random_forest_model(b, m, X, y):
    # Split the data into train/test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    rfc = RandomForestClassifier(n_estimators=100)
    rfc.fit(X_train, y_train.values.ravel())
      
    # Predictions
    predictions = rfc.predict(X_test)
    # Print metrics
    model_metrics(y_test, predictions)

    # Save model
    directory = 'RandomForestModels'
    save_model(b, m, rfc, directory)
    
    return y_test, predictions

def ridge_model(b, m, X, y):
    # Split the data into train/test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    ridge = Ridge(alpha=2)
    ridge.fit(X_train,y_train)
      
    # Predictions
    predictions = ridge.predict(X_test)
    
    # Print metrics
    model_metrics(y_test, predictions)

    # Save model
    directory = 'RidgeModels'
    save_model(b, m, ridge, directory)
    
    return y_test, predictions
        


if __name__=="__main__":

   get_models()
   # Load model
   file_model = str(input('Enter path and model: '))
   with open(file_model, 'rb') as file:  
       car = pickle.load(file)

   # Model prediction for single feature
   parameters = [int(input('Enter path and model: '))]
   car.predict([parameters])



