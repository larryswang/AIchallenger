#!/user/bin/env python
# -*- coding:utf-8 -*-

import os
model_save_path = os.path.abspath('..') + "/model/"
train_data_path = os.path.abspath('..') + "/data/sentiment_analysis_trainingset.csv"
validate_data_path = os.path.abspath('..') + "/data/sentiment_analysis_validationset.csv"
test_data_path = os.path.abspath('..') + "/data/sentiment_analysis_testset.csv"
test_data_predict_out_path = os.path.abspath('..') + "/predict/" 