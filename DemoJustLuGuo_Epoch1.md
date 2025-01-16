# CFC Studio 共学 Epoch1 指引

---

# [DemoJustLuGuo]

## 笔记证明

<!-- Content_START --> 

### 01.06

#### 学习时长：50 分钟

跟着视频在进行基本命令行的学习 (使用 powershell)

在运行 ls -l 命令时 powershell 突然报错：

> Get-ChildItem: Missing an argument for parameter 'LiteralPath'. Specify a parameter of type 'System.String[]' and try again.

百度后发现错误是因为 Powershell 使用-LiteralPath，因为该选项与-l 匹配，但它需要一个参数。（这里应该是 windows 与 linux 命令使用的差异导致的）
查阅命令帮助后发现 powershell 可直接使用 ls 或 dir、gci 等命令列出文件目录

> 或者使用 ls -Path 'C:\Users\YourUsername\Documents'

在此之前使用查看环境变量 echo $PATH命令也遇到了同样的问题，不过在经过弹幕提醒后知道了windows的powershell使用的是$env:path 命令

总结：最近的时间比较紧，今天就先看到这里，使用 powershell 的原因是我忽视了 windows 与 linux 之间的区别，在学习之时被这些奇妙错误搞麻了，目前已老实安装 bash，等考试完后会补上接下来的课程的。

### 01.08

#### 学习时长：50 分钟

安装了 wsl 之后学习完了第一节的内容

基本都是跟着视频在打，蛮不错的，除了 wsl 是虚拟机导致一些内核的改不了之外，其他的没有遇到什么问题。做了课后作业，就先传上来吧，还有一科没考完呢。

```bash
 sakuraauro@DemoJustLuGuo:/tmp/$ cd /tmp
 sakuraauro@DemoJustLuGuo:/tmp/$ mkdir missing
 sakuraauro@DemoJustLuGuo:/tmp$ ls
missing
snap-private-tmp
systemd-private-856d00b5580a4e4ab51e9660bc84158c-polkit.service-7eTcE0
systemd-private-856d00b5580a4e4ab51e9660bc84158c-systemd-logind.service-kBkmIl
systemd-private-856d00b5580a4e4ab51e9660bc84158c-systemd-resolved.service-uWN9Q6
systemd-private-856d00b5580a4e4ab51e9660bc84158c-systemd-timesyncd.service-kXJsTp
systemd-private-856d00b5580a4e4ab51e9660bc84158c-wsl-pro.service-jXoXvM
  sakuraauro@DemoJustLuGuo:/tmp$ cd missing
  sakuraauro@DemoJustLuGuo:/tmp/missing$ touch semester
  sakuraauro@DemoJustLuGuo:/tmp/missing$ ls
semester
  sakuraauro@DemoJustLuGuo:/tmp/missing$ echo '#!/bin/sh' > semester
  sakuraauro@DemoJustLuGuo:/tmp/missing$ echo 'curl --head --silent https://missing.csail.mit.edu' >> sem
ester
  sakuraauro@DemoJustLuGuo:/tmp/missing$ cat semester
#!/bin/sh
curl --head --silent https://missing.csail.mit.edu.com
  sakuraauro@DemoJustLuGuo:/tmp/missing$ /tmp/missing/semester
-bash: /tmp/missing/semester: Permission denied
  sakuraauro@DemoJustLuGuo:/tmp/missing$ sudo /tmp/missing/semester
sudo: /tmp/missing/semester: command not found
  sakuraauro@DemoJustLuGuo:/tmp/missing$ man chmod
  sakuraauro@DemoJustLuGuo:/tmp/missing$ ls -l
total 8
drwxr-xr-x 2 sakuraauro sakuraauro 4096 Jan 8 22:18 missing
-rw-r--r-- 1 sakuraauro sakuraauro 65 Jan 8 22:33 semester
  sakuraauro@DemoJustLuGuo:/tmp/missing$ chmod 777 semester
  sakuraauro@DemoJustLuGuo:/tmp/missing$ ls -l
total 8
drwxr-xr-x 2 sakuraauro sakuraauro 4096 Jan 8 22:18 missing
-rwxrwxrwx 1 sakuraauro sakuraauro 65 Jan 8 22:33 semester
  sakuraauro@DemoJustLuGuo:/tmp/missing$ ./semester
  sakuraauro@DemoJustLuGuo:/tmp/missing$ sudo ./semester(没输出？ 好像还是执行不出来)
  sakuraauro@DemoJustLuGuo:/tmp/missing$ ls -l
total 8
drwxr-xr-x 2 sakuraauro sakuraauro 4096 Jan 8 22:18 missing
-rwxrwxrwx 1 sakuraauro sakuraauro 65 Jan 8 22:33 semester
  sakuraauro@DemoJustLuGuo:/tmp/missing$ cd
  sakuraauro@DemoJustLuGuo:~$ echo '-rwxrwxrwx 1 sakuraauro sakuraauro 65 Jan 8 22:33 semester' > last-modified.txt
  sakuraauro@DemoJustLuGuo:~$ ls -l
total 8
 drwxr-xr-x 2 sakuraauro sakuraauro 4096 Jan 8 21:10 TEST
-rw-r--r-- 1 sakuraauro sakuraauro 62 Jan 8 22:41 last-modified.txt
  sakuraauro@DemoJustLuGuo:~$ cd /sys/class/power_supply/BAT1
  sakuraauro@DemoJustLuGuo:/sys/class/power_supply/BAT1$ cat capacity
94
```
### 01.10

