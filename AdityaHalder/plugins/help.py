import re

from .. import *
from .. import __version__
from .inline import *
from ..modules.misc import *
from ..modules.utils import *

from pyrogram import *
from pyrogram.types import *


@app.on_message(commandx(["help"]))
async def inline_help_menu(client, message: Message):
   try:
       if var.USERBOT_PICTURE:
         bot_results = await app.get_inline_bot_results(
            f"@{bot.username}", "help_menu_logo"
         )
       else:
         bot_results = await app.get_inline_bot_results(
            f"@{bot.username}", "help_menu_text"
         )
       await app.send_inline_bot_result(
         chat_id=message.chat.id,
         query_id=bot_results.query_id,
         result_id=bot_results.results[0].id,
       )
   except Exception:
       bot_results = await app.get_inline_bot_results(
          f"@{bot.username}", "help_menu_text"
       )
       await app.send_inline_bot_result(
         chat_id=message.chat.id,
         query_id=bot_results.query_id,
         result_id=bot_results.results[0].id,
       )
   except Exception as e:
       print(e)
       return

   try:
      await message.delete()
   except:
      pass
      


@bot.on_callback_query(filters.regex(r"help_(.*?)"))
@cb_wrapper
async def help_button(client, query):
    plug_match = re.match(r"help_plugin\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    top_text = f"""
**🥀 𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗛𝗘𝗟𝗣 𝗠𝗘𝗡𝗨
𝗦𝗔𝗥𝗞𝗔𝗥 𝗨𝗦𝗘𝗥𝗕𝗢𝗧 » {__version__} ✨...

𝗖𝗟𝗜𝗖𝗞 𝗢𝗡 𝗕𝗘𝗟𝗢𝗪 𝗕𝗨𝗧𝗧𝗢𝗡 𝗧𝗢
𝗚𝗘𝗧 𝗨𝗦𝗘𝗥𝗕𝗢𝗧.

🌷𝗣𝗢𝗪𝗘𝗥𝗗 𝗕𝗬 : [𝗦𝗔𝗥𝗞𝗔𝗥](https://t.me/ll_SARKAR_BABE_ll).**"""
    if plug_match:
        plugin = plug_match.group(1)
        text = (
            "**♨️ 𝗣𝗟𝗨𝗚𝗜𝗡 :** {}\n".format(
                PLUGINS[plugin].__NAME__
            )
            + PLUGINS[plugin].__MENU__
        )
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="↪️ 𝗕𝗔𝗖𝗞", callback_data="help_back"
                    )
                ],
            ]
        )

        await bot.edit_inline_text(
            query.inline_message_id,
            text=text,
            reply_markup=key,
            disable_web_page_preview=True
        )
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await bot.edit_inline_text(
            query.inline_message_id,
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(curr_page - 1, PLUGINS, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await bot.edit_inline_text(
            query.inline_message_id,
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(next_page + 1, PLUGINS, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await bot.edit_inline_text(
            query.inline_message_id,
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(0, PLUGINS, "help")
            ),
            disable_web_page_preview=True,
        )
