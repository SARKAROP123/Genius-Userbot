from .. import *

@app.on_message(commandx(["alive"]))
async def alive_check(client, message):
    await message.reply_text("**🥀 𝗜 𝗔𝗠 𝗔𝗟𝗜𝗩𝗘 𝗦𝗔𝗥𝗞𝗔𝗥 𝗕𝗔𝗕𝗬 ✨ ...**")



__NAME__ = "Alive"
__MENU__ = f"""
**🥀  𝗨𝗦𝗘𝗥𝗕𝗢𝗧 𝗪𝗢𝗥𝗞𝗜𝗡𝗚 𝗕𝗔𝗕𝗬
𝗢𝗥 𝗡𝗢𝗧 ..**

**Example:** `.alive`
"""
