# Git实例1+2：clone课程网站，git log / git blame

clone: git clone https://github.com/missing-semester/missing-semester.git

## README.md最后修改人（git log -1 -- README.md）
Author: Anish Athalye <me@anishathalye.com>
Date: Sat Apr 25 11:01:42 2026 -0700
Commit message: Tweak text about license

## _config.yml中collections:那行的commit（git blame + git show）
git blame _config.yml | grep "collections:"
→ a88b4eac (Anish Athalye 2020-01-17 15:26:30 -0500 19) collections:

git show a88b4eac
Author: Anish Athalye <me@anishathalye.com>
Date: Fri Jan 17 15:26:30 2020 -0500
Commit message: Redo lectures as a collection
（这次改动把各年份讲义从普通目录改造成Jekyll collection结构）
