# Inline Credit recode by Koala @manusiarakitann

import io
import json
import math
import os
import re
import time

from telethon import Button, custom, events

from . import CMD_LIST, koalalive
from platform import python_version

from telethon import version
from telethon import __version__, version
from userbot import ALIVE_LOGO, ALIVE_NAME, BOT_VER, CMD_HELP, StartTime, bot, get_readable_time
from userbot.events import register
DEFAULTUSER = ALIVE_NAME or "kampang"
ALIVE_LOGO = Config.ALIVE_LOGO
KAMPANG_TEKS_KUSTOM = Config.KAMPANG_TEKS_KUSTOM or "🐨 𝐁𝐎𝐓-𝐊𝐀𝐌𝐏𝐀𝐍𝐆 MENYALA ANJENG 🐨"
BTN_URL_REGEX = re.compile(
    r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")


@register(outgoing=True, pattern=r"^\.(?:zalive|on)\s?(.)?")
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if ALIVE_LOGO:
        bot_kampang = f"**┏▼━━━━━━━━━━━━━━━━━━━▼┓**\n"
        bot_kampang += f"**{KAMPANG_TEKS_KUSTOM}**\n\n"
        bot_kampang += f"**Tҽɳɠҽɳƚσƚ :** `{version.__version__}\n`"
        bot_kampang += f"**Vҽɾʂι Kαɱραɳɠ :** `{BOT_VER}`\n"
        bot_kampang += f"**Pყƚԋσɳ  :** `{python_version()}\n`"
        bot_kampang += f"**Uptime :** `{uptime}\n`"
        bot_kampang += f"**ƙąɱ℘ąŋɠ:** {DEFAULTUSER}\n"
        bot_kampamg += f" **𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃 :** [BOT KAMPANG](https://github.com/ManusiaRakitan/Kampang-Bot)\n🐨 **Grup Official: **[Pencet Asu](t.me/caritemanhidop)\n☬ **ѕυρρσят ву:** [KOALA 🐨](t.me/manusiarakitann)\n"
        bot_kampamg += f"**┗▲━━━━━━━━━━━━━━━━━━━▲┛**")
        await alive.client.send_file(
            alive.chat_id, ALIVE_LOGO, caption = bot_kampang, reply_to = reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**┏▼━━━━━━━━━━━━━━━━━━━▼┓**\n"
            f"**{KAMPANG_TEKS_KUSTOM}**\n\n"
            f"**Tҽɳɠҽɳƚσƚ :** `{version.__version__}\n`"
            f"**Vҽɾʂι Kαɱραɳɠ :** `{BOT_VER}`\n"
            f"**Pყƚԋσɳ :** `{python_version()}\n`"
            f"**Uptime :** `{uptime}\n`"
            f"**f"**ƙąɱ℘ąŋɠ: ** {DEFAULTUSER}\n"
            f"**𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃 :** [BOT KAMPANG](https://github.com/ManusiaRakitan/Kampang-Bot)\n🐨 **Grup Official: **[Pencet Asu](t.me/caritemanhidop)\n☬ **ѕυρρσят ву:** [KOALA 🐨](t.me/manusiarakitann)\n"
            f"┗▲━━━━━━━━━━━━━━━━━━━▲┛**"
        )

@ register(outgoing = True, pattern = r"^\.(?:koalalive|on)\s?(.)?")
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    tgbotusername=Config.BOT_USERNAME
    reply_to_id=await reply_id(alive)
        bot_kampang=f"**┏▼━━━━━━━━━━━━━━━━━━━▼┓**\n"
        bot_kampang += f **☬ 𝐁𝐎𝐓 𝐊𝐀𝐌𝐏𝐀𝐍𝐆 ☬**\n"
        bot_kampang += f"**Tҽɳɠҽɳƚσƚ :** `{version.__version__}\n`"
        bot_kampang += f"**Vҽɾʂι Kαɱραɳɠ :** `{BOT_VER}`\n"
        bot_kampang += f"**Pყƚԋσɳ  :** `{python_version()}\n`"
        bot_kampang += f"**Uptime :** `{uptime}\n`"
        bot_kampang += f"**ƙąɱ℘ąŋɠ:** {DEFAULTUSER}\n"
        bot_kampang += f" **𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃 :** [BOT KAMPANG](https://github.com/ManusiaRakitan/Kampang-Bot)\n🐨 **Grup Official: **[Pencet Asu](t.me/caritemanhidop)\n☬ **ѕυρρσят ву:** [KOALA 🐨](t.me/manusiarakitann)\n"
        bot_kampang += f"**┗▲━━━━━━━━━━━━━━━━━━━▲┛**")
results=await bot.inline_query(tgbotusername, bot_kampang)  # pylint:disable=E0602
    await results[0].click(alive.chat_id, reply_to=reply_to_id, hide_via=True)
    await alive.delete()


