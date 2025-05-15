from nonebot import require

require("nonebot_plugin_alconna")
from nonebot_plugin_alconna import Command

matcher = (
    Command("about")
    .alias("关于")
    .action(lambda: "https://github.com/chirabx/chirabot")
    .build()
)
