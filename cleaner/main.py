import discord
import asyncio

# توكن البوت الخاص بك
BOT_TOKEN = "MTMyMTA5MDU2NzM4NzYxNTIzMg.G_nBnX.7PMPS2O5SVhaGAdCRRqvnHWSJb8Y2MEsq4bfLk"
TARGET_CHANNEL_ID = 1320785017068195911  # ضع ID الغرفة التي تريد حذف الرسائل منها
DELETE_INTERVAL = 8  # بالثواني

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"تم تسجيل الدخول كبوت: {client.user}")

@client.event
async def on_message(message):
    if message.channel.id == TARGET_CHANNEL_ID and not message.author.bot:
        await asyncio.sleep(DELETE_INTERVAL)
        try:
            await message.delete()
            print(f"تم حذف الرسالة: {message.content}")
        except discord.Forbidden:
            print("لا يملك البوت صلاحيات حذف الرسائل.")
        except discord.NotFound:
            print("الرسالة غير موجودة بالفعل.")

client.run(BOT_TOKEN)
