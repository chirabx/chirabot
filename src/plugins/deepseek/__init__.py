from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="deepseek",
    description="",
    usage="",
    config=Config,
)

from . import deepseek as deepseek
