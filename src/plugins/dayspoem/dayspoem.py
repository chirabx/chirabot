import asyncio
from httpx import AsyncClient
from nonebot.adapters.onebot.v11 import Message
import re
from dataclasses import dataclass
from typing import Tuple, Optional, Protocol

# 文学类的接口

# 历史上的今天:
async def _history():
    """历史的今天的数据获取"""
    async with AsyncClient() as session:
        resp = await session.get("https://yuanxiapi.cn/api/history/?format=json")
        r = resp.json()
    if r.get("code", '300') == '200':
        day = r["day"]
        content = "\n".join([f"{i + 1}. " + k for i, k in enumerate(r["content"])])
        ret = f"{day}\n\n{content}"
    else:
        ret = "数据获取失败！"
    return Message(ret)

# 每日简报
async def _brief():
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

# 鸡汤
async def _soup1():
    """获取随机语录"""
    async with AsyncClient() as client:
        try:
            resp = await client.get("http://api.zhaoge.fun/api/rshy.php")
            sten = resp.text.split()[2]
            return Message(sten)
        except Exception as e:
            print(e)
            return Message("获取失败，请重新尝试")

# 毒鸡汤
async def _soup2():
    """获取毒鸡汤"""
    async with AsyncClient(follow_redirects=True) as client:
        resp = await client.get("https://api.sunweihu.com/api/yan/api.php?charset=utf-8&encode=json")
        if resp.is_success:
            ret = resp.json()["text"]
        else:
            ret = "获取失败！接口出现问题！"
        return Message(ret)

# 诗词
async def _poem():
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

# 段子
async def _paragraph():
    """获取段子"""
    async with AsyncClient(follow_redirects=True) as client:
        resp = await client.get("https://yuanxiapi.cn/api/Aword/")
        if resp.is_success:
            ret = resp.json()["duanju"]
        else:
            ret = "获取失败！"
        return Message(ret)

class Func(Protocol):
    # 声明为函数
    async def __call__(self) -> Optional[Message]:
        ...

@dataclass
class Source:
    # 用来存储数据的类
    name: str
    keywords: Tuple[str, ...]
    func: Func

sources = [
    Source("history", ("历史", "历史上的今天"), _history),  
    Source("brief", ("简报", "每日简报"), _brief),
    Source("soup", ("人生语录", "鸡汤"), _soup1),
    Source("bad_soup", ("随机一言", "毒鸡汤"), _soup2),
    Source("poem", ("诗词", "诗", "今日诗词"), _poem),
    Source("paragrah", ("段子",), _paragraph)
]