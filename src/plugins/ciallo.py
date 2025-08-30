# ciallo.py
import random, re
from nonebot.plugin import on_regex  
from nonebot.adapters.onebot.v11 import MessageEvent

ciallo_lines = [
    "我欲乘风归去，又恐 Ciallo～(∠・ω< )⌒☆ 玉宇",
    "一点寒芒先到，随后 Cia 出如 llo～(∠・ω< )⌒☆",
    "欲穷千里目，更上一 Ciallo～(∠・ω< )⌒☆",
    "问君能有几多愁，Cia 似一江春水向东 llo～(∠・ω< )⌒☆",
    "昔人已 Cia 黄鹤去，此地空余黄鹤 llo～(∠・ω< )⌒☆",
    "小 cia llo～(∠・ω< )⌒☆ 水人家",
    "青青子衿，悠悠我心，但为君故，Cia llo～(∠・ω< )⌒☆ 至今",
    "黄沙百战 Cia 金甲，不破 llo～(∠・ω< )⌒☆ 兰终不还",
    "一身转战三 Cia llo～(∠・ω< )⌒☆，一剑曾当百万师",
    "杨柳 Cia Cia 江水平，问 llo～(∠・ω< )⌒☆ 江上歌唱声",
    "老骥思 Ciallo～(∠・ω< )⌒☆，飞鸿阅九洲。",
    "朝 cia 白帝 Cia 云间，千里江 llo～(∠・ω< )⌒☆ 一日还",
    "桃花潭水深 Cia 尺，不及汪 llo～(∠・ω< )⌒☆ 送我情",
    "Ciallo～(∠・ω< )⌒☆ 稻花应秀色，五更桐叶最佳音",
    "Ciallo～(∠・ω< )⌒☆",
    "𝑪𝒊𝒂𝒍𝒍𝒐～(∠・ω< )⌒☆",
    "𝓒𝓲𝓪𝓵𝓵𝓸～(∠・ω< )⌒☆",
    "𝐂𝐢𝐚𝐥𝐥𝐨～(∠・ω< )⌒☆",
    "ℂ𝕚𝕒𝕝𝕝𝕠～(∠・ω< )⌒☆",
    "𝘊𝘪𝘢𝘭𝘭𝘰～(∠・ω< )⌒☆",
    "𝗖𝗶𝗮𝗹𝗹𝗼～(∠・ω< )⌒☆",
    "𝙲𝚒𝚊𝚕𝚕𝚘～(∠・ω< )⌒☆",
    "ᴄɪᴀʟʟᴏ～(∠・ω< )⌒☆",
    "𝕮𝖎𝖆𝖑𝖑𝖔～(∠・ω< )⌒☆",
    "ℭ𝔦𝔞𝔩𝔩𝔬～(∠・ω< )⌒☆",
    "ᶜⁱᵃˡˡᵒ～(∠・ω< )⌒☆",
    "ᑕ⫯Ꭿ𝘭𝘭𝖮～(∠・ω< )⌒☆",
    "☆⌒( >ω・∠)～ollɐıɔ"
    ] 

matcher = on_regex(r"(柚子|ciallo)", flags=re.I)    # re.I 表示忽略大小写

@matcher.handle()
async def _(event: MessageEvent):
    msg = random.choice(ciallo_lines)
    await matcher.finish(msg)
