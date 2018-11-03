
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

# Check the usage of GPU devices.
```
nvidia-smi
```
# Install Tensorflow.
```bash
sudo pip install tensorflow-gpu==1.4
sudo pip3 install tensorflow-gpu==1.4
```

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

# Merge two directories
```bash
rsync -avhu --progress <source>/ <destination>/
```
[Reference](https://unix.stackexchange.com/questions/149965/how-to-copy-merge-two-directories)

