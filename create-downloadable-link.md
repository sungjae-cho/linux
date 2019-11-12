Install Apache2

```
sudo apt-get install apache2
```
Place your into file the `/var/www/html` directory (might need root privileges for this)

```
sudo cp yourfile /var/www/html/yourfile
```

Access the file with the following link:

`http://your-ip-address/yourfile`

If your running under a router or firewall, you might have to open port 80 and forward it to your pc.

Reference: [How to create a downloadable public link for files on server](https://stackoverflow.com/questions/10956587/how-to-create-a-downloadable-public-link-for-files-on-server)
