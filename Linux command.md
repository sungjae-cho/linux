
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
sudo apt-get install python-pip	#python 2
sudo apt-get install python3-pip #pytohn 3
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
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install jupyter
```
If you have Python 2 installed:
```
sudo python -m pip install --upgrade pip
sudo python -m pip install jupyter
```

# Uninstall Jupyter
```
sudo pip install pip-autoremove
sudo pip-autoremove jupyter -y
```

# Check CUDA version.
```bash
nvcc --version
```
# Check cuDNN version
```bash
cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
```
# Check the usage of GPU devices.
```
nvidia-smi
```
# Install Tensorflow.
```bash
sudo pip install tensorflow-gpu==1.4
sudo pip3 install tensorflow-gpu==1.4
```
# Set environment variables for CUDA 9.0
```bash
export PATH=/usr/local/cuda-9.2/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-9.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```
[Source](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#post-installation-actions)

# Install cuDNN v7.2
Install cuDNN v7.2 for installing Tensorflow 1.7.

Download 
* `cuDNN v7.2.1 Runtime Library for Ubuntu16.04 (Deb)` 
* `cuDNN v7.2.1 Developer Library for Ubuntu16.04 (Deb)`
* `cuDNN v7.2.1 Code Samples and User Guide for Ubuntu16.04 (Deb)`
from [this page](https://developer.nvidia.com/cudnn).

```bash
sudo dpkg -i libcudnn7_7.2.1.38-1+cuda9.2_amd64.deb
sudo dpkg -i libcudnn7-dev_7.2.1.38-1+cuda9.2_amd64.deb
sudo dpkg -i libcudnn7-doc_7.2.1.38-1+cuda9.2_amd64.deb
```

## Test

First change the `#include "driver_types.h"` as `#include <driver_types.h>` in the file `/usr/include/cudnn.h`.

```bash
cp -r /usr/src/cudnn_samples_v7/ $HOME
cd  $HOME/cudnn_samples_v7/mnistCUDNN
make clean && make
./mnistCUDNN
```

If you see `Test passed!`, then cuDNN should be installed properly.

[Source](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#install-linux)



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
