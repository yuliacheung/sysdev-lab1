#!/bin/bash

# 检查参数个数
if [ $# -ne 1 ]; then
    echo "Usage: $0 <csv-file>" >&2
    exit 1
fi

csv_file="$1"

# 检查文件是否存在
if [ ! -f "$csv_file" ]; then
    echo "Error: File '$csv_file' not found" >&2
    exit 1
fi

# 统计 HTTP 5xx 最多的前 2 个 path
echo "Top 2 paths with 5xx errors:"
awk -F, 'NR>1 && $4 >= 500 && $4 < 600 {print $3}' "$csv_file" \
    | sort \
    | uniq -c \
    | sort -k1,1nr -k2,2 \
    | head -n 2 \
    | awk '{print $2 " " $1}'

# 计算平均 latency_ms
awk -F, 'NR>1 {sum += $5; count++} END {printf "Average latency: %.2f\n", sum/count}' "$csv_file"
