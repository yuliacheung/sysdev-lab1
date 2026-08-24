# Git实例3：git stash

在missing-semester仓库，修改README.md（未commit）：

git status → 显示 modified: README.md（未暂存）

git stash → Saved working directory and index state WIP on master: ...
git status → nothing to commit, working tree clean（改动被存起来，工作区变干净）

git log --all --oneline | head -5 →
f3080d3 WIP on master: fea9192 ...
8bfcedb index on master: fea9192 ...
fea9192 Merge branch ...
（发现：--all 会看到stash产生的commit对象，因为stash本质上也是存成commit、
挂在refs/stash下，只是普通git log不加--all时不会显示）

git stash pop → Dropped refs/stash@{0}: ...
git status → 又变回 modified: README.md（改动恢复了）

应用场景：正在改代码到一半，需要紧急切分支处理别的任务，又不想为半成品专门commit，
用stash先存起来，处理完再pop回来继续。
