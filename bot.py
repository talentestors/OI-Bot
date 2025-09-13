import nonebot
from nonebot.log import logger, default_format

# 定义版本信息
__version__ = "2.5.1"
VERSION_INFO = f"OI-Bot v{__version__}"

# 初始化 NoneBot
nonebot.init()

# 打印版本信息
logger.info(f"正在启动 {VERSION_INFO}")

driver = nonebot.get_driver()

# 加载配置文件
env_config = driver.config
driver.config.nickname.add("アトリ")
env_run_evironment = str(env_config.environment).strip()

# 日志处理
logger.add("log/error.log", level="ERROR", format=default_format, rotation="1 week")
logger.add("log/oi-bot.log", level="INFO", format=default_format, rotation="1 week")
# dev 环境下
if env_run_evironment == "dev":
    logger.add("log/debug.log", level="DEBUG", format=default_format, rotation="1 week")

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

if env_run_evironment == "dev":
    nonebot.load_plugin("nonebot_plugin_docs")  # 离线文档

# 默认环境下
nonebot.load_plugin("nonebot_plugin_oi_helper")  # oi-helper
nonebot.load_plugin("nonebot_plugin_neuro_draw")  # neuro-draw
nonebot.load_plugin("nonebot_plugin_whateat_pic")  # whateat-pic
nonebot.load_plugins("oi_bot/plugins")  # 加载插件

if __name__ == "__main__":
    nonebot.run()
