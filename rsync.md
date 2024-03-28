# `rsync`

## Basic
```bash
rsync <option> <source> <destination> 
```
Major options
 - a: archive files and directory while synchronizing
 - z: compress file data during the transfer
 - v: verbose output
 - h: display the output numbers in a human-readable format

## Local to Local
```bash
rsync -azvh /source/project_dir/source_dir/ /destination/project_dir/
```

## Local to Remote
```bash
rsync -avz /source/project_dir/source_dir/ lesstif@example.com:/destination/project_dir/
```

## Remote to Local
```bash
rsync -avz lesstif@example.com:/source/project_dir/source_dir/ /destination/project_dir/
```

## Progress bar option

```bash
--progress # Show the progress of each file
--progress --stats # Show the statistics of the whole process
```

## References
- [rsync 사용법 - data backup 포함](https://www.lesstif.com/system-admin/rsync-data-backup-12943658.html)
- [17 useful rsync (remote sync) Command Examples in Linux](https://www.linuxtechi.com/rsync-command-examples-linux/)
