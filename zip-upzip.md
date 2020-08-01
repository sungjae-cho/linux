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

## What does `tar.gz` stand for?

According to the [Wikipedia page of gzip](https://en.wikipedia.org/wiki/Gzip):
- "gzip is normally used to compress just single files."
- "Compressed archives are typically created by assembling collections of files into a single tar archive (also called tarball), and then compressing that archive with gzip."
- "The final compressed file usually has the extension `.tar.gz` or `.tgz`."

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Targzip.svg/2560px-Targzip.svg.png)

To summarize:
- `tar.gz` compression first gathers files to make them a single data stream, and then compress it with the gzip compression algorithm.

## `tar.gz` vs. `zip`
According to the [Wikipedia page of gzip](https://en.wikipedia.org/wiki/Gzip):
- "The ZIP archive format also uses DEFLATE."
- "The ZIP format can hold collections of files without an external archiver."
- "The ZIP format is less compact than compressed tarballs holding the same data, because it compresses files individually and cannot take advantage of redundancy between files (solid compression)."

To summarize:
- `tar.gz`: (1) Make files a single data stream. (2) Compress it.
- `zip`: (1) Compress files individually. (2) Make them a single file.
