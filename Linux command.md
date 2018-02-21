
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
apt-get install python-pip	#python 2
apt-get install python3-pip #pytohn 3
```
# Installing Jupyter
Installing Jupyter with `pip`.
If you have Python 3 installed (which we recommended):
```
python3 -m pip install --upgrade pip
python3 -m pip install jupyter
```
If you have Python 2 installed:
```
python -m pip install --upgrade pip
python -m pip install jupyter
```
# Check CUDA version.
```
nvcc --version
```
# Check the usage of GPU devices.
```
nvidia-smi
```
