import pytest
import nonebot
from pytest_asyncio import is_async_test
from nonebot.log import logger
import sys
from pathlib import Path

# 将项目根目录加入到 sys.path 中
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# 导入适配器
from nonebot.adapters.console import Adapter as ConsoleAdapter


def pytest_collection_modifyitems(items: list[pytest.Item]):
    pytest_asyncio_tests = (item for item in items if is_async_test(item))
    session_scope_marker = pytest.mark.asyncio(loop_scope="session")
    for async_test in pytest_asyncio_tests:
        async_test.add_marker(session_scope_marker, append=False)


@pytest.fixture(scope="session", autouse=True)
async def after_nonebot_init(after_nonebot_init: None):
    # 加载适配器
    driver = nonebot.get_driver()
    driver.register_adapter(ConsoleAdapter)
    nonebot.load_plugin("nonebot_plugin_oi_helper")  # oi_helper
    nonebot.load_plugin("nonebot_plugin_luoguluck")  # luoguluck
    nonebot.load_plugins("oi_bot/plugins")  # 加载插件
    logger.info("Plugin loaded")
