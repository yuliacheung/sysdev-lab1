# p09-make-clean

Makefile 的 clean 目标与 .PHONY。

## 运行

    make
    ls
    make clean
    ls

## 说明

- all 依赖 out.txt
- out.txt 由 in.txt 生成
- clean 删除生成物 out.txt
- .PHONY 声明 all 和 clean 不是文件名
