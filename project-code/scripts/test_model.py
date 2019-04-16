#this file will test the model we generated and report a number of
#metrics to help determine the quality of the model

from joblib import load
from copy import copy

#run metrics on a newly generated/updated model
def run_metrics_model(model, features_testing, labels_testing):
    TP, FP, TN, FN = 0, 0, 0, 0

    mp = model.predict(features_testing)

    for n in range(0, len(labels_testing)):
        
        #mp = model.predict(features_testing)
        if mp[n] == labels_testing[n] and mp[n] == 1:
            TP += 1
        if mp[n] == labels_testing[n] and mp[n] == 0:
            TN += 1
        if mp[n] != labels_testing[n] and mp[n] == 1:
            FP += 1
        if mp[n] != labels_testing[n] and mp[n] == 0:
            FN += 1
    print("TP:", TP , 'TN:',  TN, 'FP:', FP, 'FN', FN)

    return TP, FP, TN, FN, mp

#reports F1 score given TP FP TN FN
def F1(TP, FP, TN, FN):
    return ((2 * TP)/(2*TP + FP + FN))

#runs metrics on the predictions made by an existing model
#Different from run_metrics_model because we don't pass in the features_testing
#and features_training, but instead we pass in already made predictions
#and truth values
def run_metrics_test(predictions, truth_values):
    TP, FP, TN, FN = 0, 0, 0, 0

    for n in range(0, len(truth_values)):
        
        if predictions[n] == truth_values[n] and predictions[n] == 1:
            TP += 1
        if predictions[n] == truth_values[n] and predictions[n] == 0:
            TN += 1
        if predictions[n] != truth_values[n] and predictions[n] == 1:
            FP += 1
        if predictions[n] != truth_values[n] and predictions[n] == 0:
            FN += 1

    return TP, FP, TN, FN
