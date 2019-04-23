#this file contains functions to generate a first model (primarily for testing
# purposes) and new models each time a new dataset is upload to be trained with
#It also saves the model to a file so that we don't have to regenerate
#the model each time we want to use it to classify new data

from sklearn import svm, utils, preprocessing
from sklearn.preprocessing import StandardScaler 
from sklearn.neural_network import MLPClassifier
from joblib import dump
import numpy as np
import scripts
from scripts.read_data import read
from scripts.split_data import split
from scripts.test_model import run_metrics_model, F1
import os


def first_model():

    #We're going to keep track of the model # and files used
    #to train it in a file called list.txt, which will reside
    #in our data subdirectory
    flist = open("./data/list.txt", "w")
    flist.write("./data/data_151.csv\n./data/data_130.csv\n./data/data_53.csv\n")
    flist.close

    data = read("./data/data_151.csv")
    data += read("./data/data_130.csv") + read("./data/data_53.csv")

    #Shuffle order of feature/label vectors within array.
    #Does not change the order of values within the vectors
    utils.shuffle(data)

    #data is split into training and testing sets. The split function
    #turns the python list data into a numpy array in this process
    features_training, labels_training, features_testing, labels_testing = split(data)

    #Normalize training and testing features
    normalized_ftrain = preprocessing.normalize(NNfeatures_training)
    normalized_ftest = preprocessing.normalize(NNfeatures_testing)

    #Standardize the normalized training and testing features
    scaler = StandardScaler()
    scaler.fit(normalized_ftrain)
    x_train = scaler.transform(normalized_ftrain)
    x_test = scaler.transform(normalized_ftest)

    #create dnn model
    dnn = MLPClassifier(activation= 'tanh', solver = 'lbfgs')

    #Fit model with normalized+standardized data and training labels
    dnn.fit(x_train, labels_training)

######################Code below is left over from when we used SVM######
    """create SVM model
    svm_model = svm.SVC(max_iter = 10000, kernel='rbf', gamma = 'auto'  )
    svm_model.fit(features_training, labels_training.ravel())"""

    #Save model
    dump(dnn, './model_files/newmodeldnn.joblib')

    #svm_model=read_model_from_file()

    TP, FP, TN, FN, mp = run_metrics_model(dnn ,  x_test , labels_testing)
    f1 = F1(TP, FP, TN, FN)
    return f1

def retrain_model(new_files):

    #Indices list will keep track of original cell index values
    #from the csv through the shuffle operation below.
    #This will allow us to report later on which cells, by csv index,
    #were labeled as s-cones

    indices = []

    #open list.txt, add newest filename to the end
    flist = open("./data/list.txt", "a")
    for file in new_files:
        flist.write("./data/" + file + "\n")
    flist.close

    #open list.txt file, read all of its lines into list lines
    with open("./data/list.txt") as flist:
        lines = flist.readlines()

    #Pull this case out of the for loop because we need to create data
    lines[0] = lines[0].rstrip()

    #create data list, make it equal to data from first file
    #listed in list.txt
    data = read(lines[0])

    #append the csv indices for the first file to indices
    indices.append(np.arange(0,len(data)))

    #need to make sure we have the 3 starting datasets in the ./data
    #directory, and need to reference that with ./data
    for i in range(1,len(lines)):
        lines[i] = lines[i].rstrip()
        new = read(lines[i])

        #add the newly read in data to our data list
        data += new

        #append new list of indices to our list, using new this time
        indices.append(np.arange(0,len(new)))

    data_reformat = []
    indices_reformat = []

    for i in range(len(indices)):
        for j in range(len(indices[i])):
            indices_reformat.append(indices[i][j])

    """print("length of data: " + str(len(data)) + "\n")
    print("length of indices: " + str(len(indices)) + "\n")
    print("length of reformatted data: " + str(len(data_reformat)) + "\n")
    print("length of reformatted indices: " + str(len(indices_reformat)) + "\n")
    return"""

    #Shuffle the data before splitting. This function will move the
    #individual feature/label vectors around, but will not change
    #the order of the values inside these vectors
    utils.shuffle(data, indices_reformat)
    
    #data is split into training and testing sets. The split function
    #turns the python list data into a numpy array in this process
    features_training, labels_training, features_testing, labels_testing = split(data)

    #Normalize training and testing data
    normalized_ftrain = preprocessing.normalize(features_training)
    normalized_ftest = preprocessing.normalize(features_testing)

    #Standardize training and testing data
    scaler = StandardScaler()
    scaler.fit(normalized_ftrain)
    x_train = scaler.transform(normalized_ftrain)
    x_test = scaler.transform(normalized_ftest)

    #Create model
    dnn = MLPClassifier(activation= 'tanh', solver = 'lbfgs')

    #Fit model
    dnn.fit(x_train, labels_training)

    #delete oldmodel.joblib, set current newmodel.joblib to old
    #then save new as newmodel.joblib
    try:
        os.remove("./model_files/oldmodeldnn.joblib")
    except:
        print("no oldmodeldnn")
    os.rename("./model_files/newmodeldnn.joblib", "./model_files/oldmodeldnn.joblib")

    dump(dnn, "./model_files/newmodeldnn.joblib")

    TP, FP, TN, FN, predictions = run_metrics_model(dnn, x_test, labels_testing)
    f1 = F1(TP, FP, TN, FN)
    
    #Create list to hold csv index of each s_cone we find
    s_cone_list = []

