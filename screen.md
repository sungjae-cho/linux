# How to use `screen` command

## 1. Create a screen session
```bash
screen -S <session_name>
```

## 2. Detach/Escape from the current screen session
Press `Ctrl + a + d`.

## 3. See the list of currently running screen sessions
```bash
screen -ls
```

## 4. Resume to a screen session
Type one of the two following commands.

**Resume with a screen name.**
```bash
screen -r <session_name>
```

**Resume with a screen PID(process ID).**
```bash
screen -r <session_pid>
```


## 5. Kill/Delete a screen.
This command executes kill on a screen session, which is one of processes. Type one of the two following commands.

**With a session name**
```bash
screen -S <session_name> -X kill
```

**With a session PID**
```bash
screen -S <session_pid> -X kill
```
