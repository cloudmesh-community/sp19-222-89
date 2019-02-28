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

   #randomly shuffle the data/corresponding labels
    #np.random.shuffle(a);
    
    #separate features from labels

    #find out how many labels we need
   b_shape = np.shape(b)
    
    #make a new array for it
   b_labels = np.zeros(b_shape[0])
    
    #populate that array (slice isn't working so)
   for i in range(0, b_shape[0]):
      if(list(b[i])[8] == '3'):
         b_labels[i] = 1
      else:
         b_labels[i] = 0


    #now make array for features
   b_features = np.zeros((b_shape[0], nfeatures))

    
    #populate that array
   for i in range(0, b_shape[0]):
      for j in range(0, nfeatures):
         b_features[i][j] = list(b[i])[j]

   print(b)
   anwser = svm_model.predict(b) #Using test data to make prediction and validate the model
   return anwser 

#Create a nice ouput comparison of prediction and actual label
#for i in range(len(model.labels_testing)):
   #print("Prediction vs Answer: ", anwser[i], '|', model.labels_testing[i])

anwser = run_model('data_130.csv')
print(anwser)
