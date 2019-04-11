| Brandon Fisher, Ryan Danehy | bfisch9@iu.edu, rdanehy@iu.edu | Indiana University| hid: sp:19-523-000 | github: ☁️ | code: ☁️

## Abstract

This project was in partnership with Dr. Don Miller's lab from the IU School of Optometry, and the goal of the project is to create a binary classifier which is trained to differentiate (and generate a count of) S-cones from L and M cones in 3D retinal imaging. We deployed an RBF-kernel SVM to classify S-cones vs non-S-cones. This project has clinical significance in the tracking of progression of the disease Retinitis Pigmentosa (RP). In RP, S-cones can be seen migrating from their natural positions, and eventually disappearing entirely in retinal scans. Our service could be extended from purely classifying/counting S-cones to tracking the rate of their movement and determining the progression/severity of the disease in a given patient.


## Introduction

Datasets were provided by Dr. Miller's lab which included the 3D coordinates and aperture size of each cone detected within the retinal scan. Using this information, we were able to differentiate the S-cones from the others due to their deeper position and wider aperture compared to the other cell types. Our starting dataset includes information from the images of 3 patients' retinas, and were be divided into sub-regions to give us more subsets. Additional data were collected/requested as needed.

After the initial model is trained, unlabeled data can be given for classification via rest service, and the count of S-cones will be returned via another rest service. A different rest service gives the ability to retrain the model on new datasets, and metrics on the model will be outputed as well. 



