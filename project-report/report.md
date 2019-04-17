# This is where my title is missing

| Brandon Fisher, Ryan Danehy | bfisch9@iu.edu, rdanehy@iu.edu | Indiana University| hid: sp19-222-89 , sp19-222-102 | github: ☁️ | code: ☁️

## Abstract

We worked in partnership with Dr. Don Miller's lab from the IU School of Optometry, and the goal was to create a binary classifier which is trained to differentiate (and generate a count of) S-cones from L and M cones in 3D retinal imaging. We deployed an RBF-kernel SVM to classify S-cones vs non-S-cones. This project has clinical significance in the tracking of progression of the disease Retinitis Pigmentosa (RP). In RP, S-cones can be seen migrating from their natural positions, and eventually disappearing entirely in retinal scans. Our service could be extended from purely classifying/counting S-cones to tracking the rate of their movement and determining the progression/severity of the disease in a given patient.


## Introduction

Datasets were provided by Dr. Miller's lab which included the 3D coordinates and aperture size of each cone detected within the retinal scan. Using this information, we were able to differentiate the S-cones from the others due to their deeper position and wider aperture compared to the other cell types. Our starting dataset includes information from the images of 3 patients' retinas, and were be divided into sub-regions to give us more subsets. Additional data were collected/requested as needed.

After the initial model is trained, unlabeled data can be given for classification via rest service, and the count of S-cones will be returned via another rest service. Our service also allows the retraining of the model on new datasets, and then outputs the corresponding metrics on the newly trained model. This will allow our algorithms to be updated and improved upon as more data becomes available. 

## Basic Science
Cones or Cone cells are photorecptor cells in the retinas of humans. They are responsible for color vison and work best in bright lights. S-cone cells differ from M-cones, and L-cones based on the light wavelengths they are senstiive to. For example S-cones are sensitive to short-wavelengths, M-cones to medium-wavelengths, and L-cones to Long-wavelengths.  https://www.ncbi.nlm.nih.gov/pubmed/12675479. short-wavelengths correspond with 'blue', medium with 'green', and long with 'red'. Therefore its believed that the study of these cones could lead to new insights into dieseases such as red-green colorblindness.

Figure: https://www.ncbi.nlm.nih.gov/books/NBK11059/figure/A766/?report=objectonly

Individual cones are entirely color blind in that their response is simply a reflection of the number of photons they capture, regardless of the wavelength of the photon. It is impossible, therefore, to determine why a change in the effectiveness of a particular cone occurred. This question can only be resolved by comparing the activity in different classes of cones. Comparisons of the responses of individual cone cells, and cells at higher levels in the visual pathway are clearly involved in how the visual system extracts color information from spectral stimuli. Despite these insights, understanding of the neural mechanisms that underlie color perception has been elusive to the scientific community. 
https://www.ncbi.nlm.nih.gov/books/NBK11059/

There are two main reflection sites inside the cone photoreceptor cells that line the back of the eye. The first one occurs at what is called the inner segment – outer segment junction (ISOS) and the second one (which occurs directly behind the first one) occurs at what is called the cone outer segment tip (COST). Cones can be classfied by the comparison of the inner segment length vs outer segment length. For example histologically S-cones have a longer inner segment and a shorter outer segment. 

The ultimate goal of this project was to design an effective and fast method of classification of S-cones ultizing Machine Learning and REST Services. 

## Data
The data we used was from 3 different undisclosed/anonymous patients. We will given the data by Dr. Millers group and was provided no data that could jeopadize the patients anonymity nor were we given any personal data that could or would put a patient's privacy in concern. 

Our data includes 8 features: X-Coordinate, Y-Coordinate, ISOS_Z, ISOS_size_X, ISOS_size_x, COST_z, COST_X , and COST_y. These features were extracted from 3D imaging of the retinal hence the three dimensional parameter types. ISOS_z is the retinal depth location of ISOS and COST_z is the retinal depth location of COST. 

We visualized our data using WebPlotViz which results can be seen using the following link. https://spidal-gw.dsc.soic.indiana.edu/dashboard 

Since being a classification problem as well as our data being clustered in irregular form we decided that an SVM and or Neurl Network would be the best best model to use. 
