
Open the SSH configuration file `/etc/ssh/sshd_config`.

```
sudo vim /etc/ssh/sshd_config
```

Change `#PermitRootLogin yes` or `#PermitRootLogin no` as `PermitRootLogin yes`.

Then, activate the edited `/etc/ssh/sshd_config`.
```
sudo service sshd restart
```
