# Bark-Telegram-Notifier

Bark-Telegram-Notifier 是一个使用 Python 编写的 Telegram 机器人，利用 BARK 服务发送通知。该机器人允许白名单用户通过 Telegram 命令发送通知。

## 特性

- 使用 BARK 通过 Telegram 命令将通知发送到您的设备。
- 白名单系统，将通知发送权限限制为特定用户。
- 检索用户和群组 ID 以进行管理。

## 设置

1. 克隆存储库：

```
git clone https://github.com/your_username/Bark-Telegram-Notifier.git
```

2. 安装依赖项：

```
pip install -r requirements.txt
```

3. 获取您的 Telegram 机器人令牌和 BARK 通知 ID。
4. 在脚本中用实际值替换占位符 (`TOKEN`, `ADMIN_ID`, `BARK_BASE_URL`)。
5. 运行脚本：

```
python notifier.py
```

## 用法

- 发送 `/start` 命令以启动机器人并接收欢迎消息。
- 使用 `/notify` 或 `/notifylite` 命令发送通知。
- 使用 `/white` 命令将用户或群组添加到白名单。
- 使用 `/getid` 命令检索用户或群组的 ID。

## 命令

- `/start`: 启动机器人并接收欢迎消息。
- `/notifylite [message]`: 使用 BARK 发送通知，不带自定义声音。
- `/notify [message]`: 使用 BARK 发送通知，带有打字机声音。
- `/white [user_or_group_id]`: 将用户或群组 ID 添加到白名单。
- `/getid`: 检索用户或群组的 ID。

## 贡献

欢迎贡献！如果您发现任何问题或有改进建议，请随时提交问题或创建拉取请求。
