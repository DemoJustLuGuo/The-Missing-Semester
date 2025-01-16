# CFC Studio 共学 Epoch1 指引
---
# [ArchSerein]

> 通过共学计划完成 cs162 的剩余实验和学习 cmu18447

## 笔记证明

> 下面的日期请保证至少两个字符占位
>
>   * 正确：12.06
>   * 错误：12.6
>
> 若当天没有学习内容，请直接跳过该日期的记录，不要在日期下记录：“请假” 等内容

### 12.06

举例示范：

今日学习时间：XXXX
学习内容小结：XXXX
Homework 部分（如果有安排需要填写证明完成）
Question and Ideas（有什么疑问/或者想法，可以记在这里，也可以分享到群里讨论交流）

<!-- Content_START --> 
### 01.06

> 今日学习时间：

> 3h

> 今日学习任务：

> reading -> Multiprocessor Benchmarks and Performance Models

> 学习内容小结：

> in this subsection, the main discussion is about evaluating processor performance through benchmarking. But due to such traditional restrictions to benchmark is chiefly limited to the architecture and compiler, better data structuers and algorithms maybe give a misleading result. Then, ucbidentified 13 design patterns that they will be part of applications of the future. Next, the main discussion of The Roofline Model, how to use it to find performance bottlenecks and how to optimize the processor. How to reduce computational bottlenecks: mix floating-point operation, improve inst-level parallelism and apply SIMD; How to reduce memory bottlenecks: software prefetching and memory affinity.

> Question and Ideas（有什么疑问/或者想法，可以记在这里，也可以分享到群里讨论交流）

