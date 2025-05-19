from httpx import AsyncClient
from nonebot.adapters.onebot.v11 import Message
import re
from typing import Optional

# 每日简报
async def get_brief() -> Optional[Message]:
    """每日简报的获取"""
    async with AsyncClient() as client:
        try:
            resp = await client.get("https://api.2xb.cn/zaob?format=json")
            resp = resp.json()
            url = resp['imageUrl']
        except:
            resp = await client.get("http://bjb.yunwj.top/php/tp/lj.php")
            url = re.findall('"tp":"(?P<url>.*?)"', resp.text)[0]

        pic_ti = f"[CQ:image,file={url}]"
    return Message(pic_ti)

# 诗词
async def get_poem() -> Optional[Message]:
    """获取随机诗词"""
    async with AsyncClient() as client:
        ret = await client.get("https://v2.jinrishici.com/token")
        data = ret.json()
        if data.get("status") == "success":
            token = data["data"]
        else:
            return Message("获取失败，请重新尝试！")
        headers = {
            "X-User-Token": token
        }
        ret = await client.get("https://v2.jinrishici.com/sentence", headers=headers)
        data = ret.json()
        if data.get("status") == "success":
            # 格式化诗句和原文，遇到，。！？就换行
            def format_text(text):
                return re.sub(r'([，。！？])', r'\1\n', text)
            poem = format_text(data['data']['content'])
            origin = "\n".join([format_text(line) for line in data['data']['origin']['content']])
            tags = "、".join(data['data']['matchTags'])
            content = (
                "【今日诗词推荐】\n"
                f"{poem}\n"
                f"——《{data['data']['origin']['title']}》{data['data']['origin']['dynasty']}·{data['data']['origin']['author']}\n\n"
                f"原文：\n{origin}\n"
                f"标签：{tags}"
            )
            return Message(content)
        else:
            return Message("获取失败，请重新尝试！")