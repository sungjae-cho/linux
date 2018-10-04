# Check CUDA version.

```bash
nvcc --version
```

# Check cuDNN version

```bash
cat /usr/include/cudnn.h | grep CUDNN_MAJOR -A 2D
```

# Install CUDA 9.0

It is always desirable to read the [official Installation Guide for Linux](http://developer.download.nvidia.com/compute/cuda/9.0/Prod/docs/sidebar/CUDA_Installation_Guide_Linux.pdf) of the version of CUDA you want to install. In my case, the version is 9.0.

1. Download a runfile(local) install file from the NVIDA homepage.

```bash
sudo sh cuda_9.0.176_384.81_linux.run
```

While running the file, you are asked to install the NVIDIA driver, CUDA toolkit, and example codes. The example codes are just optional. If you already installed a recent NVIDIA driver, the CUDA toolkit is the only thing you should install. Pick the default choices while running.

```bash
Do you accept the previously read EULA?
accept/decline/quit: accept

Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 384.81?
(y)es/(n)o/(q)uit: n

Install the CUDA 9.0 Toolkit?
(y)es/(n)o/(q)uit: y

Enter Toolkit Location
 [ default is /usr/local/cuda-9.0 ]:

Do you want to install a symbolic link at /usr/local/cuda?
(y)es/(n)o/(q)uit: y

Install the CUDA 9.0 Samples?
(y)es/(n)o/(q)uit: n
```

2. Set the enviroment variables `PATH` and `LD_LIBRARY_PATH`.

**Method 1: Setting for a user environment (Recommended!)**

* Type `vim ~/.bashrc`. Add the following in the end of the file.

```bash
export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```
* Then, type the following to run `.bashrc`.
```bash
source ~/.bashrc
```

* Type `vim ~/.bash_profile`. Add `source ~/.bashrc`.

**Method 2: Setting in the Shell environment**

```bash
export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```

**Method 3: Setting accross users**

If you want the directories above to be added globally, add the variables to `/etc/environment`. `/usr/local/cuda-9.0/bin` to `PATH` and `/usr/local/cuda-9.0/lib64` to `LD_LIBRARY_PATH`.

# Set environment variables for CUDA 9.0

```bash
export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```

[Source](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#post-installation-actions)

# Install cuDNN v7.2

Install cuDNN v7.2 for installing Tensorflow 1.7. 

Open [this page](https://developer.nvidia.com/cudnn). First, click  'Download  cuDNN.' Second, login. Then, download the following files. 

* `cuDNN v7.2.1 Runtime Library for Ubuntu16.04 (Deb)` 
* `cuDNN v7.2.1 Developer Library for Ubuntu16.04 (Deb)`
* `cuDNN v7.2.1 Code Samples and User Guide for Ubuntu16.04 (Deb)`


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
