import nonebot
from nonebot.log import logger

# 初始化 NoneBot
nonebot.init()

driver = nonebot.get_driver()

# 加载配置文件
env_config = driver.config
env_run_evironment = str(env_config.environment).strip()

# 注册适配器
# ONEBOT 11 协议适配器
logger.debug(f"ONEBOT 11 协议适配器: '{env_config.onebot_access_token.strip()}'")
if env_config.onebot_access_token.strip() != "":
    from nonebot.adapters.onebot.v11 import Adapter as OnebotAdapterV11

    driver.register_adapter(OnebotAdapterV11)
    logger.info("已注册 Onebot 11 协议适配器")

# 在这里加载插件
# dev 环境下
if env_run_evironment == "dev":
    from nonebot.adapters.console import Adapter as ConsoleAdapter

    bot_enable_console = env_config.bot_enable_console
    logger.debug(f"bot_enable_console={bot_enable_console}")
    if bot_enable_console is True:
        driver.register_adapter(ConsoleAdapter)
        logger.info("已注册 Console 适配器")
        nonebot.load_builtin_plugin("echo")  # 内置插件
        logger.info("已加载 echo 插件")

# if env_run_evironment == "dev":
# nonebot.load_plugin("nonebot_plugin_docs")  # 离线文档

# 默认环境下
nonebot.load_plugin("nonebot_plugin_oi_helper")  # oi_helper
nonebot.load_plugin("nonebot_plugin_luoguluck")  # luoguluck
nonebot.load_plugins("oi_bot/plugins")  # 加载插件

if __name__ == "__main__":
    nonebot.run()
