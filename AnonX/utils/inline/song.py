from pyrogram.types import InlineKeyboardButton
import config

def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝐒𝐆_𝐁_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["𝐒𝐆_𝐁_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥀 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🥀", url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["𝐂𝐋𝐎𝐒𝐄_𝐁𝐔𝐓𝐓𝐎𝐍"], callback_data="close"
            ),
        ],
    ]
    return buttons
