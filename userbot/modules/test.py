# Inline Credit recode by Koala @manusiarakitann

import time
from platform import python_version

import logging
from telethon import version
from userbot import ALIVE_LOGO, ALIVE_NAME, KAMPANG_TEKS_KUSTOM, BOT_VER, CMD_HELP, StartTime, bot, BOT_USERNAME
from userbot.events import register
DEFAULTUSER = ALIVE_NAME or "kampang"
KOALA_PIC = ALIVE_LOGO or None
KAMPANGTEKS = KAMPANG_TEKS_KUSTOM or "🐨 𝐁𝐎𝐓-𝐊𝐀𝐌𝐏𝐀𝐍𝐆 MENYALA ANJENG 🐨"

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.WARNING)


@register(outgoing=True, pattern=r"^\.(?:zalive|on)\s?(.)?")
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    await bot.get_me()
    await get_readable_time((time.time() - StartTime))
    if KOALA_PIC:
        bot_kampang = f"**┏▼━━━━━━━━━━━━━━━━━━━▼┓**\n"
        bot_kampang += f"**{KAMPANGTEKS}**\n\n"
        bot_kampang += f"**Tҽɳɠҽɳƚσƚ :** `{version.__version__}\n`"
        bot_kampang += f"**Vҽɾʂι Kαɱραɳɠ :** `{BOT_VER}`\n"
        bot_kampang += f"**Pყƚԋσɳ  :** `{python_version()}\n`"
        bot_kampang += f"**Uptime :** `{uptime}\n`"
        bot_kampang += f"**ƙąɱ℘ąŋɠ:** {DEFAULTUSER}\n"
        bot_kampang += f" **𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃 :** [BOT KAMPANG](https://github.com/ManusiaRakitan/Kampang-Bot)\n🐨 **Grup Official: **[Pencet Asu](t.me/caritemanhidop)\n☬ **ѕυρρσят ву:** [KOALA 🐨](t.me/manusiarakitann)\n"
        bot_kampang += f"**┗▲━━━━━━━━━━━━━━━━━━━▲┛**"
        await bot.send_file(
            alive.chat_id,
            KOALA_PIC,
            caption=bot_kampang,
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**┏▼━━━━━━━━━━━━━━━━━━━▼┓**\n"
            f"**{KAMPANGTEKS}**\n\n"
            f"**Tҽɳɠҽɳƚσƚ :** `{version.__version__}\n`"
            f"**Vҽɾʂι Kαɱραɳɠ :** `{BOT_VER}`\n"
            f"**Pყƚԋσɳ :** `{python_version()}\n`"
            f"**Uptime :** `{uptime}\n`"
            f"**ƙąɱ℘ąŋɠ : ** {DEFAULTUSER}\n"
            f"**𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃 :** [BOT KAMPANG](https://github.com/ManusiaRakitan/Kampang-Bot)\n🐨 **Grup Official: **[Pencet Asu](t.me/caritemanhidop)\n☬ **ѕυρρσят ву:** [KOALA 🐨](t.me/manusiarakitann)\n"
            f"**┗▲━━━━━━━━━━━━━━━━━━━▲┛**"
        )


@register(outgoing=True, pattern=r"^\.(?:koalalive|on)\s?(.)?")
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    tgbotusername = BOT_USERNAME
    reply_to_id = await reply_id(alive)
    bot_kampang = f"**┏▼━━━━━━━━━━━━━━━━━━━▼┓**\n"
    bot_kampang += f"**☬ 𝐁𝐎𝐓 𝐊𝐀𝐌𝐏𝐀𝐍𝐆 ☬**\n\n"
    bot_kampang += f"**Tҽɳɠҽɳƚσƚ :** `{version.__version__}\n`"
    bot_kampang += f"**Vҽɾʂι Kαɱραɳɠ :** `{BOT_VER}`\n"
    bot_kampang += f"**Pყƚԋσɳ  :** `{python_version()}\n`"
    bot_kampang += f"**Uptime :** `{uptime}\n`"
    bot_kampang += f"**ƙąɱ℘ąŋɠ :** {DEFAULTUSER}\n"
    bot_kampang += f"**𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃 :** [BOT KAMPANG](https://github.com/ManusiaRakitan/Kampang-Bot)\n🐨 **Grup Official: **[Pencet Asu](t.me/caritemanhidop)\n☬ **ѕυρρσят ву:** [KOALA 🐨](t.me/manusiarakitann)\n"
    bot_kampang += f"**┗▲━━━━━━━━━━━━━━━━━━━▲┛**"
    results = await bot.inline_query(tgbotusername, bot_kampang)  # pylint:disable=E0602
    await results[0].click(alive.chat_id, reply_to=reply_to_id, hide_via=True)
    await alive.delete()


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.modules.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning Normally"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "kampang": "**Modules :** `kampang`\
      \n\n  •  **Perintah : **`.zalive` \
      \n  •  **Keterangan : **__untuk mengetahui info bot asu__\
      \n\n  •  **Perintah : **`.koalalive` \
      \n  •  **Keterangan : **__untuk mengetahui info bot via inline mode.__\
      \nSet `ALIVE_LOGO` Untuk mengubah media di info bot"
    }
)
