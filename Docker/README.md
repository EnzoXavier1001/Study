### Create and Run a Container
- **Create and run a container:** 
  - `docker container run <params> <image>:<tag>`
- **Gives a Name to the container:**
  - `docker container run --name <containers_name> <image>:<tag>`
- **Delete the container in the end:**
  - `docker container run --rm <image>:<tag>`
- **Run the container in background:**
  - `docker container run -d <image>:<tag>`

<hr />

### Create without running a container
- **Create container (container will be off):**
  - `docker container create <params> <image>:<tag>`
- **Create container (container will be on)::**
  - `docker container create -it <image>:<tag>`

<hr />

### Containers Management
- **List containers running:**
  - `docker container ls`
- **List all containers:**
  - `docker container ls -a`
- **Last container created:**
  - `docker container ls -l`
- **Start:**
  - `docker container start <container_id || name>`
- **Restart:**
  - `docker container restart <container_id || name>`
- **Pause:**
  - `docker container pause <container_id || name>`
- **Unpause the last container:**
  - `docker container unpause <container_id || name>`
- **Stop:**
  - `docker container stop <container_id || name>`
- **Remove (container not running):**
  - `docker container rm <container_id || name>`
- **Remove (container running):**
  - `docker container rm -f <container_id || name>`
- **Remove all containers:**
  - `docker container prune`

<hr />

### Mapping Port
- **Set a random port:**
  - `docker container run --name custom_name -d -P <image_name>`
- **Set a port (your_port:container_port):**
  - `docker container run --name custom_name -d -p 5000:80 <image_name>`
- **Check container port:**
  - `docker port <container_name>`
  
<hr />

### Usefull Commands
- **Acess a running container:**
  - `docker container attach <container_id || name>`
- **Seening the processes inside a container:**
  - `docker container top <container_id || name>`

<hr />

### Cleaning:
- **Containers:** 
  - `docker container rm $(docker container ls -a -q)`
- **Images:**
  - `docker image rm $(docker image ls -a -q)`
- **Volumes:**
  - `docker volume rm $(docker volume ls -q)`
- **Networks:**
  - `docker network rm $(docker network ls -q)`

<hr />

### Build
- **Build:** 
  - `docker image build <path_to_dockerfile`
- **Naming the image:**
  - `docker image build -t <custom_name> <path_to_dockerfile`

<hr />

### Images
- **List images:** 
  - `docker images`
- **Remove a image:**
  - `docker rmi <image_id>`


