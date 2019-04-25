docker-all: docker-build docker-start
	@echo "docker-all done"

docker-build:
	@echo "building the image from docker file..."
	docker build --no-cache --pull -t sp19-222-89/cone_counter:latest .
	@echo "image built"

docker-start:
	@echo "starting the service in container..."
	docker run -v `pwd`/:/docker_save/ -p 4555:4555 sp19-222-89/cone_counter

service:
	@echo "creating the service..."
	pip install --upgrade pip
	pip install -r requirements.txt

start:
	@echo "starting the service"
	pip install --upgrade pip
	pip install -r requirements.txt
	python server.py

docker-save:
	@echo "saving data from container to local machine"
	sudo docker cp $$(docker ps -alq):/sp19-222-89/project-code ./docker_save	
	@echo "done saving data"

docker-stop:
	@echo "stopping the service"
	docker stop $$(docker ps -alq)
	@echo "service stopped"

docker-remove:
	@echo "removing the image"
	docker rmi -f sp19-222-89/cone_counter
	@echo "image removed"

docker-clean: docker-save docker-stop docker-remove
	@echo "docker service stopped and image removed"

clean:
	@echo "removing service files created"
	rm -rf $(CREATED)
