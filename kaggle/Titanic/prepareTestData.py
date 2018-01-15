# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 17:10:03 2017

drop some columns
use 0 or 1 to replace the male and female


@author: jawiezhu
"""

import pandas as pd

all_df=pd.read_csv(r"C:\Users\jawiezhu\Desktop\my_python\kaggle\Titanic\test.csv")
all_df.columns
all_df.shape
#==============================================================================
# Index([u'PassengerId', u'Survived', u'Pclass', u'Name', u'Sex', u'Age',
#        u'SibSp', u'Parch', u'Ticket', u'Fare', u'Cabin', u'Embarked'],
#       dtype='object')
# 
#==============================================================================
#move column['Survived'] to the last column


#drop ['Name'] 
all_df.drop(labels=['Name'],axis=1,inplace=True)

#count nan in every column
print pd.isnull(all_df).sum()
#==============================================================================
# PassengerId      0
# Pclass           0
# Sex              0
# Age            177
# SibSp            0
# Parch            0
# Ticket           0
# Fare             0
# Cabin          687
# Embarked         2
# target           0
#==============================================================================

age_df=all_df['Age']
age_df.sort_values(ascending=False)


#show the distribution of the age
age_0_12=0
age_13_18=0
age_19_30=0
age_31_50=0
age_51=0

for item in age_df:
    if item >0 and item <=12:
        age_0_12=age_0_12+1
    if item >12 and item <=18:
        age_13_18=age_13_18+1
    if item >18 and item <=30:
        age_19_30=age_19_30+1
    if item >30 and item <=50:
        age_31_50=age_31_50+1
    if item >51:
        age_51=age_51+1
        
#print age_0_12,age_13_18,age_19_30,age_31_50,age_51

#there are a lot of people in the range 18-30,and the average of the people is 23,so use the average to fill the nan

average_age=round(age_df.sum()/age_df.index.size)

print average_age
all_df['Age'].fillna(average_age,inplace=True)


average_fare=round(all_df['Fare'].sum()/all_df.index.size)
all_df['Fare'].fillna(average_fare,inplace=True)


#check the age 
#pd.isnull(all_df).sum()
#==============================================================================
# PassengerId      0
# Pclass           0
# Sex              0
# Age              0
# SibSp            0
# Parch            0
# Ticket           0
# Fare             0
# Cabin          687
# Embarked         2
# target           0
#==============================================================================


#==============================================================================
# for i in range(0,all_df.index.size):
#     if all_df['Sex'][i]=="male":
#         all_df['Sex'][i] = 0
#     if all_df['Sex'][i]=='female':
#         all_df['Sex'][i] = 1
#==============================================================================

all_df.loc[all_df['Sex']=='female','Sex']=0
all_df.loc[all_df['Sex']=='male','Sex']=1
all_df.loc[all_df['Embarked']=='Q','Embarked']=1
all_df.loc[all_df['Embarked']=='S','Embarked']=2
all_df.loc[all_df['Embarked']=='C','Embarked']=3          
print all_df


#drop the column CABIN
all_df.drop(['Cabin','Ticket'],axis=1,inplace=True)

#drop the two NAN row of the Embarked
#all_df.dropna(how='any',inplace=True)

print pd.isnull(all_df).sum()

all_df.to_csv(r"C:\Users\jawiezhu\Desktop\my_python\kaggle\Titanic\test_not_nan.csv",index=False)
