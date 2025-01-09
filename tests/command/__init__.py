from nonebot.log import logger
import nonebot

# 导入适配器

nonebot.init()

# 加载插件
nonebot.load_plugin("nonebot_plugin_oi_helper")  # oi_helper
logger.info("Plugin loaded")
