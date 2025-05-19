from nonebot_plugin_alconna import (
    Command, 
    CommandResult, 
    UniMessage,
    Alconna,
    Args,
    Subcommand,
    on_alconna,
    CommandMeta
)

alc = Alconna(
    "ciallo",   
    meta=CommandMeta(
        description="柚子厨鉴定器！发送 ciallo，看看你是不是隐藏的柚子厨喵～"
    ),
)
# 注册命令处理器
matcher = on_alconna(alc, aliases={"柚子厨","柚子","Ciallo～(∠・ω< )⌒☆"})

# 定义命令的处理逻辑
@matcher.handle()
async def handle_command(result):
    await matcher.finish("Ciallo～(∠・ω< )⌒☆ 你果然是个柚子厨喵！")