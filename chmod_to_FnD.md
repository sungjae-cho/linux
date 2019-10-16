
## Change all directories in `.` to have `chmod 775`
```bash
find . -type d -exec chmod 775 {} \;
```

## Change all files in `.` to have `chmod 664`
```bashs
find . -type f -exec chmod 664 {} \;
```

