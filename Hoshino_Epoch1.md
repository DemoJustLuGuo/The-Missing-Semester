# CFC Studio 共学 Epoch1 指引
---
# Hoshino

> I'm joker king.

## 笔记证明

### 01.06

Study Time: 3h (Allright, I spend most of my time on reading English text, it's so hard for me.)

#### Note

The shell is a textual interface for computer, they allow you to run programs, give them input, and inspect their output in a semi-structured way.

The shell is a programming environment.Running a command in the shell is similar to writing a piece of code that the shell interprets and executes. When a command is entered, the shell searches for an executable program either in the directories listed in the `$PATH` environment variable or in the current directory (if specified explicitly).

#### Exercises

In `shell scripting` and `command-line operations`, the difference between **single quotes**`''` and **double quotes** `""`  lies in how they handle variables, special characters, and escape sequences. 

Everything inside single quotes is treated literally. Variables, escape characters, and special characters are not interpreted; they are taken as plain text.But double quotes allow the interpretation of variables, escape sequences, and command substitutions, while preserving spaces and special characters as part of the string.

![image-20250106220057226](https://minio.drivefly.cn:443/image-hoshino/blog/2025/01/06/image-20250106220057226.png)

This command line performs four operations.Firt, it runs the `./semester` to get some info.Second, `grep` filters the output of `./semester` to include only lines containing the string `last-modified`.Third, `cut` extracts specific fields from the lines filtered by grep(`-d' '` specifies that fields in the line are separated by spaces, `-f2-` instructs cut to output everything from the second field onwards).At last, `>` will  redirect the output of the previous commands to a file named `last-modified.txt`.

![image-20250106220743702](https://minio.drivefly.cn:443/image-hoshino/blog/2025/01/06/image-20250106220743702.png) 
