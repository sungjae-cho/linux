# Partition disks.

Select `free space`. And set the following.
* Size: 512MB
* Uses as: Ext4 journaling file system
* Mount point: `/boot`

Select `free space`. And set the following.
* Size: 65536MB (=64GB=RAM memory size. Just spare the size as eqaul to the RAM size)
* Type for the new partition: Primary
* Uses as: swap area

Select `free space`. And set the following.
* Size: the size for the working space
* Type for the new partition: Primary
* Location for the new partition: Beggining of this space
* Uses as: Ext4 journaling file system
* Mount point: `/`

If you have an additional disk to store data, then follow this:

Select `free space`. And set the following.
* Size: the size for data storage
* Type for the new partition: Primary
* Location for the new partition: Beggining of this space
* Uses as: Ext4 journaling file system
* Mount point: `/data`

# Set static interent connection (optional).

This step is usually required to use internet connection in university.
Follow [this instruction](https://github.com/sungjae-cho/linux/blob/master/set_static_ip_ubuntu18.md).

# Install the CUDA, its toolkit, and NVIDIA driver.

Follow the instructions given in [the NVIDIA homepage (CUDA Toolkit 10.1 Update 2 Download)](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=deblocal).
Install the CUDA through **deb (local)** because the runfile installer may cause [this kind of errors](https://devtalk.nvidia.com/default/topic/1052676/runfile-installer-error-for-cuda-10-1-on-ubuntu-18-04/).

# Setting CUDA envirtonmental variables.

Read [this instruction](https://github.com/sungjae-cho/linux/blob/master/set_cuda_env_var.md).
