
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
```
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
```
luarocks install cutorch
```

Then, enter the following.
```
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