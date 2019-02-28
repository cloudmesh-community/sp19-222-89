from joblib import dump, load
from read_data import read
import numpy as np 

#reload svm model
svm_model = load('model.joblib')

def run_model(fpath):
   anwser = {} #create an array to hold predictions
   input = read(fpath)
   #get the values from the list of dictionaries, put them into
    #a new list
   
   list_input = []
   
   for i in input:
        list_input.append(i.values())

    #convert our data list to a numpy array
   b = np.array(list_input)

   print(b)
   anwser = svm_model.predict(b) #Using test data to make prediction and validate the model
   return anwser 

#Create a nice ouput comparison of prediction and actual label
#for i in range(len(model.labels_testing)):
   #print("Prediction vs Answer: ", anwser[i], '|', model.labels_testing[i])

anwser = run_model('data_130.csv')
print(anwser)
