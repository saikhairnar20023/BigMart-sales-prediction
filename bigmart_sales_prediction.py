# -*- coding: utf-8 -*-
"""BigMart Sales Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UpIS-pd-T8VrQUaX8LXHW5OrOmJK7eZW

Import Modules
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

"""Load the dataset"""

df_train = pd.read_csv("/train (2).csv")
df

df_test = pd.read_csv("/test (1).csv")
df_test

df_train.head()

df_train.tail()

df_train.describe()

df_train.info()

df_train.isnull().sum()

"""handling missing value"""

df_test.isnull().sum()

df_train['Item_Weight'].describe()

df_train['Item_Weight'].fillna(df_train['Item_Weight'].mean(),inplace=True)  #replacing null values with mean values
df_test['Item_Weight'].fillna(df_train['Item_Weight'].mean(),inplace=True)

df_train['Item_Weight'].describe()

df_train['Outlet_Size']  #it is a categorical value

df_train['Outlet_Size'].value_counts()

df_train['Outlet_Size'].mode()

df_train['Outlet_Size'].fillna(df_train['Outlet_Size'].mode()[0],inplace=True)
df_test['Outlet_Size'].fillna(df_test['Outlet_Size'].mode()[0],inplace=True)

df_train.isnull().sum()

df_test.isnull().sum()

df_train.drop(['Item_Identifier','Outlet_Identifier'],axis=1,inplace=True)
df_test.drop(['Item_Identifier','Outlet_Identifier'],axis=1,inplace=True)

df_train

df_test

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

df_train['item_fat_content']= le.fit_transform(df_train['item_fat_content'])
df_train['item_type']= le.fit_transform(df_train['item_type'])
df_train['outlet_size']= le.fit_transform(df_train['outlet_size'])
df_train['outlet_location_type']= le.fit_transform(df_train['outlet_location_type'])
df_train['outlet_type']= le.fit_transform(df_train['outlet_type'])

df_train.head(5)

X=df_train.drop('Item_Outlet_Sales',axis=1)

Y=df_train['Item_Outlet_Sales']

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, random_state=101, test_size=0.2)

X.describe()

from sklearn.preprocessing import StandardScaler
sc= StandardScaler()

X_train_std= sc.fit_transform(X_train)

X_test_std= sc.transform(X_test)

from sklearn.linear_model import LinearRegression
lr= LinearRegression()

lr.fit(X_train_std,Y_train)

Y_pred_lr=lr.predict(X_test_std)

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

0.5041875773270634

print(r2_score(Y_test,Y_pred_lr))
print(mean_absolute_error(Y_test,Y_pred_lr))
print(np.sqrt(mean_squared_error(Y_test,Y_pred_lr)))

from sklearn.ensemble import RandomForestRegressor
rf= RandomForestRegressor()

rf.fit(X_train_std,Y_train)

Y_pred_rf= rf.predict(X_test_std)

r2_score(Y_test,Y_pred_rf)

print(r2_score(Y_test,Y_pred_rf))
print(mean_absolute_error(Y_test,Y_pred_rf))
print(np.sqrt(mean_squared_error(Y_test,Y_pred_rf)))
0.5446560233468098
784.6921567153036
1113.992107139178