# Retinal Cone Counter Rest Service

To run this code, clone the repo with:

git clone https://github.com/cloudmesh-community/sp19-222-89.git

Next, in terminal enter the project-code directory of the repo.

Then run the following commands in the terminal:

make docker-all

To test the service while it is running, navigate in a browser to:

localhost:4555

and choose the endpoint which you want to use (instructions are given on the homepage). THen, choose a file from the data directory of the repo and upload it.

Finally, to stop the service, open another terminal and navigate back to the directory containing the Dockerfile and Makefile.
Then, run the command:

make docker-clean