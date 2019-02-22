from read_data import read
from split_data import split
from sklearn import svm
from joblib import dump, load

data = read("data_53.csv")
features_training, labels_training, features_testing, labels_testing = split(data)

#create SVM model
svm_model = svm.LinearSVC()
svm_model.fit(features_training, labels_training.ravel())

dump(svm_model, 'model.joblib')

