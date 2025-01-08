# CFC Studio 共学 Epoch1 指引

---

# [DemoJustLuGuo]

## 笔记证明

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

### 01.07

#### 学习时长：50 分钟

安装了 wsl 之后学习完了第一节的内容

基本都是跟着视频在打，蛮不错的，除了 wsl 是虚拟机导致一些内核的改不了之外，其他的没有遇到什么问题。做了课后作业，就先传上来吧，还有一科没考完呢。

> sakuraauro@DemoJustLuGuo:/tmp/$ cd /tmp
> sakuraauro@DemoJustLuGuo:/tmp/$ mkdir missing
> sakuraauro@DemoJustLuGuo:/tmp$ ls
> missing
> snap-private-tmp
> systemd-private-856d00b5580a4e4ab51e9660bc84158c-polkit.service-7eTcE0
> systemd-private-856d00b5580a4e4ab51e9660bc84158c-systemd-logind.service-kBkmIl
> systemd-private-856d00b5580a4e4ab51e9660bc84158c-systemd-resolved.service-uWN9Q6
> systemd-private-856d00b5580a4e4ab51e9660bc84158c-systemd-timesyncd.service-kXJsTp
> systemd-private-856d00b5580a4e4ab51e9660bc84158c-wsl-pro.service-jXoXvM
> sakuraauro@DemoJustLuGuo:/tmp$ cd missing
> sakuraauro@DemoJustLuGuo:/tmp/missing$ touch semester
> sakuraauro@DemoJustLuGuo:/tmp/missing$ ls
> semester
> sakuraauro@DemoJustLuGuo:/tmp/missing$ echo '#!/bin/sh' > semester
> sakuraauro@DemoJustLuGuo:/tmp/missing$ echo 'curl --head --silent https://missing.csail.mit.edu' >> sem
> ester
> sakuraauro@DemoJustLuGuo:/tmp/missing$ cat semester
> #!/bin/sh
> curl --head --silent https://missing.csail.mit.edu.com
> sakuraauro@DemoJustLuGuo:/tmp/missing$ /tmp/missing/semester
> -bash: /tmp/missing/semester: Permission denied
> sakuraauro@DemoJustLuGuo:/tmp/missing$ sudo /tmp/missing/semester
> sudo: /tmp/missing/semester: command not found
> sakuraauro@DemoJustLuGuo:/tmp/missing$ man chmod
> sakuraauro@DemoJustLuGuo:/tmp/missing$ ls -l
> total 8
> drwxr-xr-x 2 sakuraauro sakuraauro 4096 Jan 8 22:18 missing
> -rw-r--r-- 1 sakuraauro sakuraauro 65 Jan 8 22:33 semester
> sakuraauro@DemoJustLuGuo:/tmp/missing$ chmod 777 semester
> sakuraauro@DemoJustLuGuo:/tmp/missing$ ls -l
> total 8
> drwxr-xr-x 2 sakuraauro sakuraauro 4096 Jan 8 22:18 missing
> -rwxrwxrwx 1 sakuraauro sakuraauro 65 Jan 8 22:33 semester
> sakuraauro@DemoJustLuGuo:/tmp/missing$ ./semester
> sakuraauro@DemoJustLuGuo:/tmp/missing$ sudo ./semester(没输出？ 好像还是执行不出来)
> sakuraauro@DemoJustLuGuo:/tmp/missing$ ls -l
> total 8
> drwxr-xr-x 2 sakuraauro sakuraauro 4096 Jan 8 22:18 missing
> -rwxrwxrwx 1 sakuraauro sakuraauro 65 Jan 8 22:33 semester
> sakuraauro@DemoJustLuGuo:/tmp/missing$ cd
> sakuraauro@DemoJustLuGuo:~$ echo '-rwxrwxrwx 1 sakuraauro sakuraauro 65 Jan 8 22:33 semester' > last-modified.txt
> sakuraauro@DemoJustLuGuo:~$ ls -l
> total 8
> drwxr-xr-x 2 sakuraauro sakuraauro 4096 Jan 8 21:10 TEST
> -rw-r--r-- 1 sakuraauro sakuraauro 62 Jan 8 22:41 last-modified.txt
> sakuraauro@DemoJustLuGuo:~$ cd /sys/class/power_supply/BAT1
> sakuraauro@DemoJustLuGuo:/sys/class/power_supply/BAT1$ cat capacity
> 94

感觉自己排版蛮差的，抽空看一下 markdown 的语法吧，现在属于是邯郸学步的阶段。
