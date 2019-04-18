To run this code:
download dockerfile
<br>
Then run the following commands int he terminal:
<br>
docker build -t service_test:latest .
<br>
docker run -v'pwd':/sp19-222-89/project-code -w /sp19-222-89/project-code  --rm -it -p 4555:4555 Dockerfile /bin/bash

