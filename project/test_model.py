#this file will test the model we generated and report a number of
#metrics to help determine the quality of the model

from joblib import load
from copy import copy

def read_model_from_file():
    svm_model = load('model.joblib')
    return svm_model
def run_metrics(model, features_testing, labels_testing):
    TP, FP, TN, FN = 0, 0, 0, 0

    for n in range(0, len(labels_testing)):
        sample = copy(features_testing[n])
        #print(sample.shape)
        sample.reshape(8,1)
        #print(sample.shape)
        mp = model.predict(features_testing)
        if mp[n] == labels_testing[n] and mp[n] == 1:
            TP += 1
        if mp[n] == labels_testing[n] and mp[n] == 0:
            TN += 1
        if mp[n] != labels_testing[n] and mp[n] == 1:
            FP += 1
        if mp[n] != labels_testing[n] and mp[n] == 0:
            FN += 1
    print("TP:", TP , 'TN:',  TN, 'FP:', FP, 'FN', FN)

    return TP, FP, TN, FN

def F1(TP, FP, TN, FN):
    return ((2 * TP)/(2*TP + FP + FN))


