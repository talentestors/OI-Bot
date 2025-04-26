#!/usr/bin/env bash
set -e

echo "进入目录..."
cd /root/OI-Bot

echo "拉取最新代码..."
git pull --depth 1

echo "清理 Git 仓库..."
git gc --prune=now --aggressive

echo "同步依赖并激活虚拟环境..."
/usr/bin/env uv sync --no-dev
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
else
    echo "虚拟环境未找到，退出"
    exit 1
fi

echo "启动 bot..."
logfile="bot_$(date +%Y-%m-%d).log"
python bot.py 2>&1 | tee "$logfile"
