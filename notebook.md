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
