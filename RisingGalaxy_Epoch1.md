# CFC Studio 共学 Epoch1 指引

---

# RisingGalaxy

> I, who am so lazy, am still learning, what about you?

## Note

### 12.06

Learning time: _next day_ `00:00 - 01:00` | `1 hour`

---

**Summary:**

Simply finished the course overview and shell part of the study, in fact, most of the basic commands before, these days the exam is busy, so today is the end.

However, here is another command line instruction, from the open source project [**tldr** _(too long; don't read)_](https://github.com/tldr-pages/tldr), compared to man, I think this project is more suitable for understanding and learning commands.

> 还是不习惯英文，后续我还是采用中文记录吧。

---

**Practice**

由于使用的是 Linux 虚拟机，Q10 未完成，其它均已完成。

以下简单记录一些注意点：

- Q5: 如果是一行一行地写入，记得使用 `>>` 而不是 `>`
- Q9: `./semester | grep -i '^last-modified:' | cut -d ' ' -f 2- > ~/last-modified.txt`
  可以分为三部分，先将 `semester` 的输出通过管道传递给 `grep`，再将 `grep` 的输出通过管道传递给 `cut`，最后将 `cut` 的输出通过管道传递给 `>`，将结果写入文件。其中 `grep` 的 `-i` 选项表示忽略大小写，`cut` 的 `-d ' '` 选项表示使用空格作为分隔符，`-f 2-` 表示从第二个字段开始输出。

---

### 12.07
