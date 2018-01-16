# -*- coding:utf-8 -*-

import numpy as np

import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, log_loss
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis


def start_to_fit(X, y):
    classifiers = [
        KNeighborsClassifier(3),
        SVC(probability=True),
        DecisionTreeClassifier(),
        RandomForestClassifier(),
        AdaBoostClassifier(),
        GradientBoostingClassifier(),
        GaussianNB(),
        LinearDiscriminantAnalysis(),
        QuadraticDiscriminantAnalysis(),
        LogisticRegression()]

    res_cols = ['Classifier','Accuracy']
    res = pd.DataFrame(columns = res_cols)

    data_set = StratifiedShuffleSplit(n_splits=10, test_size=0.3, train_size=0.7, random_state=0)

    accuracy_dic ={}


    for train_index, test_index in data_set.split(X, y):

        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        for clf in classifiers:
            name = clf.__class__.__name__
            clf.fit(X_train, y_train)
            #train_predictions = clf.predict(X_test)
            accuracy = accuracy_score(y_test, clf.predict(X_test))
            if name in accuracy_dic:
                accuracy_dic[name] += accuracy
            else:
                accuracy_dic[name] = accuracy
        




    for clf in accuracy_dic:
        accuracy_dic[clf] = accuracy_dic[clf] / 10.0
        res_entry = pd.DataFrame([[clf, accuracy_dic[clf]]], columns=res_cols)
        res = res.append(res_entry)

    print res