#!/bin/bash
set -e

echo "清理旧目录..."
if [ -d "/root/OI-Bot/" ]; then
    rm -rf /root/OI-Bot/
fi

echo "克隆仓库..."
git clone --depth 1 https://github.com/talentestors/OI-Bot.git /root/OI-Bot
cd /root/OI-Bot

echo "同步依赖并激活虚拟环境..."
uv sync --no-dev
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
else
    echo "虚拟环境未找到，退出"
    exit 1
fi

echo "启动 bot..."
logfile="bot_$(date +%Y-%m-%d).log"
python bot.py 2>&1 | tee "$logfile"
