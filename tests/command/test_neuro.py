import pytest
from pathlib import Path
from nonebug import App


@pytest.mark.asyncio
async def test_neuro_draw(app: App):
    from oi_bot.plugins.neuro_draw import draw_handler, draw_luck

    async with app.test_matcher(draw_luck):
        message, image_path = await draw_handler.handle_luck_draw("test_user")

        # 验证返回的消息
        assert isinstance(message, str), "返回的消息必须是字符串类型"
        assert len(message) > 0, "返回的消息不能为空"
        assert "今天" in message, f"消息内容应该包含抽卡相关信息，当前消息: {message}"

        # 验证返回的图片路径
        assert isinstance(image_path, Path), "返回的图片路径必须是 Path 对象"
        assert str(image_path).endswith(".png"), (
            f"图片路径应该以.png结尾，当前路径: {image_path}"
        )

        # 验证文件是否存在
        assert image_path.exists(), f"图片文件不存在: {image_path}"
        assert image_path.is_file(), f"路径不是文件: {image_path}"

        # 验证文件大小（确保不是空文件）
        file_size = image_path.stat().st_size
        assert file_size > 0, f"图片文件大小为0: {image_path}"
        assert file_size < 10 * 1024 * 1024, (
            f"图片文件过大（超过10MB）: {image_path}, 大小: {file_size} bytes"
        )

        try:
            if image_path.exists():
                image_path.unlink()
        except Exception as e:
            print(f"清理文件时出错: {e}")
