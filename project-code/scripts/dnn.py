from sklearn import utils, preprocessing
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler  
from joblib import dump
from test_model import run_metrics_model, F1
import os
import numpy as np
import scripts
from scripts.read_data import read
from scripts.split_data import split

def cnn():
   NNdata = read("./data/data_130.csv") + read("./data/data_53.csv") + read("./data/data_151.csv")

   utils.shuffle(NNdata)

   NNfeatures_training, NNlabels_training, NNfeatures_testing, NNlabels_testing = split(NNdata)

   # sgd in general f1 = 0
   #relu and lbfgs f1 = .5
   #tanh and lbfgs f1 = .6875
   #logistics and lbfgs f1 = .5762
   


   normalized_ftrain = preprocessing.normalize(NNfeatures_training)
   normalized_ftest = preprocessing.normalize(NNfeatures_testing)

   scaler = StandardScaler()
   scaler.fit(normalized_ftrain)
   x_train = scaler.transform(normalized_ftrain)
   x_test = scaler.transform(normalized_ftest)


   cnn = MLPClassifier(activation= 'tanh', solver = 'lbfgs')

   cnn.fit(x_train, NNlabels_training)

   dump(cnn, 'cnn_model.joblib')
   #cnn_model.joblib f1=1.0
   #cnn_modeltwo.joblib f1 = .98

   TP, FP, TN, FN, mp = run_metrics_model(cnn, x_test, NNlabels_testing)

   f1 = F1(TP, FP, TN, FN)
   print('f1:' , f1)
#cnn()
