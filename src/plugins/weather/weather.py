from nonebot import on_command
from nonebot.rule import to_me  #响应@的规则
from nonebot.adapters import Message  
# 可以直接使用nonebot.params模块定义的参数类型来声明依赖 
from nonebot.params import CommandArg


weather = on_command("谁是shit", rule=to_me(), aliases={"who is shit", "who's shit"}, priority=10, block=True)

@weather.handle()
async def handle_function(args: Message = CommandArg()):
    # 提取参数纯文本作为地名，并判断是否有效
    if loaction := args.extract_plain_text():
        await weather.finish(f"{loaction}是构思😜")
    # await weather.send("名字是...")
    else:
        await weather.finish("请输入人名")