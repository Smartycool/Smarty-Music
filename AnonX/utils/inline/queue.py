from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["𝐐𝐔_𝐁_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["𝐂𝐋𝐎𝐒𝐄𝐌𝐄𝐍𝐔_𝐁𝐔𝐓𝐓𝐎𝐍"],
                callback_data="close",
            ),
        ]
    ]
    dur = [
        [
            InlineKeyboardButton(
                text=_["𝐐𝐔_𝐁_2"].format(played, dur),
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["𝐐𝐔_𝐁_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["𝐂𝐋𝐎𝐒𝐄𝐌𝐄𝐍𝐔_𝐁𝐔𝐓𝐓𝐎𝐍"],
                callback_data="close",
            ),
        ],
    ]
    upl = InlineKeyboardMarkup(
        not_dur if DURATION == "Unknown" else dur
    )
    return upl


def queue_back_markup(_, CPLAY):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["𝐁𝐀𝐂𝐊_𝐁𝐔𝐓𝐓𝐎𝐍"],
                    callback_data=f"queue_back_timer {CPLAY}",
                ),
                InlineKeyboardButton(
                    text=_["𝐂𝐋𝐎𝐒𝐄_𝐁𝐔𝐓𝐓𝐎𝐍"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
