
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
