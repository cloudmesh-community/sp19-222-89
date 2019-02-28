#this file will serve to generate the initial model, and could be retooled
#to serve as a model "updater", i.e. generating a new model any time
#we gain access to a new labeled data set
#It also saves the model to a file so that we don't have to regenerate
#the model each time we want to use it to classify new data

from read_data import read
from split_data import split
from sklearn import svm
from joblib import dump
from test_model import run_metrics, F1, read_model_from_file

data = read("data_151.csv")
data += read("data_130.csv") + read("data_53.csv")
features_training, labels_training, features_testing, labels_testing = split(data)

#create SVM model
svm_model = svm.SVC(max_iter = 10000, kernel='rbf')
svm_model.fit(features_training, labels_training.ravel())

dump(svm_model, 'model.joblib')

svm_model=read_model_from_file()

TP, FP, TN, FN = run_metrics(svm_model, features_testing, labels_testing)
f1 = F1(TP, FP, TN, FN)
print('Coord_x|Coord_y|ISOS_z|ISOS_Size_x|ISOS_Size_y|COST_z|COST_Size_x|COST_Size_y ')
#print(svm_model.coef_)
print('F1 score = ' + str(f1))

