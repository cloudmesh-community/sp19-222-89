#this function is meant to read in the data from the .csv file and return
#a numpy array containing all the data. It also filters out any rows in the
#data which include NaN as either a feature or a label

"""Important note: when the data is read using the csv.DictReader,
the order of the features is changed from the original. In the 
list of dictionaries, the order of features is as follows:
ISOS_Size_x, ISOS_Size_y, COST_Size_y, COST_Size_x, Coord_y, Coord_x,
ISOS_z, COST_z, Cone_Type"""

import csv
import math
def read(fpath):

    #make file object
    with open(fpath) as f_obj:

        #make reader object
        reader = csv.DictReader(f_obj, delimiter=',')

        #make data list
        data = []

        #make boolean nan variable to store if we hit a nan value
        nan = 0
        
        #boolean to store if there's a non value or not
        for row in reader:
            nan = 0
            for i in row.items():
                if(i[1] == "NaN"):
                    nan = 1

            if(nan == 0):
                data.append(row)

        return data
