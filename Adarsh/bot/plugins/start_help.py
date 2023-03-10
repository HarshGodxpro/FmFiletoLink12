# (c) adarsh-goel 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)
from pyrogram.types import ReplyKeyboardMarkup

                      
@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "banned":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**ππΎπ π°ππ΄ π±π°π½π½π΄π³../**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**πΉπΎπΈπ½ πΌπ ππΏπ³π°ππ΄π π²π·π°π½π½π΄π» ππΎ πππ΄ πΌπ΄..**\n\n**π³ππ΄ ππΎ πΎππ΄ππ»πΎπ°π³ πΎπ½π»π π²π·π°π½π½π΄π» πππ±ππ²ππΈπ±π΄ππ π²π°π½ πππ΄ ππ·πΈπ π±πΎπ..!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Join Our Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**π°π³π³ π΅πΎππ²π΄ πππ± ππΎ π°π½π π²π·π°π½π½π΄π»**",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text="**π Hα΄Κ...!**\n\n<i>I'm Telegram Files Streaming Bot As Well Direct Links Generator</i>\n\n<i>Click On Help To Get More Information</i>\n\n<b><i><u>Warning πΈ</u></i></b>\n\n<b>π Pron Contents Leads To Permanenet Ban You.</b>",
            reply_markup=InlineKeyboardMarkup(
                [[
                   InlineKeyboardButton('Κα΄Κα΄', callback_data='help'),
                   InlineKeyboardButton('α΄Κα΄α΄α΄', callback_data='about')
                ],        
                [InlineKeyboardButton("α΄α΄α΄α΄α΄α΄κ±", url='https://t.me/MovieLandLinkChannel'),
                 InlineKeyboardButton("Κα΄α΄α΄", url='https://github.com/HarshGodxpro')]
                ]
            ),
            disable_web_page_preview=True
        )
    else:
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "banned":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="__Sα΄ΚΚΚ SΙͺΚ, Yα΄α΄ α΄Κα΄ Bα΄Ι΄Ι΄α΄α΄ α΄α΄ α΄sα΄ α΄α΄.__\n\n**[Cα΄Ι΄α΄α΄α΄α΄ Dα΄α΄ α΄Κα΄α΄α΄Κ](https://t.me/PROFE07XH) TΚα΄Κ WΙͺΚΚ Hα΄Κα΄ Yα΄α΄**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**πΉπΎπΈπ½ πΌπ ππΏπ³π°ππ΄π π²π·π°π½π½π΄π» ππΎ πππ΄ πΌπ΄..**\n\n**π³ππ΄ ππΎ πΎππ΄ππ»πΎπ°π³ πΎπ½π»π π²π·π°π½π½π΄π» πππ±ππ²ππΈπ±π΄ππ π²π°π½ πππ΄ ππ·πΈπ π±πΎπ..!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Join Our Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]                           
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**π°π³π³ π΅πΎππ²π΄ πππ± ππΎ π°π½π π²π·π°π½π½π΄π»**",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id)

        msg_text = """
<u>**Successfully Generated Your Link !**</u>\n
<b>π File Name :</b> {}\n
<b>π¦ File Size :</b> {}\n
<b>π₯ Download :</b> {}\n
<b>π₯ Watch :</b> {}"""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("β‘ π³πΎππ½π»πΎπ°π³ π½πΎπ β‘", url=stream_link)]])
        )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "banned":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="Sα΄ΚΚΚ SΙͺΚ, Yα΄α΄ α΄Κα΄ Bα΄Ι΄Ι΄α΄α΄ α΄α΄ α΄sα΄ α΄α΄.\n\n**[Cα΄Ι΄α΄α΄α΄α΄ Dα΄α΄ α΄Κα΄α΄α΄Κ](https://t.me/groupdcs) TΚα΄Κ WΙͺΚΚ Hα΄Κα΄ Yα΄α΄**",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**πΉπΎπΈπ½ πΌπ ππΏπ³π°ππ΄π π²π·π°π½π½π΄π» ππΎ πππ΄ πΌπ΄..**\n\n**π³ππ΄ ππΎ πΎππ΄ππ»πΎπ°π³ πΎπ½π»π π²π·π°π½π½π΄π» πππ±ππ²ππΈπ±π΄ππ π²π°π½ πππ΄ ππ·πΈπ π±πΎπ..!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Update Channel π°", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**π°π³π³ π΅πΎππ²π΄ πππ± ππΎ π°π½π π²π·π°π½π½π΄π»**",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="**βͺΌ **How to Use Me ?**\n\nβͺΌ Send Me Any File Or Media From Telegram.\nβͺΌ I Will Provide External Direct Download Link !\n\n\nβͺΌDownload Link With Fastest Speed β‘οΈ\n\n\nWarning β οΈ\nβͺΌ π Pron Contents Leads To Permanenet Ban You.\n\nβͺΌ Contact Developer Or Report Bugs : @PROFE07XH**",
  parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [[
        InlineKeyboardButton('Κα΄α΄α΄', callback_data='start'),
        InlineKeyboardButton('α΄Κα΄α΄α΄', callback_data='about')
        ],
        [
        InlineKeyboardButton('α΄Κα΄κ±α΄', callback_data='close'),
        ],        
        ]
        )
    )

@StreamBot.on_message(filters.command('about') & filters.private & ~filters.edited)
async def about_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!β‘"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "banned":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="__Sα΄ΚΚΚ SΙͺΚ, Yα΄α΄ α΄Κα΄ Bα΄Ι΄Ι΄α΄α΄ α΄α΄ α΄sα΄ α΄α΄.__\n\n**[Cα΄Ι΄α΄α΄α΄α΄ Dα΄α΄ α΄Κα΄α΄α΄Κ](https://t.me/PROFE07XH) TΚα΄Κ WΙͺΚΚ Hα΄Κα΄ Yα΄α΄**",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**πΉπΎπΈπ½ πΌπ ππΏπ³π°ππ΄π π²π·π°π½π½π΄π» ππΎ πππ΄ πΌπ΄..**\n\n**π³ππ΄ ππΎ πΎππ΄ππ»πΎπ°π³ πΎπ½π»π π²π·π°π½π½π΄π» πππ±ππ²ππΈπ±π΄ππ π²π°π½ πππ΄ ππ·πΈπ π±πΎπ..!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Updates Channel π°", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**π?π³**",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""<b>About Me and Owner πΉ</b>

<b>β­βββββββγFile To Linkγ</b>
β
β£βͺΌ<b>β My Name : File To Link Bot</b>
β£βͺΌ<b>β Update : @{Var.UPDATES_CHANNEL}</b>
β£βͺΌ<b>πΈVersion : 3.1.2</b>
β£βͺΌ<b>πΉLast Updated : [ 21-aug-22 ]</b>
β£βͺΌ<b>β¨YouTube Channel: <a href='https://youtube.com/@violencegaming7662'>PROFE07XH Channel</a></b>
β
<b>β°βββββββγTHANK YOUγ</b>""",
  parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [[
        InlineKeyboardButton('Κα΄α΄α΄', callback_data='start'),
        InlineKeyboardButton('Κα΄Κα΄', callback_data='help')
        ]]
        )
    )
