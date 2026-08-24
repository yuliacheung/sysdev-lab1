# Git实例4：~/.gitconfig 别名

命令：
git config --global alias.graph "log --all --graph --decorate --oneline"

效果：以后在任意仓库执行 git graph，等同于执行完整的
git log --all --graph --decorate --oneline

验证 ~/.gitconfig 内容：
[user]
        name = yuliacheung
        email = yuliacheung@stu.ouc.edu.cn
[alias]
        graph = log --all --graph --decorate --oneline

git graph 实际输出（片段）：
*   fea9192 (HEAD -> master, origin/master, origin/HEAD) Merge branch 'oiahoon/docs/fix-uv-lock-example'
|\
| * 7343431 docs: fix uv lockfile Docker example
|/
*   853e0ea Merge branch
 'tufailrizvi-debug/fixing_typo'