#### 学习时长：1小时

Bash 中的字符串通过 ' 和 " 分隔符来定义，但是它们的含义并不相同。以 ' 定义的字符串为原义字符串，其中的变量不会被转义，而 " 定义的字符串会将变量值进行替换。

>  foo=bar
>
>  echo "$foo"
> 
>  打印 bar
> 
>  echo '$foo'
> 
>  打印 $foo

自己实操的时候没有正确理解这段话
在执行 `echo "mkdir -p "$1""` 时一直奇怪为什么输出只有 `mkdir -p`
实际上正确的写法应该是`echo 'mkdir -p "$1"'`(~~日常铸币~~)

___

这章还讲到了 &&（与操作符） 和 ||（或操作符）  两种运算符，我具体的实操是这样的

```bash
sakuraauro@DemoJustLuGuo:~/TEST$ true || echo 123
sakuraauro@DemoJustLuGuo:~/TEST$ echo $?
0                        ##true返回0，即执行前一个命令成功
sakuraauro@DemoJustLuGuo:~/TEST$ false || echo 123
123                      ##false返回1，即执行前一个命令失败，将执行后一个命令
sakuraauro@DemoJustLuGuo:~/TEST$ true && echo 123
123                      ##true返回0即执行成功，将执行后一个命令
sakuraauro@DemoJustLuGuo:~/TEST$ false && echo 123
sakuraauro@DemoJustLuGuo:~/TEST$ echo $?
1                        ##false返回1即执行失败，不会执行后一个命令
```

___

还讲到了三种通配符，个人实操了一遍感觉确实有助于提升效率。这里就先把它列出来

>1.当你想要利用通配符进行匹配时，你可以分别使用 ? 和 * 来匹配一个或任意个字符。例如，对于文件 foo, foo1, foo2, foo10 和 bar, rm foo? 这条命令会删除 foo1 和 foo2 ，而 rm foo* 则会删除除了 bar 之外的所有文件。
>
>2.花括号 {} - 当你有一系列的指令，其中包含一段公共子串时，可以用花括号来自动展开这些命令。这在批量移动或转换文件时非常方便。

下面是我的示例

