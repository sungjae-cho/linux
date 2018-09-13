# UNIX Shell Reminder
## 1 Essential Commands
* echo
* ;
* pwd
* ls
* cd
  * '.' directory, '..' directory, '~' directory
  * '\*', '?' for pattern matching
  * '' single quotes
* mv
* mkdir
* curl
  * curl (-o [file name]) -L [URL]
* cat
* less
* rm
  * rm -i
* rmdir
* grep
  * grep [string] [file_name]
    * Reads the file and print all the lines that have the string.
  * grep [stirng] [file_name] | less
    * Displays the output not on the command screen, but on the another screen.
    * The pipeline '|' means that the result of the left operand feeds the right operand.
  * grep -c [string] [file_name]
    * Returns the number of the strings in the file.
  * grep [string] [file_name] | wc -l
    * Returns the number of the strings in the file.
  * curl -L https://tinyurl.com/zeyq9vc | grep fish
    * Displays all the lines that contains 'fish'
  * curl -L https://tinyurl.com/zeyq9vc | grep fish | wc -l
    * Counts the number of 'fish' in the page.
  * curl -L https://tinyurl.com/zeyq9vc | grep -c fish
    * Counts the number of 'fish' in the page
* variables
  * There are __3 types of variables used in the shell__: local variables, environment variables, and shell variables.
  * numbers='This is a message.'
    * Variable assignment
    * 'numbers' is a __local variable__.
    * A __local variable__ is a variable that is present within the current instance of the shell.
  * echo $numbers
    * Variable
  * unset numbers
    * Deletes the variable 'numbers'
  * echo $LINES x $COLUMNS
    * $LINES and $COLUMNS are called __shell varaibles__.
    * A __shell variable__ is a special variable that is set by the shell and is required by the shell in order to function correctly. 
  * echo $PATH
    * $PATH is called an __environment variable__.
    * An __environment variable__ is available to any child process of the shell.
    * If you try to run a program by entering its name, the shell finds the name in the working directory and the directories stored in PATH variable.
    * The directories in PATH variable are separated by colons ':'.
    * $PATH is searched from beginning to end, with the first matching executable being run.
    * Executables in the current directory '.' are only executed if '.' is in $PATH
  * PATH=$PATH:(new_directory)
    * Add a new directory to PATH.
    * PATH is set to be default after exiting the shell.
  * help(command)
  * screen
    * screen -list
      * See the list of screen processes.
    * screen -S screen_name
      * Start a screen process.
    * kill pid_screen_name
      * You can find the pid of the screen from 'screen -list' command. 
    * Ctrl + A + D
      * Return to the parent screen
      * There exists the only one parent screen. The rest of screens are child screens.

## 2 Other things about the shell
### 2.1 Shell programmging
* A __shell script__ is a file that contains shell commands.
* Writing shell scripts is called __shelling programming__.
* Make \*.sh that contains the set of commands.
* Type ./\*.sh. Then the commands in the file are executed in order.

### 2.2 Customizing the shell. Shell configuration files. Startup files.
* The shell in every terminal you open will run the commands in the file called '.bash_profile'(Mac, Windows) or '.bashrc'(Linux).
* Git Bash in Windows runs '.bash_profile' right after the shell has run.
* I found '.bash_profile' in the directory '/c/Users/{user_name}', which is the home directory of Windows.
* '.bash_profile' and '.bashrc' are hidden. To see hidden files, you should type __ls -l -a__, with -a option.  
* In the Git Bash in Window, '.bash\_profile' is written as follows by default.
  ```
  if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
  ```
* This command runs the file '.bashrc'. Then, by editing '.bashrc' we can set the customized environment.

### 2.3 Shell prompt design
* You can design your prompt as you want. You just put into PS1 how to change the prompt.
  ```
  $ PS1='$ '
  ```
* You can design your prompt in the site http://bashrcgenerator.com/.
* By putting the statement of setting PS1 in '.bashrc', you can use your design as the default setting.
    
### 2.4 Make a long command shorter!
* Using __alias__ command, you can make a long command shorter.
  ```
  $ alias ll='ls -la'
  ```
* Remind ll will be replaced with 'ls -la'. 
* So, you can add arguments of 'ls', for example:
  ```
  $ ll directory
  ```
* It is also possible to make alias as the default setting by putting the commands in '.bashrc'. 
* You can see the list of alias by typing __alias__.
  ```
  $ alias
  alias ll='ls -la'
  ```

# 3 References
* [Shell Workshop | Udacity](https://classroom.udacity.com/courses/ud206)
* [Unix - What is Shells? | Tutorialspoint](https://www.tutorialspoint.com/unix/unix-what-is-shell.htm)

# 4 Further reading
* [The Bash Academy](http://www.bash.academy/)
* [Bash Beginners Guide](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/)
* [Bash Programming HOWTO](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html) 
* [Regexr — Learn Regular Expressions](http://regexr.com/)
