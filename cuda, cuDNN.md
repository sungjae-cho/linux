# Check CUDA version.
```bash
nvcc --version
```
# Check cuDNN version
```bash
cat /usr/include/cudnn.h | grep CUDNN_MAJOR -A 2D
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
