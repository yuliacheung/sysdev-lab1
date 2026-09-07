# Q6: Dotfiles

## 操作记录
- 创建 `dotfiles/` 目录，纳入本 repo 的版本控制
- 把 `~/.bashrc` 迁移为 `dotfiles/bashrc` 管理，自定义了 PS1（用户名+主机名绿色，路径蓝色）
- 用 `ln -s` 把 `~/.bashrc` 软链接到 `dotfiles/bashrc`，实现"改 dotfiles 里的文件、实际配置同步生效"
- 写了 `install.sh`，用软链接的方式一键安装配置，方便在新机器上快速部署

## 关键知识点
- 软链接（`ln -s`）让 dotfiles 仓库和实际生效的配置文件保持同步，不用每次手动复制
- 安装脚本应该用 `ln -sf` 而不是 `cp`，这样修改 dotfiles 仓库里的文件会立刻反映到实际配置
