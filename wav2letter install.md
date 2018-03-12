
# 3rd trial
Update your .bashrc file with the following:
```sh
# We assume Torch will be installed in $HOME/usr.
# Change according to your needs.
export PATH=$HOME/usr/bin:$PATH

# This is to detect MKL during compilation
# but also to make sure it is found at runtime.
INTEL_DIR=/opt/intel/lib/intel64
MKL_DIR=/opt/intel/mkl/lib/intel64
MKL_INC_DIR=/opt/intel/mkl/include

if [ ! -d "$INTEL_DIR" ]; then
    echo "$ warning: INTEL_DIR out of date"
fi
if [ ! -d "$MKL_DIR" ]; then
    echo "$ warning: MKL_DIR out of date"
fi
if [ ! -d "$MKL_INC_DIR" ]; then
    echo "$ warning: MKL_INC_DIR out of date"
fi

# Make sure MKL can be found by Torch.
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$INTEL_DIR:$MKL_DIR
export CMAKE_LIBRARY_PATH=$LD_LIBRARY_PATH
export CMAKE_INCLUDE_PATH=$CMAKE_INCLUDE_PATH:$MKL_INC_DIR
```

Type the following to update `.bashrc` to the terminal.
```sh
source $HOME/.bashrc
```

Install LuaJIT + LuaRocks.
```sh
git clone https://github.com/torch/luajit-rocks.git
cd luajit-rocks
mkdir build; cd build
cmake .. -DCMAKE_INSTALL_PREFIX=$HOME/usr -DWITH_LUAJIT21=OFF
make -j 4
make install
cd ../..
```

KenLM Language Model Toolkit
KenLM requires Boost.
Install Boost.
```sh
sudo apt-get install libboost-dev libboost-system-dev libboost-thread-dev libboost-test-dev
```

Install KenLM.
```sh
wget https://kheafield.com/code/kenlm.tar.gz
tar xfvz kenlm.tar.gz
cd kenlm
mkdir build && cd build
cmake .. -DCMAKE_INSTALL_PREFIX=$HOME/usr -DCMAKE_POSITION_INDEPENDENT_CODE=ON
make -j 4
make install
cp -a lib/* ~/usr/lib # libs are not installed by default :(
cd ../..
```

Install OpenMPI.
```sh
wget https://www.open-mpi.org/software/ompi/v2.1/downloads/openmpi-2.1.2.tar.bz2
tar xfj openmpi-2.1.2.tar.bz2
cd openmpi-2.1.2; mkdir build; cd build
../configure --prefix=$HOME/usr --enable-mpi-cxx --enable-shared --with-slurm --enable-mpi-thread-multiple --enable-mpi-ext=affinity,cuda --with-cuda=/usr/local/cuda
make -j 20 all
make install
```

Install TorchMPI.
```sh
MPI_CXX_COMPILER=$HOME/usr/bin/mpicxx ~/usr/bin/luarocks install torchmpi
```

I met the error like the following.
```sh
/tmp/luarocks_torchmpi-scm-1-6079/TorchMPI/lib/detail/reduce_kernel.cu:1:17: fatal error: THC.h: No such file or directory
```

Based on [this article](https://github.com/torch/cunn/issues/407), install `cuTorch`.
```sh
luarocks install cutorch
```

Then, enter the following.
```sh
MPI_CXX_COMPILER=$HOME/usr/bin/mpicxx ~/usr/bin/luarocks install torchmpi
```

Error messages
```sh
pp.o
Linking CXX shared module libtorchmpi.so
/usr/bin/ld: cannot find -lnccl_static
collect2: error: ld returned 1 exit status
make[2]: *** [lib/libtorchmpi.so] Error 1
make[1]: *** [lib/CMakeFiles/torchmpi.dir/all] Error 2
make: *** [all] Error 2

Error: Build error: Failed building.
```

I think NCCL is required.
So, I installed NCCL based on [this page](http://docs.nvidia.com/deeplearning/sdk/nccl-install-guide/index.html#down).
You can download NCCL from [this page](https://developer.nvidia.com/nccl/nccl-download) after you register the page with your email.
Because my CUDA and Ubuntu versions are 8.0 and 14.04, I downloaded 'NCCL 2.1.15 for Ubuntu 14.04 and CUDA 8', which is a local version.
Then, download file. Then, I got the file `nccl-repo-ubuntu1404-2.1.15-ga-cuda8.0_1-1_amd64.deb`.
Then, install the file.
```sh
sudo dpkg -i nccl-repo-ubuntu1404-2.1.15-ga-cuda8.0_1-1_amd64.deb
```
Then, update `apt-get`.
```sh
sudo apt update
```
Then, install `libnccl2` and `libnccl-dev`.
```sh
sudo apt install libnccl2 libnccl-dev
```
Now the installation of NCCL is over.

Then, try again the following command for installing TorchMPI.
```sh
MPI_CXX_COMPILER=$HOME/usr/bin/mpicxx ~/usr/bin/luarocks install torchmpi
```
I got a success result.

## Torch and other Torch packages
Install Torch and other Torch packages.

```sh
luarocks install torch
luarocks install cudnn # for GPU support
luarocks install cunn # for GPU support
```
The results of the three lines were all successful.

## wav2letter packages
```sh
cd ~
git clone https://github.com/facebookresearch/wav2letter.git
cd wav2letter
```
```sh
cd gtn && luarocks make rocks/gtn-scm-1.rockspec && cd ..
```
I met the follwing error message.
```sh
CMake Error at /usr/share/cmake-2.8/Modules/FindPackageHandleStandardArgs.cmake:      108 (message):
  Could NOT find FFTW (missing: FFTW_INCLUDES FFTW_LIBRARIES)
```
I should have install FFTW library.



```sh
cd speech && luarocks make rocks/speech-scm-1.rockspec && cd ..
cd torchnet-optim && luarocks make rocks/torchnet-optim-scm-1.rockspec && cd ..
cd wav2letter && luarocks make rocks/wav2letter-scm-1.rockspec && cd ..
# Assuming here you got KenLM in $HOME/kenlm
# And only if you plan to use the decoder:
cd beamer && KENLM_INC=$HOME/kenlm luarocks make rocks/beamer-scm-1.rockspec && cd ..
```
