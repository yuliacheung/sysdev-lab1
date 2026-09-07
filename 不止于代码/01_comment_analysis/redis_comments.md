# Redis源码注释分析

## TODO注释
```c
/* TODO: implement better eviction algorithm */
```

## 外部文档引用
```c
/* 参考: https://redis.io/topics/lru-cache */
```

## "why not"注释
```c
/* 避免使用随机抽样，因为会影响性能 */
```

## 血泪教训
```c
/* FIXME: 在高并发下可能出现的竞态条件 */
```

## 如果没有这些注释
- 开发者会重复遇到同样的问题
- 难以理解设计决策
- 维护成本大幅增加
