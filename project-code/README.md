
To run this code:
download dockerfile

Then run the following commands in the terminal:

```bash
docker build -t service_test:latest .

docker run -v'pwd':/sp19-222-89/project-code -w /sp19-222-89/project-code  --rm -it -p 4555:4555 Dockerfile /bin/bash
```
