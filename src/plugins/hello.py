# # plugins/hello.py
# from nonebot.rule import to_me
# from nonebot.adapters import Event
# from nonebot.adapters.onebot.v11 import MessageSegment
# from nonebot import on_command #用于监听特定的 命令，并在命令触发时执行对应的逻辑
# from nonebot import on_message #用于监听所有的消息事件（如私聊消息、群聊消息等）

# hello_setu = on_message(rule=to_me(), block=False, priority=100)
# matcher = on_command("来张涩图",rule=to_me(),aliases={"来张色图","来张图片","我要涩涩"})

# @hello_setu.handle()
# async def hello_handle(event: Event):
#     message = str(event.get_message()).strip()
#     if message in  {"来张涩图", "来张色图", "来张图片", "我要涩涩"} :
#         return
#     # await hello_setu.send(f"不要说{message}，说来张涩图")  # 普通发送，完成后继续后续流程
#     await hello_setu.finish(f"不要说{message}，说来张涩图")  # 最终发送，完成后停止整个流程


# @matcher.handle()
# async def _(event: Event):
#     user_id = event.get_user_id()
#     print(user_id)
#     if user_id == "1819496201":
#         await matcher.send("你太坏了，不给你看")
#     await matcher.send(MessageSegment.image("https://www.chirabx.xyz/images/background/0.png"))


# # from nonebot.internal.adapter import Event
# # from nonebot.adapters.onebot.v11 import MessageSegment

# # matcher = on_command("来张涩图")

# # @matcher.handle()
# # async def _(event: Event):
# #     user_id = event.get_user_id()
# #     if user_id == "1819496201":
# #         await matcher.finish("你太坏了，不给你看")
# #     await matcher.finish(MessageSegment.image("xxx.jpg"))


# # from nonebot import on_command
# # from nonebot.adapters.onebot.v11 import Event, MessageSegment

# # matcher = on_command("来张涩图")

# # @matcher.handle()
# # async def _(event: Event):
# #     user_id = event.get_user_id()
# #     if user_id == "1819496201":
# #         await matcher.finish("你太坏了，不给你看")
# #     # 使用实际有效的图片URL或base64数据
# #     await matcher.finish(MessageSegment.image("https://www.chirabx.xyz/images/background/0.png"))
