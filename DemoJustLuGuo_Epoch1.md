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
实际上正确的写法应该是`echo 'mkdir -p "$1"'`(~~~~日常铸币~~~~)

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