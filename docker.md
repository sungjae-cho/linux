# Reference
* [Get Started | Docker Documentation](https://docs.docker.com/get-started/)
* [About Docker CE | Docker Documentation](https://docs.docker.com/install/)
* [Get Docker CE for Ubuntu | Docker Documentation](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [NVIDIA/nvidia-docker](https://github.com/NVIDIA/nvidia-docker)

# Key Words
Docker, container, image, cluster, containerization, virtual machine

* containerization: The use of Linux containers to deploy applications
* image: an executable package that includes everything needed to run an application--the code, a runtime, libraries, environment variables, and configuration files
* container: a runtime instance of an image--what the image becomes in memory when executed (that is, an image with state, or a user process)
  * A container runs natively on Linux and shares the kernel of the host machine with other containers.
* virtual machine:
  * A virtual machine (VM) runs a full-blown “guest” operating system with virtual access to host resources through a hypervisor.
* Community Edition (CE)
  * For developers and small teams
* Stable 
  * Stable gives you latest releases for general availability. Recommended for general users.
* Test
  * Test gives pre-releases that are ready for testing before general availability.
* Nightly 
  * Nightly gives you latest builds of work in progress for the next major release.
* Enterprise Edition (EE)
  * Docker Enterprise Edition (Docker EE) is designed for enterprise development and IT teams who build, ship, and run business-critical applications in production and at scale.
  * EE is a superset of the code delivered in CE.

# Key Statements
* container ≠ virtual machine

# Commands

* `docker ps`: see a list of your running containers.
* `docker cp <containerId>:/file/path/within/container /host/path/target`: Copying files from a docker container to a host. 


# Install
## Uninstall old versions
```bash
sudo apt-get remove docker docker-engine docker.io
```

## Install Docker CE

### SET UP THE REPOSITORY

Update the `apt` package index:
```bash
sudo apt-get update
```

Install packages to allow apt to use a repository over HTTPS:
```bash
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
```

Add Docker’s official GPG key:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

Verify that you now have the key with the fingerprint.
```bash
sudo apt-key fingerprint 0EBFCD88
```

Use the following command to set up the stable repository.
```bash
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

### INSTALL DOCKER CE

Update the apt package index.
```bash
sudo apt-get update
```

Install the latest version of Docker CE.
```bash
sudo apt-get install docker-ce
```

Verify that Docker CE is installed correctly by running the `hello-world` image.
```bash
sudo docker run hello-world
```

### UPGRADE DOCKER CE

To upgrade Docker CE, first run `sudo apt-get update`, then follow the installation instructions, choosing the new version you want to install.

### To Use `docker` Command Without `sudo` Permission

This enables the `user` to use the `docker` command with out `sudo` permission.
```bash
sudo usermod -aG docker "user"` 
```

## Install NVIDIA Container Runtime for Docker
```bash
# If you have nvidia-docker 1.0 installed: we need to remove it and all existing GPU containers
docker volume ls -q -f driver=nvidia-docker | xargs -r -I{} -n1 docker ps -q -a -f volume={} | xargs -r docker rm -f
sudo apt-get purge -y nvidia-docker

# Add the package repositories
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
  sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update

# Install nvidia-docker2 and reload the Docker daemon configuration
sudo apt-get install -y nvidia-docker2
sudo pkill -SIGHUP dockerd

# Test nvidia-smi with the latest official CUDA image
docker run --runtime=nvidia --rm nvidia/cuda:9.0-base nvidia-smi
```

### To Use `nvidia-docker` Command Without `sudo` Permission

This enables the `user` to use the `nvidia-docker` command with out `sudo` permission.
```bash
sudo usermod -aG nvidia-docker "user"` 
```
