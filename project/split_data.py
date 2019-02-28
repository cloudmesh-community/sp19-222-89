#this function splits the returned by read_data into training and
#testing using an 80-20 split (respectively)

import numpy as np

def split(data):

    #variable to store # of features, in this case we have 8
    nfeatures = 8
    
    #get the values from the list of dictionaries, put them into
    #a new list
    list_data = []
    
    for i in data:
        list_data.append(i.values())

    #convert our data list to a numpy array
    a = np.array(list_data)


    #randomly shuffle the data/corresponding labels
    #np.random.shuffle(a);
    
    #separate features from labels

    #find out how many labels we need
    a_shape = np.shape(a)
    
    #make a new array for it
    a_labels = np.zeros(a_shape[0])
    
    #populate that array (slice isn't working so)
    for i in range(0, a_shape[0]):
        if(list(a[i])[8] == '3'):
            a_labels[i] = 1
        else:
            a_labels[i] = 0


    #now make array for features
    a_features = np.zeros((a_shape[0], nfeatures))

    
    #populate that array
    for i in range(0, a_shape[0]):
        for j in range(0, nfeatures):
            a_features[i][j] = list(a[i])[j]

    
    #split to training and testing

    #80% for training, 20% for testing
    n_train = np.int(np.round(a_shape[0] * 0.8))
    n_test = a_shape[0] - n_train
     
    a_feat_training = a_features[0:n_train]
    a_feat_testing = a_features[0:n_test]
    a_label_training = a_labels[0:n_train]
    a_label_testing = a_labels[0:n_test]
    
    return a_feat_training, a_label_training, a_feat_testing, a_label_testing