if Config.BOT_USERNAME is not None and tgbot is not None:

    @ tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder=event.builder
        result=None
        query=event.text
        hmm=re.compile("secret (.*) (.*)")
        match=re.findall(hmm, query)
        if query.startswith(
            "**𝐁𝐎𝐓-𝐊𝐀𝐌𝐏𝐀𝐍𝐆") and event.query.user_id == bot.uid:
            buttons=[
                (
                    custom.Button.inline("Stats", data="stats"),
                    Button.url(
    "𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃",
     "https://github.com/manusiarakitan/kampang-bot"),

                    custom.Button.inline("Stats", data="stats"),
                    Button.url("𝓚𝓸𝓪𝓵𝓪 🐨", "https://t.me/manusiarakitann"),
                )
            ]
            if ALIVE_LOGO and ALIVE_LOGO.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALIVE_LOGO,
                    # title="𝐁𝐎𝐓-𝐊𝐀𝐌𝐏𝐀𝐍𝐆",
                    text=query,
                    buttons=buttons,
                )
            elif ALIVE_LOGO:
                result = builder.document(
                    ALIVE_LOGO,
                    title="𝐁𝐎𝐓-𝐊𝐀𝐌𝐏𝐀𝐍𝐆",
                    text=query,
                    buttons=buttons,
                )
            else:
                result = builder.article(
                    title="𝐁𝐎𝐓-𝐊𝐀𝐌𝐏𝐀𝐍𝐆"",
                    text=query,
                    buttons=buttons,
                )
            
            await event.answer([result] if result else None)
        elif event.query.user_id == bot.uid and query.startswith("Inline buttons"):
            markdown_note = query[14:]
            prev = 0
            note_data = ""
            buttons = []
            for match in BTN_URL_REGEX.finditer(markdown_note):
                # Check if btnurl is escaped
                n_escapes = 0
                to_check = match.start(1) - 1
                while to_check > 0 and markdown_note[to_check] == "\\":
                    n_escapes += 1
                    to_check -= 1
                # if even, not escaped -> create button
                if n_escapes % 2 == 0:
                    # create a thruple with button label, url, and newline
                    # status
                    buttons.append(
                        (match.group(2), match.group(3), bool(match.group(4)))
                    )
                    note_data += markdown_note[prev : match.start(1)]
                    prev = match.end(1)
                # if odd, escaped -> move along
                elif n_escapes % 2 == 1:
                    note_data += markdown_note[prev:to_check]
                    prev = match.start(1) - 1
                else:
                    break
            else:
                note_data += markdown_note[prev:]
            message_text = note_data.strip()
            tl_ib_buttons = ibuild_keyboard(buttons)
            result = builder.article(
                title="Inline creator",
                text=message_text,
                buttons=tl_ib_buttons,
                link_preview=False,
            )
            await event.answer([result] if result else None)
        elif event.query.user_id == bot.uid and match:
            query = query[7:]
            user, txct = query.split(" ", 1)
            builder = event.builder
            secret = os.path.join("./userbot", "secrets.txt")
            try:
                jsondata = json.load(open(secret))
            except Exception:
                jsondata = False
            try:
                # if u is user id
                u = int(user)
                try:
                    u = await event.client.get_entity(u)
                    if u.username:
                        koala = f"@{u.username}"
                    else:
                        koala = f"[{u.first_name}](tg://user?id={u.id})"
                except ValueError:
                    # ValueError: Could not find the input entity
                    koala = f"[user](tg://user?id={u})"
            except ValueError:
                # if u is username
                try:
                    u = await event.client.get_entity(user)
                except ValueError:
                    return
                if u.username:
                    koala = f"@{u.username}"
                else:
                    koala = f"[{u.first_name}](tg://user?id={u.id})"
                u = int(u.id)
            except Exception:
                return
            timestamp = int(time.time() * 2)
            newsecret = {str(timestamp): {"userid": u, "text": txct}}

            buttons = [
                custom.Button.inline("Buka Pesan Rahasia 🔐", data=f"secret_{timestamp}")
            ]
            result = builder.article(
                title="secret message",
                text=f"🔒 Mengirim Pesan Rahasia Ke {koala}, Hanya Anak Kampang Yang Bisa Membuka Nya.",
                buttons=buttons,
            )
            await event.answer([result] if result else None)
            if jsondata:
                jsondata.update(newsecret)
                json.dump(jsondata, open(secret, "w"))
            else:
                json.dump(newsecret, open(secret, "w"))


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working=False
    output="No Database is set"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.modules.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output=f"❌ {str(e)}"
        is_database_working=False
    else:
        output="Functioning Normally"
        is_database_working=True
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
