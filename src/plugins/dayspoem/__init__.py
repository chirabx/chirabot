from nonebot import  on_command
from nonebot.typing import T_Handler 
from .data_source import Source, sources
from nonebot.matcher import Matcher
from nonebot.plugin import PluginMetadata
 
 
__plugin_meta__ = PluginMetadata(
    name="今日诗词",
    description="这个插件会根据时间、地点、天气、事件智能推荐诗词！",
    usage="/今日诗词",
)
def create_matchers():
    def create_handler(source: Source) -> T_Handler:
        async def handler(matcher: Matcher):
            res = None
            try:
                res = await source.func()
                if not res:
                    res = "获取数据失败"
            except Exception as e:
                print(e)
                res = "出错了，请稍后再试"
            await matcher.finish(res)
 
        return handler
 
    for source in sources:
        on_command(
            source.keywords[0], aliases=set(source.keywords), block=True, priority=12
        ).append_handler(create_handler(source))
 
 
create_matchers()