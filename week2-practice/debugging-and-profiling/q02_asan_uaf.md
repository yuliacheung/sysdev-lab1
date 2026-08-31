# Q9: AddressSanitizer 检测 use-after-free

## 现象
不加 sanitizer 编译运行时程序没有崩溃，但第二次 print 输出的是乱码（`J` 后面跟垃圾字符），说明写入了已经不属于自己的内存，但没有立刻报错——这类 bug 很难靠肉眼或普通运行发现。

## ASan 报告解读
用 `gcc -fsanitize=address -g uaf.c -o uaf` 编译后，ASan 直接定位：
- WRITE of size 1 at uaf.c:12 → `greeting[0] = 'J';`（非法写入）
- freed by ... uaf.c:10 → `free(greeting);`（释放位置）
- previously allocated by ... uaf.c:6 → `malloc(32);`（分配位置）

Shadow bytes 中的 `fd` 标记代表"Freed heap region"，是 ASan 判断这块内存已被释放的依据。

## 修复
`free()` 之后立刻把指针置为 `NULL`，并删除后续对该指针的读写。修复后重新用 ASan 编译运行，无任何报错。

## 关键知识点
- Use-after-free 不一定崩溃，可能只是悄悄读写脏数据，比直接崩溃更危险
- ASan 通过给每块堆内存维护"shadow memory"标记状态（可用/已释放/redzone），实现对非法访问的精确检测
- `free()` 后置 `NULL` 是防御性编程的常见做法，能把潜在的 use-after-free 提前转化成明显的 NULL 解引用崩溃
