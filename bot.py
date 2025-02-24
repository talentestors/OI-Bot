import nonebot
# from nonebot.adapters.console import Adapter as ConsoleAdapter # dev
from nonebot.adapters.onebot.v11 import Adapter as OnebotAdapterV11
import nonebot.config  # 避免重复命名

# 初始化 NoneBot
nonebot.init()

# 注册适配器
driver = nonebot.get_driver()
# driver.register_adapter(ConsoleAdapter) # dev
driver.register_adapter(OnebotAdapterV11)

# 加载配置文件
env_config = driver.config
env_run_evironment = str(env_config.environment).strip()

# 在这里加载插件
# dev 环境下
if env_run_evironment == "dev":
    nonebot.load_builtin_plugins("echo")  # 内置插件
    nonebot.load_plugin("nonebot_plugin_docs")  # 离线文档

nonebot.load_plugin("nonebot_plugin_oi_helper")  # oi_helper
nonebot.load_plugin("nonebot_plugin_luoguluck")  # oi_helper
nonebot.load_plugins("oi_bot/plugins")  # 加载插件

if __name__ == "__main__":
    nonebot.run()
