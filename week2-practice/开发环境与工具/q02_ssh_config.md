# Q7: SSH 配置与端口转发

## 操作记录
- 生成 SSH key（ed25519）
- 在本机安装 openssh-server，模拟远程机器
- 配置 `~/.ssh/config`，设置 Host 别名 `vm`，配置 `LocalForward 9999 localhost:8888`
- `ssh-copy-id vm` 完成公钥认证，验证免密登录成功
- 在 vm 上启动 `python3 -m http.server 8888`，本机 `curl http://localhost:9999` 验证端口转发成功
- 修改 `sshd_config` 尝试禁用密码登录和 root 登录后，sshd 重启后拒绝连接（Connection refused），排查后未能在预期时间内解决，后续可能是 WSL 环境下 sshd 重启机制或 tcp wrapper 相关问题

## 关键知识点
- `LocalForward` 把本地端口的流量通过 SSH 隧道转发到远程机器上的另一个端口，常用于访问远程机器上只监听 localhost 的服务
- 禁用密码登录前必须先确认 key 登录正常，否则可能把自己锁在外面