```bash
sakuraauro@DemoJustLuGuo:~/TEST$ touch test{1..9}.txt ##创建名为test1到test9的txt文件
sakuraauro@DemoJustLuGuo:~/TEST$ ls
change.sh    hi.txt     test2.txt  test5.txt  test8.txt
document.sh  more       test3.txt  test6.txt  test9.txt
hello.txt    test1.txt  test4.txt  test7.txt
sakuraauro@DemoJustLuGuo:~/TEST$ rm test?.txt  ##删除所有带test(x).txt的文件（好像只在10以内有效？）
sakuraauro@DemoJustLuGuo:~/TEST$ ls
change.sh  document.sh  hello.txt  hi.txt  more
```

以下是另一个示例
```bash
sakuraauro@DemoJustLuGuo:~/TEST$ touch test{1..11}.txt  ##创建名为test1到test11的txt文件
sakuraauro@DemoJustLuGuo:~/TEST$ ls
change.sh    hi.txt     test10.txt  test3.txt  test6.txt  test9.txt
document.sh  more       test11.txt  test4.txt  test7.txt
hello.txt    test1.txt  test2.txt   test5.txt  test8.txt
sakuraauro@DemoJustLuGuo:~/TEST$ rm test?.txt  ##删除所有带test(x).txt的文件
sakuraauro@DemoJustLuGuo:~/TEST$ ls
change.sh    hello.txt  more        test11.txt
document.sh  hi.txt     test10.txt  ##这里test10.txt和test11.txt并没有被删除
sakuraauro@DemoJustLuGuo:~/TEST$ rm test??.txt
sakuraauro@DemoJustLuGuo:~/TEST$ ls
change.sh  document.sh  hello.txt  hi.txt  more  ##把?换成??就可以删除掉了
```
另外，使用`rm test*.txt`命令应该会更方便，不过看使用场景吧。

### 01.12

#### 学习时长：1小时

先补上上一节的作业
```bash

#!/bin/bash

 export new_workspace=""

 marco(){
         new_workspace=$(pwd)
 }

 polo(){
         cd "$new_workspace"
 }
 
 下面是终端输出
 
 sakuraauro@DemoJustLuGuo:~/afterwork$ marco marco.sh
sakuraauro@DemoJustLuGuo:~/afterwork$ cd
sakuraauro@DemoJustLuGuo:~$ polo
sakuraauro@DemoJustLuGuo:~/afterwork$
```

```bash
#!/usr/bin/env bash  

 standard_out="standard_out.txt"
 standard_error="standard_error.txt"
 success_count=0
 while true;do
          n=$(( RANDOM % 100 ))

 if [[ n -eq 42 ]]; then
    echo "Something went wrong" >> "$standard_out"
    >&2 echo "The error was using magic numbers" >> "$standard_error"
    exit 1
 fi

 echo "Everything went according to plan" >> "$standard_out"
 if [ $? -ne 0 ]; then  
        echo "脚本在失败前共运行了 $success_count 次"
        break
   fi
    ((success_count++))
done

cat "$standard_out"
cat "$standard_error"
```

学习了vim编辑器的使用
基本上 vim 共分为这几种模式：
1.正常模式：在文件中四处移动光标进行修改
2.插入模式：插入文本
3.替换模式：替换文本
4.可视化模式（一般，行，块）：选中文本块
5.命令模式：用于执行命令

下面是一些从讲义上摘抄下来的内容，上手这个还是需要点时间的，抄下来方便自己查看

>你可以按下 <ESC>（退出键）从任何其他模式返回正常模式。在正常模式，键入 i 进入插入 模式，R 进入替换模式，v 进入可视（一般）模式，V 进入可视（行）模式，<C-v> （Ctrl-V, 有时也写作 ^V）进入可视（块）模式，: 进入命令模式。

___

>在正常模式下键入 : 进入命令行模式。 在键入 : 后，你的光标会立即跳到屏幕下方的命令行。 这个模式有很多功能，包括打开，保存，关闭文件，以及 退出 Vim。
>
>:q 退出（关闭窗口）
>
>:w 保存（写）
>
>:wq 保存然后退出
>
>:e {文件名} 打开要编辑的文件
>
>:ls 显示打开的缓存
>
>:help {标题} 打开帮助文档

