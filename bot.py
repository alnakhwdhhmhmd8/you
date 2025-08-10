from pyrogram import Client, idle
from pyromod import listen

OWNER_ID = int(f"7728230165")
ch = "xvwwvl" 
OWNER_USERNAME = "wwvvwl"
ST = "wwvvwl"
LT = "wwvvwl"
DEVS = []
DEVS.append(OWNER_USERNAME)
DEVS.append(ST)
DEVS.append(LT)
OWNER = "ᴊᴀᴋلـ"

bot_token="8490252476:AAE4BgPkVWENSnJGc6WRyZ852svWY9KRZTU"
bot_token2="BAFF9UIAaoYWHhc0a2WtGVDzLutEhpsTDI5CKI5cywpcu4hboeegyWN8bzfYK21_IObgBiU5uLXvkXbRopvrAgf_WvH2UE5n97annM4RyIWkspg04Xceb17eKnbCIkL8bJ0nDph2nXXuzfPwphalcdGjes5Q73ZLw0RkHtU7kjkp7gquE2wuWAV1qwecMasqRpbC7bGGl2E1zgmNvib4eulxle9yHv6ICy7LvkFGTBvSUUtfCFSSfxq-ItkOTos5QdOB-5zxj1Od9dzsyMl0XVd9qJ2HcvWfNH93MkyQPdkdK9lkcwmvBKcg_2yplZYqiTSYLaNJlqiEACPmQtnh4rcCHSwaRgAAAAHMo28VAA"


bot = Client("ITA", api_id=8186557, api_hash="efd77b34c69c164ce158037ff5a0d117", bot_token=bot_token, plugins=dict(root="CASER"))
lolo = Client("hossam", api_id=8186557, api_hash="efd77b34c69c164ce158037ff5a0d117", session_string=bot_token2)    

bot_id = bot.bot_token.split(":")[0]

async def start_zombiebot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    await lolo.start()
    try:
      await bot.send_message(OWNER_USERNAME, "**تم تشغيل الصانع بنجاح..💗**")
    except:
      pass
    await idle()
