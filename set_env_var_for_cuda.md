# Set the enviroment variables `PATH` and `LD_LIBRARY_PATH`.

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
