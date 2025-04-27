# oi-bot-1panel

在 1Panel 面板运行 OI-Bot

---

## 使用方式

_注意:_ 请自行寻找代理

如果无法拉取镜像请修改 docker-compose 中的 ghcr.io/talentestors/oi-bot:latest

添加你的代理

### 1 使用 git 命令获取应用

`1Panel`计划任务类型`Shell 脚本`的计划任务框里，添加并执行以下命令，或者保存为 sh 然后在终端运行。

```bash
#!/bin/sh

install_dir=$(which 1pctl | xargs grep '^BASE_DIR=' | cut -d'=' -f2)

rm -rf $install_dir/1panel/resource/apps/local/oi-bot-1panel

git clone -b 1panel https://github.com/talentestors/OI-Bot.git "$install_dir/1panel/resource/apps/local/oi-bot-1panel"

if [ $? -eq 0 ]; then
    rm -rf $install_dir/1panel/resource/apps/local/oi-bot
    mv $install_dir/1panel/resource/apps/local/oi-bot-1panel $install_dir/1panel/resource/apps/local/oi-bot
    echo "success"
else
    echo "error"
    exit 1
fi
```

然后应用商店刷新本地应用即可。

### 2 使用压缩包方式获取应用

`1Panel`计划任务类型`Shell 脚本`的计划任务框里，添加并执行以下命令，或者保存为 sh 然后在终端运行。

```bash
#!/bin/sh

install_dir=$(which 1pctl | xargs grep '^BASE_DIR=' | cut -d'=' -f2)

rm -rf $install_dir/1panel/resource/apps/local/OI-Bot-1panel

if command -v wget > /dev/null; then
    wget -O $install_dir/1panel/resource/apps/local/oi-bot-1panel.zip https://github.com/talentestors/OI-Bot/archive/refs/heads/1panel.zip
elif command -v curl > /dev/null; then
    curl -o $install_dir/1panel/resource/apps/local/oi-bot-1panel.zip https://github.com/talentestors/OI-Bot/archive/refs/heads/1panel.zip
else
    echo "请先安装wget或curl"
    exit 1
fi

unzip "$install_dir/1panel/resource/apps/local/oi-bot-1panel.zip" -d "$install_dir/1panel/resource/apps/local/"
if [ $? -ne 0 ]; then
    echo "解压失败，请检查压缩包或安装unzip工具"
    exit 1
fi
rm -rf $install_dir/1panel/resource/apps/local/oi-bot-1panel.zip
rm -rf $install_dir/1panel/resource/apps/local/oi-bot
mv $install_dir/1panel/resource/apps/local/OI-Bot-1panel $install_dir/1panel/resource/apps/local/oi-bot
echo "success"
```

然后应用商店刷新本地应用即可。
