#This function will run the model and return a list of the labels
#assigned to the given feature sets.
from joblib import dump, load
from read_data import read
import numpy as np
from split_data import format
from flask import jsonify, request

def run_model(fpath):

    #reload svm model from file
    #need to choose latest model
    svm_model = load('newmodel.joblib')
    
    #create list to hold final labels
    answer = []

    #pass the given file to our read function to get its data
    input = read(fpath)

    #pass the dict-form data to our format function to get it in numpy array
    #form so that sci-kit learn will use it
    input_formatted = format(input) 

    #Now let's create an array of indices the same length as our data
    #indices = np.arange(0,len(input_formatted))

    #run prediction on every data point given, return resultant list
    #of classifications
    answer = svm_model.predict(input_formatted) 
    return answer

def do_this():
    if request.method == 'POST':
        print(request.form)
