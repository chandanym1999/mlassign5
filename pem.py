# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 06:55:24 2020
@author: chandan Y M
DATASET:    pem
OBJECTIVE:  An attempt to identify malnutrition like IUGR , MARASMUS and KWASHIORKOR using machine learning.
STEP APPROACH:  
1.  Data collection
2.  Data interpretation
3.  Data visualization analysis
4.  Data cleaning
5.a. Create arrays
  b. Get training dataset
  c. Get testing dataset
6.  Algorithm selection
7.  Training
8.  Testing
"""
#data collection
#import libraries and dataframe
import pandas as pd
data=pd.read_csv("pem.csv")
print(data)

#data interpretation
data.describe()
data.info()
data['diagnosis'].unique()

#data visualization
import seaborn as sb
sb.heatmap(data.corr(),annot=True)

#data cleaning
data.drop('id',inplace=True,axis=1) #default: axis=0 (row)

#replace string attributes to 0, 1 and 2
classes = {'varacious':0, 'good':1, 'poor':2}  
data.replace({'appetite':classes},inplace=True) 

classes1 = {'negative':0, 'present':1}  
data.replace({'edema':classes1},inplace=True) 

classes2 = {'dry_scaly':0, 'dermatosis':1, 'no':2}  
data.replace({'skin_changes':classes2},inplace=True) 

classes3 = {'no':0, 'irritable':1, 'lethargic':2}  
data.replace({'phychomotor_changes':classes3},inplace=True) 

classes4= {'normal':0, 'distended':1}  
data.replace({'abdomen':classes4},inplace=True) 

classes5 = {'no':0, 'yes':1}  
data.replace({'organomegaly':classes5},inplace=True) 

classes6 = {'IUGR':0, 'marasmus':1,'kwashiorkor':2}  
data.replace({'diagnosis':classes6},inplace=True)
print(data)
 

#Create arrays 
'''
data.columns
x=data[['age_inmonths', 'birth_weight', 'appetite', 'edema',
       'skin_changes', 'phychomotor_changes', 'serum_albumin_level', 'abdomen',
       'organomegaly', 'subcutaneous_fat', 'present_weight']]
y=['diagnosis']
'''
x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

#Split universal dataset (train:test)
#Library: sklearn
#module : model_selection
#class  : train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( x, y, test_size=0.3, random_state=42)

#Algorithm selection
#Logistic regression
#Library: sklearn
#module : linear_model
#class  : LogisticRegression
from sklearn.linear_model import LogisticRegression
LR = LogisticRegression()

#train the model
LR.fit(X_train,y_train)

#test the model
y_p = LR.predict(X_test)

#Check accuracy by giving x_test and y_test data
#Use score(x_test, y_test)
accuracy=LR.score(X_test,y_test)
print("Accuracy: ", accuracy)

#Confusion matrix: tells right and wrong predictions
#Library: sklearn
#module : metrics
#class  : confusion_matrix
#Use confusion_matrix(actual,predicted)
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_p)
print("Confusion Matrix:")
print(confusion_matrix)

#check for new entries
print("Enter the new values of the individual")
age_inmonths=float(input("Enter the age_inmonths: "))
birth_weight=float(input("Enter the birth_weight: "))
appetite=int(input("Enter the appetite('varacious':0, 'good':1, 'poor':2): "))
edema=int(input("Enter the edema('negative':0, 'present':1): "))
skin_changes=int(input("Enter the skin_changes('dry_scaly':0, 'dermatosis':1, 'no':2): "))
phychomotor_changes=int(input("Enter the phychomotor_changes('no':0, 'irritable':1, 'lethargic':2): "))
serum_albumin_level=float(input("Enter the serum_albumin_level: "))
abdomen=int(input("Enter the abdomen('normal':0, 'distended':1): "))
organomegaly=int(input("Enter the organomegaly('no':0, 'yes':1): "))
subcutaneous_fat=float(input("Enter the subcutaneous_fat: "))
present_weight=float(input("Enter the present_weight: "))
a=[[age_inmonths, birth_weight, appetite, edema,
       skin_changes, phychomotor_changes, serum_albumin_level, abdomen,
       organomegaly, subcutaneous_fat, present_weight]]
y_pred=LR.predict(a)
print()
print("The diagnosis is('IUGR':0, 'marasmus':1, 'kwashiorkor':2) :", y_pred)
