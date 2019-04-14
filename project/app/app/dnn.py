from read_data import read
from split_data import split
from sklearn import utils, preprocessing
from sklearn.neural_network import MLPClassifier
from joblib import dump
from test_model import run_metrics_model, F1
import os


NNdata = read("./data/data_130.csv") + read("./data/data_53.csv") + read("./data/data_151.csv")

utils.shuffle(NNdata)

NNfeatures_training, NNlabels_training, NNfeatures_testing, NNlabels_testing = split(NNdata)

# sgd in general f1 = 0
#relu and lbfgs f1 = .5
#tanh and lbfgs f1 = .6875
#logistics and lbfgs f1 = .5762


cnn = MLPClassifier(activation= 'tanh', solver = 'lbfgs')

cnn.fit(NNfeatures_training, NNlabels_training.ravel())


TP, FP, TN, FN, mp = run_metrics_model(cnn, NNfeatures_testing, NNlabels_testing)

f1 = F1(TP, FP, TN, FN)
print('f1:' , f1)
print("Coefficents for features: ")
for coef in cnn.coefs_:
   print(coef.shape(cnn.coefs_))
