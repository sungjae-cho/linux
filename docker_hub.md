# Docker Hub

## 1. Key concepts

- Image: An object containing a virtual enviroment.
- User name: The user name of Docker Hub ID.
- Repository: A collection of docker images.
- Tag: A name to identify docker images in a docker repository.

## 2. How to push a docker image to a docker repository

1. Create a docker repository for user account.
1. Check the image ID of the docker container from the result of typing `docker ps`.
1. Tag a name to be used in your docker repository.
```bash
docker tag <docker_ID> <user_name>/<repository>:<tag>
```
1. Push the tag image to the repository of your user account.
```bash
docker push <user_name>/<repository>
```
