from typing import Union

from pyrogram.types import InlineKeyboardButton
from config import SUPPORT_GROUP


def setting_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀𝐔𝐃𝐈𝐎 𝐐𝐔𝐀𝐋𝐈𝐓𝐘", callback_data="AQ"
            ),
            InlineKeyboardButton(
                text="𝐕𝐈𝐃𝐄𝐎 𝐐𝐔𝐀𝐋𝐈𝐓𝐘", callback_data="VQ"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐀𝐔𝐓𝐇 𝐔𝐒𝐄𝐑𝐒", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="𝐂𝐋𝐄𝐀𝐍 𝐌𝐎𝐃𝐄", callback_data="CM"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❄ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 ❄", url=f"{SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["𝐂𝐋𝐎𝐒𝐄_𝐁𝐔𝐓𝐓𝐎𝐍"], callback_data="close"
            ),
        ],
    ]
    return buttons


def audio_quality_markup(
    _,
    low: Union[bool, str] = None,
    medium: Union[bool, str] = None,
    high: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝐒𝐓_𝐁_8"].format("➻")
                if low == True
                else _["𝐒𝐓_𝐁_8"].format(""),
                callback_data="LQA",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["𝐒𝐓_𝐁_9"].format("➻")
                if medium == True
                else _["𝐒𝐓_𝐁_9"].format(""),
                callback_data="MQA",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["𝐒𝐓_𝐁_10"].format("➻")
                if high == True
                else _["𝐒𝐓_𝐁_10"].format(""),
                callback_data="HQA",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["𝐁𝐀𝐂𝐊_𝐁𝐔𝐓𝐓𝐎𝐍"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text=_["𝐂𝐋𝐎𝐒𝐄_𝐁𝐔𝐓𝐓𝐎𝐍"], callback_data="close"
            ),
        ],
    ]
    return buttons


def video_quality_markup(
    _,
    low: Union[bool, str] = None,
    medium: Union[bool, str] = None,
    high: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝐒𝐓_𝐁_11"].format("➻")
                if low == True
                else _["𝐒𝐓_𝐁_11"].format(""),
                callback_data="LQV",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["𝐒𝐓_𝐁_12"].format("➻")
                if medium == True
                else _["𝐒𝐓_𝐁_12"].format(""),
                callback_data="MQV",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["ST_B_13"].format("➻")
                if high == True
                else _["ST_B_13"].format(""),
                callback_data="HQV",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["𝐁𝐀𝐂𝐊_𝐁𝐔𝐓𝐓𝐎𝐍"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text=_["𝐂𝐋𝐎𝐒𝐄_𝐁𝐔𝐓𝐓𝐎𝐍"], callback_data="close"
            ),
        ],
    ]
    return buttons


def cleanmode_settings_markup(
    _,
    status: Union[bool, str] = None,
    dels: Union[bool, str] = None,
    sug: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝐒𝐓_𝐁_7"], callback_data="CMANSWER"
            ),
            InlineKeyboardButton(
                text=_["𝐒𝐓_𝐁_14"] if status == True else _["ST_B_15"],
                callback_data="CLEANMODE",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["𝐒𝐓_𝐁_26"], callback_data="COMMANDANSWER"
            ),
            InlineKeyboardButton(
                text=_["𝐒𝐓_𝐁_14"] if dels == True else _["ST_B_15"],
                callback_data="COMMANDELMODE",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["𝐁𝐀𝐂𝐊_𝐁𝐔𝐓𝐓𝐎𝐍"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text=_["𝐂𝐋𝐎𝐒𝐄_𝐁𝐔𝐓𝐓𝐎𝐍"], callback_data="close"
            ),
        ],
    ]
    return buttons


def auth_users_markup(_, status: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝐒𝐓_𝐁_3"], callback_data="AUTHANSWER"
            ),
            InlineKeyboardButton(
                text=_["𝐒𝐓_𝐁_16"] if status == True else _["ST_B_17"],
                callback_data="AUTH",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["𝐒𝐓_𝐁_18"], callback_data="AUTHLIST"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["𝐁𝐀𝐂𝐊_𝐁𝐔𝐓𝐓𝐎𝐍"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text=_["𝐂𝐋𝐎𝐒𝐄_𝐁𝐔𝐓𝐓𝐎𝐍"], callback_data="close"
            ),
        ],
    ]
    return buttons


def playmode_users_markup(
    _,
    Direct: Union[bool, str] = None,
    Group: Union[bool, str] = None,
    Playtype: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝐒𝐓_𝐁_19"], callback_data="SEARCHANSWER"
            ),
            InlineKeyboardButton(
                text=_["𝐒𝐓_𝐁_20"] if Direct == True else _["ST_B_21"],
                callback_data="MODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["𝐒𝐓_𝐁_22"], callback_data="AUTHANSWER"
            ),
            InlineKeyboardButton(
                text=_["𝐒𝐓_𝐁_16"] if Group == True else _["ST_B_17"],
                callback_data="CHANNELMODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["𝐒𝐓_𝐁_25"], callback_data="PLAYTYPEANSWER"
            ),
            InlineKeyboardButton(
                text=_["𝐒𝐓_𝐁_16"]
                if Playtype == True
                else _["ST_B_17"],
                callback_data="PLAYTYPECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["𝐁𝐀𝐂𝐊_𝐁𝐔𝐓𝐓𝐎𝐍"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text=_["𝐂𝐋𝐎𝐒𝐄_𝐁𝐔𝐓𝐓𝐎𝐍"], callback_data="close"
            ),
        ],
    ]
    return buttons
