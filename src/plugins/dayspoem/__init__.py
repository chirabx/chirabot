from nonebot_plugin_alconna import Alconna, CommandMeta, on_alconna
from nonebot.adapters.onebot.v11 import Message,Event
from nonebot.internal.adapter.bot import Bot
from nonebot import require,get_bot
require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
from .dayspoem import get_brief, get_poem
# 定义简报命令
brief_command = Alconna(
    "简报",
    meta=CommandMeta(
        description="这是一个获取每日简报的插件\n输入简报/今日简报获取内容"
    ),
)

# 定义诗词命令
poem_command = Alconna(
    "诗词",
    meta=CommandMeta(
        description="根据时间、地点、天气、事件智能推荐今日诗词"
    ),
)

# 注册简报命令处理器
brief_matcher = on_alconna(brief_command, aliases={"今日简报"})
@brief_matcher.handle()
async def handle_brief():
    result = await get_brief()
    await brief_matcher.finish(result or "获取简报失败，请稍后再试！")

# 注册诗词命令处理器
poem_matcher = on_alconna(poem_command, aliases={"今日诗词", "诗"})
@poem_matcher.handle()
async def handle_poem():
    result = await get_poem()
    await poem_matcher.finish(result or "获取诗词失败，请稍后再试！")

from nonebot import get_driver
target_group_id = get_driver().config.target_group_id


# 定时任务：每天早上8点推送简报
@scheduler.scheduled_job("cron", hour=8, minute=0, id="daily_brief_push")
async def daily_brief_push():
    bot: Bot = get_bot()  # 获取当前 Bot 实例
    result = await get_brief()
    if result:
        for group_id in target_group_id:
            await bot.send_group_msg(group_id=group_id, message=result)
            await bot.send_group_msg(group_id=group_id, message="今日简报已送达")