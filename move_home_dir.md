# Moving the home directory to another directory

This command below moves all files and directories in the current home directory to a new directory `/newhome/<username>`. 
Before entering the following command, no process must be run by the user named `<username>`.
```
sudo usermod -d /newhome/<username> -m <username>
```
[Reference](https://stackoverflow.com/a/50481329/4207740)
