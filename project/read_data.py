#this function is meant to read in the data from the .csv file and return
#a numpy array containing all the data

"""Important note: when the data is read using the csv.DictReader,
the order of the features is changed from the original. In the 
list of dictionaries, the order of features is as follows:
ISOS_Size_x, ISOS_Size_y, COST_Size_y, COST_Size_x, Coord_y, Coord_x,
ISOS_z, COST_z, Cone_Type"""

import csv
def read(fpath):

    #make file object
    with open(fpath) as f_obj:

        #make reader object
        reader = csv.DictReader(f_obj, delimiter=',')

        #make data list
        data = []

        for row in reader:
            data.append(row)

        return data
