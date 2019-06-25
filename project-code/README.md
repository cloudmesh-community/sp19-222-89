# Retinal Cone Counter Rest Service

To run this code, clone the repo with:

git clone https://github.com/cloudmesh-community/sp19-222-89.git

Next, in terminal enter the project-code directory of the repo.

Then run the following commands in the terminal:

make docker-all

To test the service while it is running, navigate in a browser to:

localhost:4555

and choose the endpoint which you want to use (instructions are given on the homepage). Then, choose a file from the data directory of the repo and upload it.

Finally, to stop the service, open another terminal and navigate back to the directory containing the Dockerfile and Makefile.
Then, run the command:

make docker-clean

Other Commands:
make docker-stop 
-stops the program but keeps the container up so it can be easily restarted without rebuilding the whole container

make docker-start

-Restarts the program after it has been stopped.

docker login

-logins into docker and makes sure it is running.

Note: to install docker go to this link https://docs.docker.com/docker-for-mac/install/
Visualization: https://spidal-gw.dsc.soic.indiana.edu/public/groupdashboard/E222
