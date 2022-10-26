from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN

@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=f"<b><i>Hello 👋 {msg.from_user.mention},\n\nI Am Simple Renamer Bot With Permanent Thumbnail Support.\n\nMaintained By ✔️ <a href=https://t.me/hellobikash77>Bikash</a></b></i>"                                     
    button= [[
        InlineKeyboardButton("🔗 Support", url="https://t.me/TechSupportChat")
        InlineKeyboardButton("🔔 Updates", url="https://t.me/Tech_Projects2021")
        ],[
        InlineKeyboardButton("ℹ️ Help", callback_data="help"),
        InlineKeyboardButton("😎 About", callback_data="about") 
    ]]  
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt=f"just send a file and /rename <new name> with replayed your file\n\nReply a photo and send /set to set temporary thumbnail\n/view to see your thumbnail"
    button= [[        
        InlineKeyboardButton("🔐 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    txt=f"<b>🤖 Bot Name: {me.mention}\n👨‍💻 Developer: <a href=https://t.me/hellobikash77>Bikash</a></b>"                 
    button= [[        
        InlineKeyboardButton("🔐 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return
