<div align="center">

![logo](./docs/images/atri-256x256.png)

# ✨ OI-Bot | 高性能ですから！✨

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![license](https://img.shields.io/github/license/talentestors/OI-Bot.svg)](https://www.gnu.org/licenses/agpl-3.0.html)
![python](https://img.shields.io/badge/python-3.12+-blue.svg)
[![nonebot](https://img.shields.io/badge/nonebot-v2.4.1-EA5252.svg)](https://nonebot.dev/)
[![onebot11](https://img.shields.io/badge/OneBot-v11-black?style=social&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABABAMAAABYR2ztAAAAIVBMVEUAAAAAAAADAwMHBwceHh4UFBQNDQ0ZGRkoKCgvLy8iIiLWSdWYAAAAAXRSTlMAQObYZgAAAQVJREFUSMftlM0RgjAQhV+0ATYK6i1Xb+iMd0qgBEqgBEuwBOxU2QDKsjvojQPvkJ/ZL5sXkgWrFirK4MibYUdE3OR2nEpuKz1/q8CdNxNQgthZCXYVLjyoDQftaKuniHHWRnPh2GCUetR2/9HsMAXyUT4/3UHwtQT2AggSCGKeSAsFnxBIOuAggdh3AKTL7pDuCyABcMb0aQP7aM4AnAbc/wHwA5D2wDHTTe56gIIOUA/4YYV2e1sg713PXdZJAuncdZMAGkAukU9OAn40O849+0ornPwT93rphWF0mgAbauUrEOthlX8Zu7P5A6kZyKCJy75hhw1Mgr9RAUvX7A3csGqZegEdniCx30c3agAAAABJRU5ErkJggg==)](https://onebot.dev/)

[![Docker Image](https://github.com/talentestors/OI-Bot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/talentestors/OI-Bot/actions/workflows/docker-image.yml)

</div>

This chatbot provides match information for OIer and ACMer, based on the Nonebot2 framework.

## Usage

### Install

```bash
git clone --depth=1 https://github.com/talentestors/OI-Bot.git
cd OI-Bot
```

pip install

```bash
pip install -r requirements.txt
```

Usage of UV

```bash
uv sync --no-dev
```

### Docker

Pull and run the docker image directly:

```bash
docker pull ghcr.io/talentestors/oi-bot:latest
```

#### Use 1panel appstore deployment

[See docs](./docs/1panel-appstore.md)

### Run

```bash
python bot.py
```

### Config

```bash
cp .env.example .env
```

Edit `.env` file

Configurations:

- `OneBot`:
  - `ONEBOT_ACCESS_TOKEN`: OneBot 11 access token
  - url: `ws://ip:port/onebot/v11/ws`
- `nonebot-plugin-oi-helper`:
  - see [nonebot-plugin-oi-helper](https://github.com/talentestors/nonebot-plugin-oi-helper)

---

This project includes software from the following sources:

1. [nonebot2](https://nonebot.dev/)
   - Licensed under the MIT License
2. [nonebot-adapter-onebot](https://onebot.adapters.nonebot.dev/)
   - Licensed under the MIT License
3. [nonebot-plugin-oi-helper](https://github.com/talentestors/nonebot-plugin-oi-helper)
   - Copyright (C) 2024 talentestors
   - Licensed under the GNU Affero General Public License, Version 3
   - <https://www.gnu.org/licenses/agpl-3.0.html>
