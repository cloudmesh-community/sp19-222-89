# S-cone Classification Using REST Services and Machine Learning

| Brandon Fischer, Ryan Danehy
| bfisch9@iu.edu, rdanehy@iu.edu
| Indiana University Bloomington
| hid: sp19-222-89 sp19-222-102
| github: [:cloud:](https://github.com/cloudmesh-community/sp19-222-89/tree/master/project-report/report.md)
| code: [:cloud:](https://github.com/cloudmesh-community/sp19-222-89/tree/master/project-code)

---

Keywords: S-cones, Scikit, Support Vect Machine, Neural Network, WebPlotViz, ISOS (Inner Segment - Outer Segment junction), Cone Outer segment tip (COST).

---


## Abstract

We worked in partnership with Dr. Don Miller's lab from the IU School
of Optometry to create a binary classifier which is trained to
differentiate (and generate a count of) S-cones from L and M cones in
3D retinal imaging. We deployed an RBF-kernel SVM to classify S-cones
vs non-S-cones. This project has clinical significance in the tracking
of progression of the disease Retinitis Pigmentosa (RP). In RP,
S-cones can be seen migrating from their natural positions, and
eventually disappearing entirely in retinal scans. Our service could
be extended from purely classifying/counting S-cones to tracking the
rate of their movement and determining the progression/severity of the
disease in a given patient.

## Introduction

Cones or Cone cells are photoreceptor cells in the retinas of humans. They 
are responsible for color vison and work best in bright lights. S-cone cells 
differ from M-cones and L-cones based on the light wavelengths they are 
senstive to. For example S-cones are sensitive to short-wavelengths, M-cones 
to medium-wavelengths, and L-cones to Long-wavelengths [@89-Role]. Short-wavelengths 
correspond with 'blue', medium with 'green', and long with 'red', therefore 
it is believed that the study of these cones could lead to new insights into 
dieseases such as red-green colorblindness.

![Spectrum of Wavlengths](images/Color_Vision.png){#fig:Color_Vision}

Caption: Color vision. The absorption spectra of the four photopigments in 
the normal human retina. The solid curves indicate the three kinds of cone 
opsins; the dashed curve shows rod rhodopsin for comparison. Absorbance is 
defined as the log value of the intensity of incident light divided by 
intensity of transmitted light [@89-Role].

Individual cones are entirely color blind in that their response is simply a 
reflection of the number of photons they capture, regardless of the 
wavelength of the photon. Therefore it is impossible to determine why a 
change in the effectiveness of a particular cone occurred. This question can 
only be resolved by comparing the activity in different classes of cones. 
Comparisons of the responses of individual cone cells, and cells at higher 
levels in the visual pathway are clearly involved in how the visual system 
extracts color information from spectral stimuli. However, understanding of 
the neural mechanisms that underlie color perception has been elusive to the 
scientific community @fig:Color_Vision.

"This diagram was produced based on histological 
sections from a human eye to determine the density of the cones. The diagram 
represents an area of about 1° of visual angle. The number of S-cones was set
to 7% based on estimates from previous studies. The L-cone:M-cone ratio was 
set to 1.5. This is a reasonable number considering that recent studies have
shown wide ranges of cone ratios in people with normal color vision. In the
central fovea an area of approximately 0.34° is S-cone free. The S-cones 
are semi-regularly distributed and the M- and L-cones are randomly 
distributed. Throughout the whole retina the ratio of L- and M- cones to 
S-cones is about 100:1 [@89-Rochester]."

There are two main reflection sites inside the cone photoreceptor cells that 
line the back of the eye. The first one occurs at what is called the inner 
segment – outer segment junction (ISOS) and the second one (which occurs 
directly behind the first one) occurs at what is called the cone outer 
segment tip (COST). Cones can be classfied by the comparison of the inner 
segment length vs outer segment length. For example, histologically S-cones 
have a longer inner segment and a shorter outer segment. The ultimate goal of
this project was to design an effective and fast method of classification of
S-cones, using REST Services to facilitate user interaction with the model.

## Data

Datasets were provided by Dr. Miller's lab which included the 3D
coordinates and aperture size of each cone detected within the retinal
scan. Using this information, we were able to differentiate the
S-cones from the others due to their deeper position and wider
aperture compared to the other cell types. Our starting dataset
includes information from the images of three patients' retinas, with
a mix of healthy and colorblind individuals. Additional data was
collected as needed. The data provided was delivered in a fashion to
not jeopadize the patients anonymity nor were we given any personal
data that could or would put a patient's privacy in concern.

After the initial model was trained, unlabeled data is given a
classification through a rest service, and the count and locations of
S-cones was returned via another rest service. The service also allows
the retraining of the model on new datasets, and outputs the
corresponding metrics on the newly trained model. This allows the
model to be updated and re-trained as more data becomes available.

Our data includes eight features: X-Coordinate of cone (Coord_X), Y
Coordinate of cone (Coord_Y),Retina Depth location of Inner- Outer
Segment(ISOS_Z), X Coordinate of ISOS (ISOS_size_X), Y Coordinate of
ISOS (ISOS_size_Y), Retina Depth location of COST (COST_Z), X
Coordinate of COST (COST_size_X), and Y Coordinate of COST
(COST_size_Y). These features were extracted from 3D imaging of the
retinal hence the three dimensional parameter types. ISOS_z is the
retinal depth location of ISOS and COST_z is the retinal depth
location of COST.

### Preprocessing

Our raw data had some observations that were unknown or missing
certain datapoints, and as such were marked "Nan" in the original
dataset. We preproccessed the data in order to exclude feature vectors
which included Nan for any feature value. The preproccessing that we
performed on the data can be seen in the read_data.py file. Machine
learning models can be very sensitive to scaling and in order to
prevent this we normalized the data. Normalization rescales the data
to be in the range of 0 to 1, thus eliminating any possible feature
scaling within our data. We performed normalization on our data using
Scikit learn's preprocessing.normalize() function. This function
scales the input indivudally to unit norms (vector length). In order
to guarantee the quality of our data before training a model, we
standardized our data. Standardization transforms data to have a mean
of zero and standard deviation of 1. Standardization was performed by
using scikit learn's StandardScaler(). The function first_model and
retrain_model in model.py show this normalization and standardization.

### Visualization

We visualized our data using WebPlotViz which results can be seen
using the following link.
https://spidal-gw.dsc.soic.indiana.edu/public/groupdashboard/E222. From the WebPlotViz
visualizations it can be noted that the data is not clearly seperated
into clusters nor in a regular shape. It also imporant to notice how
there is no clear distiniction on which features are weighted heaviler
than others in classifying S-cone from M and L-cones. However,
histological studies have shown that the biggest differentiation
betwen the different cones types is the difference between ISOS_Z -
COST_Z [@89-structure]. This difference siginifes the physical length of an
important component of the cone photoreceptors. In one of the
visualizations we plotted X_coordinate vs Y-coordinate vs (COST_Z-
ISOS_Z). In this plot it is not glaringly obvious that (COST_Z-
ISOS_Z) is the most imporant feature, but there does seem to be a
noticeable correlation. The lack of an obviously dominant feature led
us to the conclusion that for our model to train the best no weights
should be applied (*Not sure that's accurate, I think DNN will always
give weights*)

## Model Discussion

In our final project we decided to use a neural network using scikit
learn's MLPClassifier(). We had several reason for picking a neural
network model, one being the fact that it is supervised learning.
Supervised learning make sense for our project because in our training
data we were given labels for every cell observed. Supervised learning
also made sense given that our goal was to predict the type of cone
for a given cell, and making predictions is usually the goal behind
supervised learning algorithms. Additionally, neural networks are
ideal for solving non-linear classification problems, which is
precisely what we are trying to solve [@89-Neural].

### Failures

We started out trying to use a support vector machine algorithm (SVM)
as our model of choice, but several problems became evident while
trying to implement the SVM. We originally choose Scikit’s svm.SVC()
algorithm, but after testing it became apparent the model was not
accurate at all averaging an F1 score below .3. We then experimented
with altering the parameters of the algorithm, including changing from
a linear to non-linear SVM model. We found that changing the kernel to
‘RBF’ produced an F1 score of 1.0. This makes sense given that our
data is grouped in a nonlinear way and ‘RBF’ are used for nonlinear
solutions.

![RBF Kernel example](images/rbf_kernel_pic.png){#fig:RBF_Kernel}

However, an F1 score of 1.0 is a possible symptom of an over-fitting
problem. Over-fitting is when an algorithm matches so perfectly to the
training data that the model does not generalize well to
classification of additional datasets.

![Overfitting example](images/Overfitting.png){#fig:Overfitting} 

To determine whether there is overfitting or not we decided to
decrease the amount of data used for training. Decreasing the amount
of data used for training should only slightly decrease the
performance of the model unless there is overfitting. If there was
overfitting then they would be a drastic difference since they would
be less data to fit perfectly too. We trained with roughly 60% of the
data rather than 80%. The new model that was trained with 60% of the
data performed horribly, confirming the overfitting problem. Thus we
decided to move on to the implementation of a neural network.

### Activation Function

When deciding to implement a multi-layer perceptron (neural network)
it is imporant to consider and analzye what activation function will
work best for your data solution. The types of activation functions
have very important influences on the networks’ learning speeds,
classification correct rates and non-linear mapping precision.
Activation functions determine the output of a neural network. The
function is attached to each neuron in the network, and determines
whether it should be activated (“fired”) or not, based on whether each
neuron’s input is relevant for the model’s prediction. Activation
functions also help normalize the output of each neuron to a range
between 1 and 0 or between -1 and 1. An additional aspect of
activation functions is that they must be computationally efficient
because they are calculated across thousands or even millions of
neurons for each data sample. Modern neural networks use a technique
called backpropagation to train the model, which places an increased
computational strain on the activation function, and its derivative
function. Backpropagation is an algorithm which traces back from the
output of the model, through the different neurons which were involved
in generating that output, back to the original weight applied to each
neuron. Backpropagation suggests an optimal weight for each neuron,
which results in the most accurate prediction [@89-Activation].

### Decision

In order to decide what activation function fit our model best we
experimented with a few activation functions. Firstly we experimented
with a logistics function which performed poorly averaging an F1 score
around .5. Next we tried using the RELU function which performed
significantly better averaging a F1 score around .9. However the best
was the Hyperbolic Tangent (Tanh), which averaged f1 score around .95.
The advantages tanh provides is that its zero centered meaning it
makes it easier to model strongly positive, negative, or neutral
inputs. As previosuly mentioned our input (features) are very neutral
making this activation function perfect for our model [@89-Activation].

## REST Service Implementations

REST is an abstraction of the basic HTTP methods (like GET, POST, etc)
which is used to build APIs that behave in predictable ways. The basic
behaviors of REST services are called CRUD: Create, Read, Update, and
Delete [@89-REST]. These map to the HTTP methods POST, GET, PUT, and
DELETE, respectively. When a server is launched that implements REST
conventions, the fields of the URL submitted to the website will
contain endpoints and/or parameters which are used to specify the
desired behavior.

The interaction between client and server for our service in
particular involves the use of 3 yaml specified endpoints: /,
/app/run, and /app/retrain. These can be found in our master.yaml
file. The '/' endpoint is a simple read action from the client, and a
rendered html page with information about our service is returned to
the client.

The /app/run endpoint specifies another read action, and returns a
rendered html template to the client which will allow a user to upload
one or more .csv files containing data which they want classified.
When the user clicks the upload button on this page, a create action
is used to send the data files from client to server. The files which
are uploaded are then run through the model to have their S-cones
counted, and then an html file containing feedback is dynamically
generated. A rendered version is returned to the client.

Similarly, the /app/retrain endpoint specifies a read action and
returns a rendered file-upload html template to the client. The client
user will upload files with which to train a new model, and then by
clicking the upload button they again generate a create action. These
uploaded files are then used to train a new model, which is created,
saved, and tested. The metrics calculated as a result of this testing,
accuracy, precision, recall, and F1 score, are dynamically written to
an html file, which is then rendered and returned to the client.

## Specification

```
swagger: "2.0"
info: 
  version: "0.0.1"
  title: "cone classifier"
  description: "classify cones from csv data"
  termsOfService: "http://swagger.io/terms/"
  contact: 
    name: "Ryan Danehy and Brandon Fischer"
  license: 
    name: "Apache"
host: "localhost:4555"

consumes:
  - "text/html"
produces:
  - "text/html"

basePath: "/app"

paths:
  /run:
    get:
      operationId: scripts.uploadrun.display
      description: "Displays upload file page"
      responses:
        "200":
          description: "Upload page displayed successfully"

  /upload_file:
    post:
      operationId: scripts.uploadrun.upload
      description: "Generate post request to actually upload file"
      responses:
        "201":
          description: "File upload successful"

  /retrain:
    get:
      operationId: scripts.uploadrerun.display
      description: "Displays upload new training file page"
      responses:
        "200":
          description: "Upload page displayed successfully"

  /upload_file_retrain:
    post:
      operationId: scripts.uploadrerun.upload
      description: "Generate post request to actually upload file"
      responses:
        "201":
          description: "File upload successful"
```

