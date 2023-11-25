from .. import SUDOERS
from pyrogram.types import *
from traceback import format_exc
from typing import Callable


def sudo_user_only(func: Callable) -> Callable:
    async def decorator(client, message: Message):
        if message.from_user.id in SUDOERS:
            return await func(client, message)
        
    return decorator


def cb_wrapper(func):
    async def wrapper(bot, cb):
        from .. import bot
        users = SUDOERS
        if cb.from_user.id not in users:
            await cb.answer(
                "❎ You Are Not A Sudo User❗",
                cache_time=0,
                show_alert=True,
            )
        else:
            try:
                await func(bot, cb)
            except Exception:
                print(format_exc())
                await cb.answer(
                    f"❎ Something Went Wrong, Please Check Logs❗..."
                )

    return wrapper


def inline_wrapper(func):
    async def wrapper(bot, query):
        from .. import bot
        users = SUDOERS
        if query.from_user.id not in users:
            try:
                button = [
                    [
                        InlineKeyboardButton(
                            "💥 𝗠𝗬 𝗕𝗢𝗧 𝗢𝗪𝗡𝗘𝗥✨",
                            url=f"https://t.me/ll_SARKAR_BABE_ll"
                        )
                    ]
                ]
                await bot.answer_inline_query(
                    query.id,
                    cache_time=1,
                    results=[
                        (
                            InlineQueryResultPhoto(
                                photo_url=f"https://telegra.ph/file/51d2a8d64d64b798347d0.jpg",
                                title="🥀 𝗦𝗔𝗥𝗞𝗔𝗥 𝗨𝗦𝗘𝗥𝗕𝗢𝗧✨",
                                thumb_url=f"https://telegra.ph/file/51d2a8d64d64b798347d0.jpg",
                                description=f"𝗦𝗔𝗥𝗞𝗔𝗥 𝗨𝗦𝗘𝗥...",
                                caption=f"<b>🥀 𝗪𝗘𝗟𝗖𝗢𝗠𝗘 › 𝗧𝗢 › 𝗦𝗔𝗥𝗞𝗔𝗥 🌷\n✅ 𝗨𝗦𝗘𝗥𝗕𝗢𝗧 v2.0 ✨...</b>",
                                reply_markup=InlineKeyboardMarkup(button),
                            )
                        )
                    ],
                )
            except Exception as e:
                print(str(e))
                await bot.answer_inline_query(
                    query.id,
                    cache_time=1,
                    results=[
                        (
                            InlineQueryResultArticle(
                                title="",
                                input_message_content=InputTextMessageContent(
                                    f"||**🥀𝗢𝗪𝗡𝗘𝗥❗...\n\n𝗨𝗦𝗘𝗥:** <i>https://t.me/ll_SARKAR_BABE_ll/</i>||"
                                ),
                            )
                        )
                    ],
                )
            except Exception as e:
                print(str(e))
                pass
        else:
           return await func(bot, query)

    return wrapper
