# 1. What is the difference between `apt-get update` and `apt-get upgrade`?


`apt-get update` updates the list of available packages and their versions, but it does not install or upgrade any packages.

```bash
sudo apt-get update
```

`apt-get upgrade` actually installs newer versions of the packages you have. After updating the lists, the package manager knows about available updates for the software you have installed. This is why you first want to update.

```bash
sudo apt-get upgrade
```

# 2. My packages
```bash
# Process usage viewer
sudo apt-get install htop

# Convert window text to unix text: This is necessary to convert text written in Windows inot text used in Unix.
sudo apt-get install dos2unix
```
