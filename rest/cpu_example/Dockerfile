FROM ubuntu:18.04
RUN apt-get update -y && \
apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt
COPY ./server.py /app/server.py
COPY ./Makefile /app/Makefile
COPY ./cpu.py /app/cpu.py
COPY ./cpu.yaml /app/cpu.yaml

WORKDIR /app

RUN pip install -r requirements.txt


ENTRYPOINT ["python"]

CMD ["server.py"]
