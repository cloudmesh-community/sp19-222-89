2/7/2019: Discussed more about .yaml files and REST services, including
how to send a URL request that contains arguments.

2/12/2019: Learned how to read data from .csv files using pandas. Also learned
how to create box plots from data.

Useful functions: select_dtypes()
		  iloc()
		  .boxplot()

Discussed important topics to cover and understand before starting work on the
final project. Also talked about getting our proposals turned in and then
creating GitHub teams for each group after that.

3/19/19: In depth explanation of k-nearest neighbors algorithm using the
example of comparing cars. We used top speed, transmission type, model year,
and color to compare cars and determine if they'd be fast or not fast.

This included writing KNN_example python notebook in my prg directory. Also
covered was the importance of standardization or normalization of data.
We used standardization to make it so that top speed and model year
wouldn't have a disproportionately huge impact on how the car was labeled
vs our other features because of their large numeric values.

3/21/19: Finished KNN example, talked about logistic regression as well.
In lab, we worked on getting the cms tools working, and running the new
cloudmesh.nn service. We also each picked a machine learning algorithm to code
and explain the example of for next time.

3/26/19: Talked about packaging of python files, dealing with directory
weirdness/importing a package from a different directory. Need to use
this to separate our code into individual directories instead
of having all of our code inside one directory.

server.py in own directory (topmost). Then in __init__.py inside each sbudir
 do:
import os
(name)_dir = os.getwd()

Also talked about docker. Looked up how to get docker container's ip address,
you use 
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id

We'll probably want this for setting up the docker container to run either on
the local machine of our user or on a cloud platform that will host it for us.
docker build -t docker_example:latest

3/28/19: Talked more about Docker.
Process: make Dockerfile, then run build as shown below, then
do docker run as shown below. To view the running/open containers,
use docker container ls -all.

docker build -t docker_example:latest .
-t lets us specify the name

docker run -i -p 5000:5000 tag_name
-i gives terminal to let us actually enter a container 
-p defines port
tag_name is what we named it in the docker build line

4/2/2019: Machine Learning + Cloud Services

Logistic regression
t(x) = a + Bx
Probability y(x)=1 is 1/(1+exp(-t(x)))
Probability y(x) = 0 is exp(-t(x))/(1+exp(-t(x)))
Total probability of set of measurements (x1, x2), (x2,y2)...(xn, yn) is 
P(y1)P(y2)...P(yn)
Minimize -lnP(y1)-lnP(y2)...-lnP(yn)

Clustering = unsupervised learning

K-Means: partition n data points into k clusters
Went through visual example(s)
Pros: can be applied to many use cases, easy to understand and implement
Always converged to something
Cons: computation intensive if there's too many points, could be unlucky
with initializing centroids, may be unsure of what value to use for k,
algorithm not robust to noise

Visualize data before carrying out algorithm
Try to reduce number of clusters
Remove noise before performing k-means
Try one of the improved clustering algorithms

Webplotviz is good online tool for visualizing data

4/4/2019: K-means clustering examples
T-Shirt example first, showed clustering using various K values, plotted
with webplotviz

One K-Means variant uses a fixed size cluster and just finds you as 
many clusters of that size as it can. Returned 420,000 clusters for
fungi data

Visualization can identify problems, especially with biological
classificiation done by people

Dimensionality reduction important to visualize, take hundreds of
features down to 3

Went throughlots of good/bad examples of the clustesr made by
k-means (mainly bad) because of reaching some local minima instead of global.
Using stochastic gradient descent instead of gradient descent can make
your algorithm not fall prey to local minimums.

Parallelism for K-Means is relatively simple and easy to implement. Adapt
it to use with Map Reduce

Lab: talked about report setup, then worked on project

4/9/2019:
General Optimization problem(s)
-Continuous vs discrete parameters
-Optimization methods like newton's method, gradient descent, stochastic
gradient descent
-Lots of optimization inspired by nature. People try to write optimization
algorithms based on the behavior of many many species
-Humans naturally do optimization when learning, doing tasks, etc
-You can model a lot of optimization problems using particles/physics
-Greedy algorithm = one that uses iterations, each one makes most obvious
minization step (greedy step). This prioritizes short term optima, not
always global optima
-Distances in Funny Spaces (recommender systems great example)
-In CS/AI/math, a heuristic is a technique to quickly solve a problem
for which classic methods are too slow. Used to find approximate solution
by trading optimality, completeness, accuracy, and/or precision for speed
-SVM: one of the most popular supervised classification algorithms 
-SVM works well for real clusters, but not so much when "life is messy, and
often life is messy"
-Many updates/changes/optimizations to SVM
-Fuzzy Clustering gives probabilities to be in certain clusters,
so points can be in more than 1! Very different from the other
methods we've discussed
-Talked about hidden Markov Methods. Basically states w/transition
probabilities. I think we talked about these in 221 and maybe applied
some kind of reinforcement learning/reward thing to them (?)

4/16/2019:
-Reviewed the overall structure of our project/things we've covered as
a part of creating the project
-Python: .py files, "scripts"
-Packaging: __init__.py important, tells python to interpret a directory containing
a .py file as a module
-Docker: 