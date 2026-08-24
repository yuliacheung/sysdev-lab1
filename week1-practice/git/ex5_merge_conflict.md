# Git实例5：模拟merge conflict

在recipe-conflict-demo/仓库中：
1. 初始commit：recipe.txt内容 "1 cup sugar"
2. 分出salty、sweet两个分支
3. salty分支改成 "1 cup salt" 并commit
4. sweet分支改成 "2 cups sugar" 并commit
5. 回main，先merge salty（fast-forward成功），再merge sweet（冲突）

冲突时recipe.txt内容：
<<<<<<< HEAD
1 cup salt
=======
2 cups sugar
>>>>>>> sweet

含义：
- <<<<<<< HEAD 到 =======：当前分支(main，已含salty改动)的版本
- ======= 到 >>>>>>> sweet：正在合并进来的sweet分支版本

解决方式：保留salty的盐，手动改成"1 cup salt"，去掉冲突标记，
git add + git commit完成合并。

最终历史（git log --all --graph --oneline，见同目录conflict-log.txt）：
*   4ce6513 resolve conflict: keep salt
|\
| * 6d4ee51 sweet: more sugar
* | 5c4992a salty: change to salt
|/
* f2ebb29 initial recipe
