# Retinal Cone Counter Rest Service

To run this code:
download Dockerfile and Makefile

Then run the following commands in the terminal:

make docker-all

To test the service while it is running, download a .csv file from the project-code/data directory. Then, navigate to:

localhost:4555

and choose the endpoint which you want to use (instructions are given on the homepage).

Finally, to stop the service, open another terminal and navigate back to the directory containing the Dockerfile and Makefile.
Then, run the command:

make docker-clean