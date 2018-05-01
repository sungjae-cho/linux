# What is Debian package installation?
The following webpage well describes what are the Debian package installation and how to manipulate them.
https://askubuntu.com/questions/40779/how-do-i-install-a-deb-file-via-the-command-line

Debian packages named as `*.deb` are manually installed via the `dpkg` command (Debian Package Management System).

## Before using `sudo dpkg -i`
```
sudo apt-get install -f
```
I think this command may install applications forcefully.

## Install a package
```
sudo dpkg -i DEB_PACKAGE
```

## Remove a package
```
sudo dpkg -r PACKAGE_NAME
```
