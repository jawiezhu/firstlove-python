# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 17:10:03 2017

drop some columns
use 0 or 1 to replace the male and female


@author: jawiezhu
"""

import pandas as pd
from MultiColumnLabelEncoder import *


def add_target_column(all_df):
    survived=all_df['Survived']
    all_df.drop(labels=['Survived'],axis=1,inplace=True)
    all_df.insert(all_df.columns.size, 'target', survived)


def drop_columns(all_df):
    #    drop name columns
    all_df.drop(labels=['Name'], axis=1, inplace=True)
    # drop the column CABIN
    all_df.drop(['Cabin', 'Ticket'], axis=1, inplace=True)
    # drop the two NAN row of the Embarked
    #all_df.dropna(how='any', inplace=True)
    all_df['Embarked'].fillna(0.0, inplace=True)
    all_df['Fare'].fillna(0.0, inplace=True)


def fill_non_age(all_df):
    age_df = all_df['Age']
    age_df.sort_values(ascending=False)
    age_0_12 = 0
    age_13_18 = 0
    age_19_30 = 0
    age_31_50 = 0
    age_51 = 0
    for item in age_df:
        if 0 < item <= 12:
            age_0_12 = age_0_12 + 1
        if 12 < item <= 18:
            age_13_18 = age_13_18 + 1
        if 18< item <= 30:
            age_19_30 = age_19_30 + 1
        if 30< item <= 50:
            age_31_50 = age_31_50 + 1
        if item > 51:
            age_51 = age_51 + 1

    #   there are a lot of people in the range 18-30,and the average of the people is 23,
    #   so use the average to fill the nan
    average_age = round(age_df.sum() / age_df.index.size)
    print('Average age is :', average_age)
    all_df['Age'].fillna(average_age, inplace=True)


def label_encoder(all_df):
    all_df = MultiColumnLabelEncoder(columns=['Sex', 'Embarked']).fit_transform(all_df)
    return all_df

def preprocess_for_train_data(TRAIN_PATH, RESULT_TRAIN_PATH):
    all_df = pd.read_csv(TRAIN_PATH)
    add_target_column(all_df)
    fill_non_age(all_df)
    all_df = label_encoder(all_df)
    drop_columns(all_df)
    all_df.to_csv(RESULT_TRAIN_PATH, index=False)

def preprocess_for_test_data(TEST_PATH, RESULT_TEST_PATH):
    all_df = pd.read_csv(TEST_PATH)
    fill_non_age(all_df)
    all_df = label_encoder(all_df)
    drop_columns(all_df)
    #all_df.drop(all_df.columns[len(all_df.columns) - 1], axis=1, inplace=True)
    all_df.to_csv(RESULT_TEST_PATH, index=False)