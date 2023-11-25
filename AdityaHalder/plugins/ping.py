from .. import *
from datetime import datetime


@app.on_message(commandx(["ping"]) & SUDOERS)
async def alive_check(client, message):
    start = datetime.now()
    m = await eor(message, "**🩸𝗣𝗢𝗡𝗚 𝗕𝗔𝗕𝗬 !**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await m.edit(f"**🩸𝗣𝗜𝗡𝗚𝗘𝗗 !\nLatency:** `{ms}` ms")


__NAME__ = "Ping"
__MENU__ = f"""
**🥀 𝗖𝗛𝗘𝗖𝗞 𝗨𝗦𝗘𝗥𝗕𝗢𝗧 
𝗣𝗜𝗡𝗚 𝗟𝗔𝗧𝗘𝗡𝗖𝗬 ✨...**

**Example:** `.ping`
"""
