# -*- coding:utf-8 -*-

from get_data_report import *
from preprocess_for_data import *

RAW_TRAIN_FILE = r'./data/train.csv'
RAW_TEST_FILE = r'./data/test.csv'
RESULT_TRAIN_PATH = r'./data/res_train.csv'
RESULT_TEST_PATH = r'./data/res_test.csv'


def main():
    get_data_report(RAW_TRAIN_FILE)
    preprocess_for_train_data(RAW_TRAIN_FILE, RESULT_TRAIN_PATH)
    preprocess_for_test_data(RAW_TEST_FILE, RESULT_TEST_PATH)


if __name__ == '__main__':
    main()