___

>基本移动: hjkl （左， 下， 上， 右）     **卧槽这个左下上右太抽象了，哪怕左上下右也行啊**
>
>行： 0 （行初）， ^ （第一个非空格字符）， $ （行尾）
>
>翻页： Ctrl-u （上翻）， Ctrl-d （下翻）
>
>i 进入插入模式
>
>但是对于操纵/编辑文本，不单想用退格键完成
>
>比如 d{移动命令} 再 i
>
>x 删除字符（等同于 dl）
>
>s 替换字符（等同于 xi） 
>
>更多值得学习的: 比如 ~ 改变字符的大小写

___

### 01.13

#### 学习时长：1小时

本节课讲的内容是使用ssh获取远程服务器的日志文件，通过搜索、过滤来找到并整理需要的数据
说实话这一节讲的内容有点密了，这里就先整理出自己认为有用的

sed编辑器

主要是运用s（替换命令）。s 命令的语法如下：s/REGEX/SUBSTITUTION/, 其中 REGEX 部分是我们需要使用的正则表达式，而 SUBSTITUTION 是用于替换匹配结果的文本。

正则表达式

>. 除换行符之外的 “任意单个字符”
>
>* 匹配前面字符零次或多次
>
>+ 匹配前面字符一次或多次
>
>[abc] 匹配 a, b 和 c 中的任意一个
>
>(RX1|RX2) 任何能够匹配 RX1 或 RX2 的结果
>
>^ 行首
>
>$ 行尾

sed 的正则表达式有些时候是比较奇怪的，它需要你在这些模式前添加 \ 才能使其具有特殊含义。或者，您也可以添加 -E 选项来支持这些匹配。~~（你怎么知道我刚刚实操就被坑了）~~

感觉就这些需要重点记一下（其实是后面用方便直接打开看，就不用一个个点网页看语法使用示例了），其他的看了但是总感觉云里雾里的，说实话还是更喜欢把自己的实操记录的输出复制上来，可以更直观的看到我写了什么，为什么这么写。

~~（还有感觉这正则表达式不像是人发明出来的）~~

### 01.14

##### 学习时长：1小时

shell在执行一些命令时会出现响应慢的情况
使用`ctrl+c`可以停止命令的执行，它的本质是给进程发送了一个信号以改变其执行。
结束进程的信号还包括`SIGINT`(CTRL+C) `SIGQUIT`(CTRL+\) `SIGTERM`(kill -TERM <PID>)

不仅如此，信号机制中还有`SIGSTOP`(CTRL+Z)以暂停进程的信号，我们可以使用 fg 或 bg 命令恢复暂停的工作。它们分别表示在前台继续或在后台继续。

终端多路复用常用的复用器是`tmux`,使用tmux可以同时运行多个任务，或者一边运行编辑器一边运行程序。tmux常用的快捷键都是以`CTRL+B`起手，`X`结束的，这里就先列举几个自己感觉常用的吧

- mux 开始新会话
- tmux new -s NAME 以指定名称开始一个新会话
- tmux ls 列出当前所有会话
- 在 tmux 中输入 <C-b> d ，将当前会话分离
- c 创建一个新窗口，使用 <C-d> 关闭
- <C-b> N 跳转到第 N 个窗口

别名：
一些常用的命令可以使用别名来代替输入，感觉跟之前讲到的 脚本差不多，不同的是脚本声明一个函数，然后通过`source`命令加载，别名是通过`alias`命令定义的，而且应该一次只能定义一个长命令
在默认情况下 shell 并不会保存别名。为了让别名持续生效，需要将配置放进shell的启动文件里，像是 .bashrc 或 .zshrc

感觉这节主要还是以演示居多吧，所以就先写到这里。今天主要就是给wsl装了个可视化界面  ~~（虽然我觉得并不好看）~~  总结就是摸了。

### 01.15

#### 学习时长：90分钟

