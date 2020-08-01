# Compression & extraction

## Zip 

1. Move to the parent directory of a directory to zip.
2. Then, type the following command.

```bash
$ tar -czvf zip-file-name.tar.gz dir-to-zip
```

### When you want to see how compression has been proceeded

```bash
$ tar cf - dir-to-zip -P | pv -s $(du -sb dir-to-zip | awk '{print $1}') | gzip > zip-file-name.tar.gz
```

## Unzip

1. Move the parent directory of a directory to unzip.
2. Then, type the following command.

```bash
$ tar -xzvf zip-file-name.tar.gz # for tar extension
```

```bash
$ gzip -d zip-file-name.gz # for gz extension
```

```bash
$ unzip zip-file-name.zip # for zip extension
```

