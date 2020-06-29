import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn import tree
from pandas import DataFrame as df

home_data= pd.read_csv("home_original.csv", delimiter= ",") 
Y_data= home_data['House']  

real_model = DecisionTreeClassifier(criterion= 'entropy', random_state= 123)
real_model.fit(X_data, Y_data)

x1=input('Sound: ')
x2=input('friend:')
x3=input('idol: ')
x4=input('ability: ')
x5=input('clothing: ')
x6=input('halloween: ')
x7=input('weather: ')
x8=input('money: ')
x9=input('ghost: ')

df1=df(data={'Sound':[x1],'friend':[x2],'idol':[x3],'ability':[x4],'clothing':[x5],'halloween':[x6],'weather':[x7],'money':[x8],'ghost':[x9]})



Y_pred= real_model.predict(df1) 