今天为了试一下ssh的使用，给家里不用的老电脑也安装了wsl（别问我为什么也安装wsl，问就是没那么多空间）

安装了wsl后，在初次启动时并没有弹出设置用户的提示，而是直接以root权限进入了
这里需要创建自己的用户名
通过`adduser`命令设置，这时会让你输入密码，之后就一堆巴拉巴拉的没用的个人信息，我全跳过了
然后使用`vim`命令编辑`/etc/sudoers`,在打开的配置文件中，找到root ALL=(ALL:ALL) ALL 在下面添加刚设的用户名加上ALL=(ALL:ALL)ALL 就可以
还可以通过`cat /etc/passwd |grep 用户名` 来验证自己的配置是否被正确保存了

接下来就是使用ssh命令了，使用`ssh ip地址`后弹出

>ssh: connect to host 192.168.1.5 port 22: Connection refused

这是由于wsl并没有内置`openssh-server`，就需要执行`sudo app-get install openssh-server`以安装

安装之后我们再执行ssh命令，我们会惊奇的发现：

>connect to host 192.168.1.5 port 22: Connection refused
>
>哈哈，还是不行
>

别急，因为ssh服务妹有启动，这时我们执行` /etc/init.d/ssh start`之后就可以了

注意的是一定要`ssh 该系统上存在的用户名@ip地址 `才可以，为什么这么说呢，你猜是谁直接输ip地址最后输密码输到怀疑人生。

哦对，还有个公钥登录的方法，简单来说就是使用`ssh-keygen`命令生成一个公钥，再用`ssh-copy-id 用户名@ip地址`发送到目标主机后。之后再用ssh登录就不用输入密码了。

搞完这一套步骤，不出意外你就可以享受ssh带来的便利了。

这里贴一点自己的操作

```bash
sakuraauro@DemoJustLuGuo:~$ ssh 192.168.1.5
ssh: connect to host 192.168.1.5 port 22: Connection refused #这里是刚开始尝试
sakuraauro@DemoJustLuGuo:~$ sudo apt-get install openssh-server
（省略掉输出）
sakuraauro@DemoJustLuGuo:~$ /etc/init.d/ssh start
Starting ssh (via systemctl): ssh.serviceFailed to start ssh.service: Interactive authentication required.
See system logs and 'systemctl status ssh.service' for details.
 failed!    #这里的意思好像是执行失败了，我没懂，所以我接下来准备看一下ssh服务的状态
sakuraauro@DemoJustLuGuo:~$ systemctl status ssh.service
○ ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/usr/lib/systemd/system/ssh.service; disabled; preset: enabled)
     Active: inactive (dead)      #ssh服务被加载了，但是并不在活跃状态？我试试看能不能跑
TriggeredBy: ● ssh.socket
       Docs: man:sshd(8)
             man:sshd_config(5)  
```
---
```bash             
sakuraauro@DemoJustLuGuo:~$ ssh 192.168.1.5
The authenticity of host '192.168.1.5 (192.168.1.5)' can't be established.
ED25519 key fingerprint is SHA256:(省略掉).
sakuraauro@192.168.1.5's password:
Permission denied, please try again.
sakuraauro@192.168.1.5's password:
Permission denied, please try again.
sakuraauro@192.168.1.5's password:
sakuraauro@192.168.1.5: Permission denied (publickey,password). #这里输了好几次密码但是没有成功，我有点自我怀疑了。
```
---
```bash
sakuraauro@DemoJustLuGuo:~$ ssh shimarin@192.168.1.5
shimarin@192.168.1.5's password:
Welcome to Ubuntu 24.04.1 LTS (GNU/Linux 4.4.0-19041-Microsoft x86_64)
（下面是一些状态信息，直接省略掉）
shimarin@WINPC-xxxxxxxx:~$     #前缀变成了另一台电脑的用户名及名字，ssh连接成功了，下面用logout断开连接
shimarin@WINPC-906291016:~$ logout
Connection to 192.168.1.5 closed.
```


<!-- Content_END -->