If you want to have both stderr and output displayed on the console and in a file use this:

```bash
SomeCommand 2>&1 | tee SomeFile.txt
```
