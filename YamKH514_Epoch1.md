# CFC Studio 共学 Epoch1 指引
---
# [YamKH514]

> 一般路过，不必在意

## 笔记证明

### 01.06

Duration of study: 1h \
What did I learn today: The Shell

Try to use English handouts and study note.

` which ` Programe \
Using ` which ` to find out the address which argument you entered.

    ~/The-Missing-Semester$ which which
    /usr/bin/which

今天先到这儿，有几科重量级还要复习 ⊙﹏⊙∥

### 01.08

Duration of study: 1h \
What did I learn today: Using the Shell

A path on the shell is a delimited list of directories \
It separated by ` / ` on Linux or OS X and ` \ `on Windows. \
We can use ` pwd ` to get currented path, ` ls ` to list files and directories on currented path, ` cd ` to change currented working directory. \
Entering ` ls -l /home `, the shell will output:
```bash
ren@ren-VMware-Virtual-Platform:~/The-Missing-Semester$ ls -l /home
total 4
drwxr-x--- 27 ren ren 4096 Jan  8 23:13 ren
```
Using ` -l ` to get more infomation about each file or directory present.
The ` drwxr-x--- ` indicate what permissions the owner of the file (`ren`), the owning group (`ren`), and everyone else respectively have the given permission. \
- ` - ` indicates that the grpup or user does not have the given permission.
- ` w ` indicate ` modify `
- ` r ` indicate ` read `
- ` x ` indicate ` execute `. If you want to enter a directory, you need this permission.

Using `man` programe to get more information about a programe, like:
```bash
$ man ls
```

### 01.09

Duration of study: 1h \
What did I learn today: Using the Shell

Normally, a programe's input and output are both our terminal. We can use `< file` and `> file` to rewire the input and output streams of a program to a file. We can also use `>>` to append to a file.
```bash
ren@ren-VMware-Virtual-Platform:~$ echo hello > hello.txt
ren@ren-VMware-Virtual-Platform:~$ cat hello.txt 
hello
ren@ren-VMware-Virtual-Platform:~$ cat < hello.txt 
hello
ren@ren-VMware-Virtual-Platform:~$ echo world >> hello.txt 
ren@ren-VMware-Virtual-Platform:~$ cat hello.txt 
hello
world
```
The `|` operator lets us "chain" programe such that the output of one is the input of another.
```bash
ren@ren-VMware-Virtual-Platform:~$ ifconfig | grep 192
        inet 192.168.10.134  netmask 255.255.255.0  broadcast 192.168.10.255
```

Homework

```bash
ren@ren-VMware-Virtual-Platform:/tmp$ mkdir missing
ren@ren-VMware-Virtual-Platform:/tmp$ cd ./missing/
ren@ren-VMware-Virtual-Platform:/tmp/missing$ touch semester
ren@ren-VMware-Virtual-Platform:/tmp/missing$ chmod 777 semester
ren@ren-VMware-Virtual-Platform:/tmp/missing$ ./semester | grep last-modified > ~/last-modified.txt
ren@ren-VMware-Virtual-Platform:/tmp/missing$ cat ~/last-modified.txt
last-modified: Sat, 21 Dec 2024 16:53:01 GMT
```

### 01.10

Duration of study: 40min \
What did I learn today: Shell Scripting

Using `foo=bar` to access the value of the variable with `$foo`. Using `foo = bar` will not work, because it will be interpreted as calling the `foo` program with argumenrs `=` and `bar`. \
Using `'` and `"` to define strings, but they are not equivalent. Strings delimited with `'` will not substitute variable value whereas whereas `"` delimited strings will. \
`bash` supports control flow techniques including `if`, `case`, `while` and `for`. It also supports for defining function, like:
```bash
mcd () {
    mkdir -p "$1"
    cd "$1"
}
```
`Bash` uses a veriety of special variables to refer to arguments, error codes, and other relevant variables.
> `$0` - Name of the script
>
> `$1` to `$9` - Arguments to the script. `$1` is the first argument and so on.
>
> `$@` - All the arguments
>
> `$#` - Number of arguments
>
> `$?` - Return code of the previous command
>
> `$$` - Process identification number (PID) for the current script
>
> `!!` - Entire last command, including arguments. A common pattern is to execute a command only for it to fail due to missing permissions; you can quickly re-execute the command with sudo by doing `sudo !!`
>
> `$_` - Last argument from the last command. If you are in an interactive shell, you can also quickly get this value by typing `Esc` followed by `.` or `Alt+.`

### 01.11

Duration of study: 40min \
What did I learn today: Shell Scripting and Shell Tools

When we perform comparisons in bash, try to use double brackets `[[]]` in favor of simple brackets `[]`.It will reduce chances of making mistakes although it can't be portable to `sh`.

What is shell globbing（通配）?
> When launching scripts, you will often want to provide arguments that are similar. Bash has ways of making this easier, expanding expressions by carrying out filename expansion. These techniques are often referred to as shell globbing.
- Wildcards: Using `?` and `*` to match one or any amount of characters respectively.
- Curly braces`{}`: Whenever we have a common substring in a series of commands,wo can use `{}` for bash to expand this automatically.
```bash
mv *{.py,.sh} folder
# Will move all *.py and *.sh files
```

Using `man` command to  learn how to use commands, or using [TLDR pages](https://tldr.sh/) to check example use cases of a command quickly.

Using `find` to find where the file is. Its syntax can sometimes be tricky to remember, so we can use `fd` which is a simple, fast and user-frindly alternative to `find`.
```bash
# Find all directories named src
find . -name src -type d
# Find all python files that have a folder named test in their path
find . -path '*/test/*.py' -type f
# Find all files modified in the last day
find . -mtime -1
# Find all zip files with size in range 500k to 10M
find . -size +500k -size -10M -name '*.tar.gz'
# Delete all files with .tmp extension
find . -name '*.tmp' -exec rm {} \;
# Find all PNG files and convert them to JPG
find . -name '*.png' -exec convert {} {}.jpg \;
```

Using `grep`, `ack`, `ag` and `rg` to find code.

