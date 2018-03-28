
Copy a directory. 
'-R' means 'recursive.'
```
cp -R <src_dir> <dest_dir>
```
Update `apt-get`.
```
sudo apt-get update
```
Install `pip` or `pip3`.
```
apt-get install python-pip	#python 2
apt-get install python3-pip #pytohn 3
```
Upgrade `pip` or `pip3`
```
sudo -H pip2 install --upgrade pip #python 2
sudo -H pip3 install --upgrade pip #pytohn 3
```
# Installing Jupyter
Installing Jupyter with `pip`.
If you have Python 3 installed (which we recommended):
```
python3 -m pip install --upgrade pip
python3 -m pip install jupyter
```
If you have Python 2 installed:
```
python -m pip install --upgrade pip
python -m pip install jupyter
```

# Uninstall Jupyter
```
pip install pip-autoremove
pip-autoremove jupyter -y
```

# Check CUDA version.
```
nvcc --version
```
# Check cuDNN version
```
cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
```
# Check the usage of GPU devices.
```
nvidia-smi
```
# Install Tensorflow.
```
sudo pip install tensorflow-gpu==1.4
sudo pip3 install tensorflow-gpu==1.4
```
# Set environment variables for CUDA 8.0
```
export PATH=/usr/local/cuda-8.0/bin
export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64
```
[Source](https://gist.github.com/mjdietzx/0ff77af5ae60622ce6ed8c4d9b419f45)

# Install cuDNN v6.0
Install cuDNN v6.0 for installing Tensorflow 1.4.
```
# install cuDNN v6.0
CUDNN_TAR_FILE="cudnn-8.0-linux-x64-v6.0.tgz"
wget http://developer.download.nvidia.com/compute/redist/cudnn/v6.0/${CUDNN_TAR_FILE}
tar -xzvf ${CUDNN_TAR_FILE}
sudo cp -P cuda/include/cudnn.h /usr/local/cuda-8.0/include
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda-8.0/lib64/
sudo chmod a+r /usr/local/cuda-8.0/lib64/libcudnn*
```
[Source](https://gist.github.com/mjdietzx/0ff77af5ae60622ce6ed8c4d9b419f45)

# How do I get the size of a directory on the command line?
```
du -sh <directory_path>
```

# How do I extract a tar.gz or .tgz file?
```
tar xvzf <file>.tar.gz
tar xvzf <file>.tgz
```

# Refresh `.bashrc`
```sh
source $HOME/.bashrc
```
