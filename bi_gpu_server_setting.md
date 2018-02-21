# To install
* Install Jupyter notebook.
* Tensorflow 1.4.0 of Python 2 and Python 3.

# 1. Basic commands
## 1.1. Update the `apt-get` package.
```
sudo apt-get update
```

## 1.2. Install or update `pip` and `pip3`.
```
sudo apt-get install python-pip	  # python 2
sudo apt-get install python3-pip   # python 3
```

# 2. Install Juypter

## 2.1. Install Juypter
Installing Jupyter with `pip`.
If you have Python 3 installed (which we recommended):
```
sudo python3 -m pip install jupyter
```
If you have Python 2 installed:
```
sudo python -m pip install jupyter
```
## 2.3. Install or update `ipython`.
```
sudo apt-get install ipython2
sudo apt-get install ipython3
```

## 2.2. Make Python 2 and Python 3 available in Jupyter
```
sudo python2 -m pip install -U ipykernel
sudo python2 -m ipykernel install --user
sudo python3 -m pip install -U ipykernel
sudo python3 -m ipykernel install --user
```

# 3. Install Tensorflow

## 3.1. Set environment variables for CUDA 8.0
```
export PATH=/usr/local/cuda-8.0/bin
export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64
```

## 3.2. Install cuDNN v6.0
Install cuDNN v6.0 for installing Tensorflow 1.4.
```
CUDNN_TAR_FILE="cudnn-8.0-linux-x64-v6.0.tgz"
wget http://developer.download.nvidia.com/compute/redist/cudnn/v6.0/${CUDNN_TAR_FILE}
tar -xzvf ${CUDNN_TAR_FILE}
sudo cp -P cuda/include/cudnn.h /usr/local/cuda-8.0/include
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda-8.0/lib64/
sudo chmod a+r /usr/local/cuda-8.0/lib64/libcudnn*
```

## 3.3. Install the lastest `tensorflow-gpu`
```
sudo pip install --upgrade tensorflow-gpu  # for Python 2.7 and GPU
sudo pip3 install --upgrade tensorflow-gpu # for Python 3.n and GPU
```

## 3.4. Install `tensorflow-gpu` in version 1.4
```
sudo pip install tensorflow-gpu==1.4
sudo pip3 install tensorflow-gpu==1.4
```

## 3.5. Check
```
python
>>> import tensorflow as tf
>>> tf.__version__
```
```
python3
>>> import tensorflow as tf
>>> tf.__version__
```