> a description of The Roofline Models is at the link [the roofline models wiki](https://en.wikipedia.org/wiki/Roofline_model)

### 01.07

> 今日学习时间：

> 3h

> 今日学习任务：

> Completing the file system buffer cache

> 学习内容小结：

> The original pintos implementation of the file system, when it performs read/write operations, that will directly access the file system's underlying block device. Now, I need to add a buffer cache for the file system.

> the buffer cache structure I designed is:
```
struct buf {
  int cnt;
  bool dirty;
  struct block *dev;
  block_sector_t blockno;
  struct list_elem elem;
  uint8_t data[BLOCK_SECTOR_SIZE];
};
/**
* cnt: number of references to the current buffer 
* dirty: when data is only written to the buffer and not synchronized to disk, dirty is true, otherwise false
* dev: maybe always fs_device, but like fsutil.c use other device, maybe they don't need the buffer cache
* blockno: sector number, the position of read/write
* elem: list element, Data Structures for Bidirectional Chained Tables
* data: the data aera of buffer
**/
```
> when pintos need to read/write, it will use bread/bwrite, not block_read/block_write. block_read/block_write will be used in the bread/bwrite, when caching missing. If there are no free cache blocks, the LRU algorithm will be used to replace the one that meets the requirement. You need to make sure that ditry is set before replacing it, and if it is true you need to write it back to disk and replace it.

### 01.08

> 今日学习时间：

> 4.5h

> 今日学习任务：

> Synchronize the modified contents of the buffer to disk in the idle thread, add cwd records to the pcb, and add directory support to the filesystem (partial implementation).

> 学习内容小结：

> The cwd in pcb records the inode, but in userproc only inode structure declaration and can not access to the actual data in the inode, at first thought of how to make userproc only contain inode header file on struct inode definition but has not been successful, later in rtfsc when found in the file system Then I found out in rtfsc that there is a layer of abstraction in the file system and it provides a way to get the inode (you need to add a helper function yourself).

> As far as directory support is concerned, it is currently just an update of the lookup function originally provided by pintos.

> Regarding the synchronization of data in the buffer to disk, the manual says that this is achieved by non-busy-wait sleep, but I don't have much of an idea, so I just synchronize when the current resource is free, i.e., when the idle thread is running.

> Finally, I used the originally unused area of the inode_disk to implement the file extension support

> However, I felt that the design idea was not perfect and needed a lot of modification.

### 01.09

> 今日学习时长

> 6h

> 今日学习任务

> Added support for all directory-related system calls and filesystems, though there are still issues

> 学习内容小结

> Even if you have a simple idea before implementation, but when you implement it according to your own thinking, because you don't have enough rtfsc, it will lead to some processes are not well implemented or even have conflicts, then you have to re-conceptualize and change your thinking, but the source code of pintos is still relatively complex, then I am stuck in a loop, I hope to finish it soon!

> commit log: [01.09](https://github.com/crazyofcode/cs162/commit/cc3a71d28370b9c9da209a12575c7765d0349482)

### 01.10

> 今日学习时长

> 5h

> 今日学习任务

> Continuing with yesterday's mission.

> 学习内容小结

> Fixed the logic in the syscall parameter check, updated the logic in mkdir, open, write to create directories properly, and the userprog test points passed except for oom (which is supposed to be caused by files opened by cwd).

> commit log: [01.10](https://github.com/crazyofcode/cs162/commit/592aa7e4e475cc4efd3208a72dd8179b1551705c)

### 01.12

> 今日学习时长

> 4.5h

> 今日学习任务

> 缝缝补补, 跟着测试点的错误信息, 修改实现的问题

> 学习内容小节

> 主要是文件/目录的新建和删除相关操作实现的补充, 比如不能删除 pcb->cwd 的父目录和不能删除 "/" 目录等, 现在关于这两个部分的测试点还有 rm-tree 没有通过

> commit log: [01.12](https://github.com/crazyofcode/cs162/commit/4bde035a38e5dcddd2faed3fc4d6a567af5bc508)

### 01.13

> 今日学习时长

> 6h

> 今日学习任务

> 修复关于文件系统中 dir 相关实现的 bug

> 学习内容小结

> readdir 系统调用的实现错误, pos 指针没有被正确的记录, 修改了在第一个 proj 中对于打开文件的 entry 的定义, 增加了对目录的支持, 相应的系统调用函数如: open 等也作了相应的修改, 修改了 dir lookup 函数的 bug, 修复了 inode 被打开但是没有被正确的关闭的问题，最后是文件扩容的问题(只是实现了部分, 即是说扩容量必须小于 BLOCK_SECTOR_SIZE), 但是 dir-vine 测试点还没有通过。

> commit log: [01.13](https://github.com/crazyofcode/cs162/commit/72421901cba7848d660457f330f7f4c405ee1969)

### 01.14

> 今日学习时长

> 5h

> 今日学习任务

> 完善文件的扩展, 使用 120 个直接索引和 6 个间接索引, 能够支持更大的文件

> 学习内容小结

> 将 pintos 提供的 free-map 的功能函数进行封装，以满足我设计的双重索引的需要，主要修改了释放和分配 sector 块的逻辑，不过由于需要判断是所以直接索引还是简介索引以及间接索引的内容在哪一块磁盘空间导致逻辑变得更为复杂，写得有些乱，然后发现我的持久性测试都没有通过但是我在 shundown 和 idle-thread 里都有 bflush 的使用，还没找到问题

> commit log: [01.14](https://github.com/crazyofcode/cs162/commit/ac3e1f81c82ffa5c5b886b5b2262cc0fd0767d63)

### 01.15

> 今日学习时长

> 2h

> 今日学习任务

> 文件系统的持久化

> 学习内容小结

> 持久化的测试调试不了一点, 只能看到错误信息是 "存在名字为空的文件"，但是看不到其他的信息, 对于它打包的 tar 文件也是很难查看, 呃呃呃放弃了。后面开始看 18447 的 slides 了，cs162 就到这了吧。

### 01.16

> 今日学习时长

> 4h

> 今日学习任务

> out-of-order's lecture, Memory Technology and Organization's slide and P&H 5.1-5.2

> 学习内容小结

> OoO 主要介绍的是指令的调度和寄存器的重命名。第一种方案是每个 unit 会有一个 reservation table 记录使用的数据的来源, 每一个条目有一个别名, 会将这个别名记录到 registers alias table 中作为寄存器的别名并将寄存器的 valid 位置为 0表示这个寄存器的值在后续的 cycle 中由 producer 写入, 所有和这个寄存器有关的 consumer 都会被 stall。在 producer 完成该条指令后会通过总线进行广播，会更新每个 unit 和 registers alias table 中和这个寄存器相关的条目，如果该条目更新后，需要的源数据都准备好后就会有调度器决定是否进入后续的流水线。关于每个 unit 中的数据什么时候 retire，我还不是很清楚。由于通过总线广播生产的数据时会在很多个 table 中复制，为了减少这种消耗，后来简化成了类似指针的结构，分为前端的寄存器和与 arch 状态相关的物理寄存器，前端的寄存器在 renaming 后会有一个 index 指向实际使用的物理寄存器，以这种方式减少数据的复制。对于 commit 的指令不会立刻 retire，而是保存在 rob 中，保证顺序发射，乱许执行，顺序提交，用以实现精确异常。后面还补充了关于内存类似的步骤，不过由于内存的地址空间是非常大的，难以使用 renaming。

<!-- Content_END -->
