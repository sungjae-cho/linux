# `scp`: Secure Copy

## 1. Copy a remote directory to a local directory

```bash
scp -r remote_username@10.10.0.2:/remote/directory /local/directory
```

## 2. Copy a local directory to a remote directory

```bash
scp -r /local/directory remote_username@10.10.0.2:/remote/directory
```

## 3. Copy a remote directory to a different remote directory

From `remote1_username@10.10.0.1:/remote1/directory` to `remote2_username@10.10.0.2:/remote/directory`

```bash
scp -r remote1_username@10.10.0.1:/remote1/directory remote2_username@10.10.0.2:/remote2/directory
```
