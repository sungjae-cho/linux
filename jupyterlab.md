# Install jupyter lab
```
sudo pip3 install --upgrade pip
sudo pip3 install jupyterlab
```
[Reference](http://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)

# Setting remote jupyter lab

Download `setup_nbserver_jupyter.py`.

```
wget https://raw.githubusercontent.com/sungjae-cho/linux/master/setup_nbserver_jupyter.py
```

Execute the downloaded python script for installation. 

```
python3 setup_nbserver_jupyter.py
```

After execution, you can specify a port number and a password required to access jupyter lab.

# Execute jupyter lab
```
jupyter lab # case 1: without root permission
sudo juypter lab --allow-root # case 2: with root permission
```
