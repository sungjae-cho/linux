# Install `apex` in Python

Installing `apex` is error-prone. Therefore, it is necessary to record the environment and install commands when the installation is successful.

* Anaconda3: 4.8.5 (installed by `Anaconda3-2019.10-Linux-x86_64.sh`)
  * Python: 3.7.4
  * GCC: GCC 7.3.0
* CUDA: 10.1
* PyTorch: 1.4.0
  * Installation: `conda install pytorch==1.4.0 torchvision==0.5.0 cudatoolkit=10.1 -c pytorch`
* apex: 0.1
  * Installation:
```bash
git clone https://github.com/NVIDIA/apex.git
cd apex
python setup.py install --cuda_ext --cpp_ext
```