###################################################################
#Note: the for loop below uses the index of the cone from the
#predictions list. For the case where we have more than 1 file,
#the s_cone list will contain its global position from the entire
#list of csvs used. This should be fixed, probably to somehow include
#the filename that the cone came from...
###################################################################
    #For each 1 in the predictions list, add its index to the
    #s_cone list.
    for i in range(len(predictions)):
        if(predictions[i] == 1):
            s_cone_list.append(i)

    #Erase what's already in the file
    f_result = open("./templates/complete_retrain.html", "w")
    f_result.write("")
    f_result.close

    #Now fill it with what we want
    f_result = open("./templates/complete_retrain.html", "a")
    f_result.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"UTF-8\">\n\t<title>Title</title>\n</head>\n<body>")
    
    f_result.write(
    '<style type="text/css">'
    '.tg  {border-collapse:collapse;border-spacing:0;}'
    '.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}'
    '.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}'
    '.tg .tg-s6z2{text-align:center}'
    '.tg .tg-s268{text-align:left}'
    '</style>'
    '<table class="tg">'
    '<tr>'
        '<th class="tg-s268" colspan="2" rowspan="2"></th>'
        '<th class="tg-s6z2" colspan="2">Actual Class</th>'
    '</tr>'
    '<tr>'
        '<td class="tg-s268">S-Cone</td>'
        '<td class="tg-s268">Other</td>'
    '</tr>'
    '<tr>'
        '<td class="tg-s6z2" rowspan="2">Predicted<br>Class</td>'
        '<td class="tg-s268">S-Cone</td>'
        '<td class="tg-s268">' + str(TP) + '</td>'
        '<td class="tg-s268">' + str(FP) + '</td>'
    '</tr>'
    '<tr>'
        '<td class="tg-s268">Other</td>'
        '<td class="tg-s268">' + str(FN) + '</td>'
        '<td class="tg-s268">' + str(TN) + '</td>'
    '</tr>'
    '</table>'
    '<br /><br /><br />'
    )
    f_result.write("F1: " + str(f1) + "<br /><br /><br />")
    f_result.write("List of S-Cone indices: " + str(s_cone_list))
    f_result.write("<br /><br /><br />\n</body>\n</html>")
    f_result.close()

def normalize():
    
    #read in the data
    data = read("./data/data_151.csv")
    data += read("./data/data_130.csv") + read("./data/data_53.csv")
    
    #split the data into training features, and testing datasets for training and validation testing
    features_training, labels_training, features_testing, labels_testing = split(data)
    
    #Normalize the data for WebPlotViz
    normalized_ftrain = preprocessing.normalize(features_training)
    normalized_ftest = preprocessing.normalize(features_testing)


    counter1 = 0
    with open('normalize.txt', 'w') as f:
        for item in normalized_ftrain:
            f.write("%s " % counter1)
            f.write("%s " % item[0])
            f.write("%s " % item[1])
            #print((4*(item[5]- item[2])), '\n X:')
            #print(item[0], '\n')
            f.write("%s " % (2*(item[2]- item[5])))
           
            f.write("%s " % int(labels_training[counter1]))
            f.write("%s\n" % int(labels_training[counter1]))
            
            counter1 = counter1 + 1

        counter2 = 0

        for item in normalized_ftest:
            f.write("%s " % (counter2 + counter1))
            f.write("%s " % item[0])
            f.write("%s " % item[1])
            f.write("%s " % (2*(item[2]- item[5])))
            f.write("%s " % int(labels_testing[counter2]))
            f.write("%s\n" % int(labels_testing[counter2]))
            counter2 = counter2 + 1
            
normalize()

    
