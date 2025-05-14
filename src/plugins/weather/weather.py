from nonebot import on_command
from nonebot.rule import to_me  #响应@的规则
from nonebot.adapters import Message,Event
# 可以直接使用nonebot.params模块定义的参数类型来声明依赖 
from nonebot.params import CommandArg


weather = on_command("天气", rule=to_me(), aliases={"weather", "今日天气"}, priority=5, block=True)

@weather.handle()
async def handle_function(args: Message = CommandArg()):
    # 提取参数纯文本作为地名，并判断是否有效
    if loaction := args.extract_plain_text():
        await weather.finish(f"{loaction}的天气是...")
    # await weather.send("天气是...")
    else:
        await weather.finish("请输入地名")
        try:
            event:Event = await weather.receive(timeout=30)
            loaction = event.get_plaintext()
            if loaction:
                await weather.finish(f"{loaction}的天气是...")
            else:
                await weather.finish("未检测到地名，已取消操作。")
        except TimeoutError:
            await weather.finish("等待超时，已取消查询。")        