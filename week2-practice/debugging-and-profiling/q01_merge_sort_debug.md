# Q8: 归并排序调试

## Bug 描述
`merge` 函数的 else 分支里，`result.append(right[i])` 用错了索引变量——`i` 是 `left` 数组的索引，取 `right` 数组的值应该用 `j`。

## 调试过程（使用 pdb）
- 在 else 分支加 `pdb.set_trace()` 断点
- 前几次 `i == j`（都是 0），看不出问题
- 继续 `c` 几轮后，数组变长为 `left=[1,3]`, `right=[1,4]`，此时 `i=1, j=0`
- `p right[i]` → 4，`p right[j]` → 1：两者不同，暴露出原代码取错了变量
- 此时 `left[i]=3 > right[j]=1`，本该把 `right[j]=1` 放进结果，但代码错误地放入了 `right[i]=4`

## 修复
```python
else:
    result.append(right[j])  # 原来是 right[i]
    j += 1
```
修复后 `merge_sort([3, 1, 4, 1, 5, 9, 2, 6])` 正确输出 `[1, 1, 2, 3, 4, 5, 6, 9]`

## 关键知识点
- pdb 常用命令：`p 变量名` 查看值，`c` 继续执行到下一个断点，`q` 退出调试器
- 类似"复制粘贴打错索引变量"的 bug，光看代码容易忽略，需要构造能让 `i != j` 的输入才能在调试器里暴露出来
