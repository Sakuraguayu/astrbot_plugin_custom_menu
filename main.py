from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.api.message_components import *

import os
import random


@register(
    "astrbot_plugin_custom_menu",
    "Futureppo",
    "自定义图片菜单，直接发送图片而不是合并转发",
    "1.0.0"
)
class custommenu(Star):

    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command(
        "菜单",
        alias=["帮助", "功能", "你怎么用"]
    )
    async def custommenu(self, event: AstrMessageEvent):

        # 插件目录
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # menu 文件夹
        menu_dir = os.path.join(base_dir, "menu")

        # 自动创建目录
        if not os.path.exists(menu_dir):
            try:
                os.makedirs(menu_dir, exist_ok=True)
                logger.info(f"已自动创建 menu 文件夹: {menu_dir}")
            except Exception as e:
                logger.error(f"创建 menu 文件夹失败: {e}")
                yield event.plain_result("创建menu文件夹失败")
                return

        # 支持的图片格式
        image_extensions = [
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".bmp",
            ".webp"
        ]

        # 获取所有图片
        image_paths = [
            os.path.join(menu_dir, f)
            for f in os.listdir(menu_dir)
            if os.path.isfile(os.path.join(menu_dir, f))
            and os.path.splitext(f)[1].lower() in image_extensions
        ]

        # 没有图片
        if not image_paths:
            logger.warning(f"menu 文件夹中没有图片: {menu_dir}")
            yield event.plain_result(
                "menu文件夹里没有图片，请先放入菜单图片。"
            )
            return

        try:
            # 随机选择一张图片
            selected_image = random.choice(image_paths)

            logger.info(f"发送菜单图片: {selected_image}")

            # 加载图片
            image = Image.fromFileSystem(selected_image)

            # 直接发送图片
            yield event.chain_result([
                image
            ])

        except Exception as e:
            logger.error(f"发送菜单图片失败: {e}")

            yield event.plain_result(
                "菜单发送失败，请查看控制台日志。"
            )
