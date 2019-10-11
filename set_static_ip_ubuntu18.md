## 1. Check ethenets.

```bash
$ ls /sys/class/net
enp0s31f6  lo
```

`enp0s31f6` is the ethernet to be set.

## 2. Change `/etc/netplan/50-cloud-init.yaml`

```bash
sudo vim /etc/netplan/50-cloud-init.yaml
```

Then, change `/etc/netplan/50-cloud-init.yaml` like the followings:

```shell
network:
    ethernets:
        enp0s31f6:
            addresses: [<static-ip>/24]
            gateway4: <gateway-ip>
            nameservers:
              addresses: [8.8.8.8,8.8.4.4]
            dhcp4: no
    version: 2
```

The most important things to be set are ethenet names and `dhcp4: no`.

## 3. Apply the setting.

```bash
sudo netplan apply
```

## 4. Check whether the settings are applied.

```bash
ip addr
ip route
```

## 5. Check whether the network works

```bash
nslookup google.com
```

## Referenes
* [ubuntu 18 LTS 고정 ip 설정(static ip config)](https://www.lesstif.com/pages/viewpage.action?pageId=61899302)
