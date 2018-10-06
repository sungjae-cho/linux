Preparing to install Ubuntu.
* Select nothing. Just click `Continue`.
* Click `Continue in UEFI mode`.

Install type.
* Select `Something else`, which means you can create or resize partitions yourself, or choose multiple partitions for Ubuntu.

Select `free space`. Click the `+` button. And set the following.
* Size: 1MB
* Type for the new partition: Primary
* Location for the new partition: Beggining of this space
* Uses as: Reserved BIOS boot area

Select `free space`. Click the `+` button. And set the following.
* Size: 512MB
* Type for the new partition: Primary
* Location for the new partition: Beggining of this space
* Uses as: Ext4 journaling file system
* Mount point: `/boot`

Select `free space`. Click the `+` button. And set the following.
* Size: 65536MB (=64GB=RAM memory size)
* Type for the new partition: Primary
* Location for the new partition: Beggining of this space
* Uses as: swap area

Select `free space`. Click the `+` button. And set the following.
* Size: the size for the working space
* Type for the new partition: Primary
* Location for the new partition: Beggining of this space
* Uses as: Ext4 journaling file system
* Mount point: `/`

Then, click `Install Now`.

Keep choosing `Continue`.

Set your user name and password.

Then, you can start install Ubuntu.

# Set up network

```bash
sudo apt update
```

```bash
sudo apt upgrade
```

```bash
sudo apt install build-essential cmake pkg-config libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev libgtk-3-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libatlas-base-dev gfortran screen
```

```bash
sudo apt-get install python2.7 python-pip python3-pip python-dev python-virtualenv git dkms linux-headers-generic openssh-server vim build-essential python3-tk nodejs npm nodejs-legacy
```

```bash
sudo pip3 install -U pip
```

```bash
sudo pip3 install -U matplotlib scipy numpy scikit-learn atpy astropy pandas readchar JSAnimation opencv-python jupyter jupyterlab pillow
```

Install driver

```bash
wget http://us.download.nvidia.com/XFree86/Linux-x86_64/375.66/NVIDIA-Linux-x86_64-375.66.run
```

```bash
sudo apt-get remove nvidia* && sudo apt autoremove
```

```bash
sudo vim /etc/modprobe.d/blacklist.conf
```
Then, add the followings in the end of the text.

```
blacklist amd76x_edac 
blacklist vga16fb
blacklist nouveau
blacklist rivafb
blacklist nvidiafb
blacklist rivatv
blacklist lbm-nouveau
options nouveau modeset=0
alias nouveau off
alias lbm-nouveau off
```
```bash
echo options nouveau modeset=0 | sudo tee -a /etc/modprobe.d/nouveaukms.conf
sudo update-initramfs -u
reboot
```
`Ctrl+Alt+F1`. Then, login.
```bash
sudo service lightdm stop
```

Install nvidia driver with installing CUDA. 


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
(y)es/(n)o/(q)uit: y

???Something yes or default choice

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

3. Then, 
```bash
sudo apt-get install cuda 
reboot
```

