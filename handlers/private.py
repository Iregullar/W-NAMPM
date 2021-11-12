from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("https://i.ytimg.com/vi/tt1A_9AsCjM/maxresdefault.jpg")
    await message.reply_text(
        f"""Ben **{bn}** !!
Grubunuzun sesli ve görüntülü sohbetinde müzik çalmak için tasarlan bir botum, Bana Mp3 Formatında Şarkıları Veriniz. Komutlarım Aşağıdaki Gibidir:
🔥 /oynat - Yanıtlanan ses dosyasını veya YouTube videosunu linki url aracılığıyla oynatılır. 
🔥 /dinle - YouTube üzerinden müzik bulut. 
🔥 /bul - İstenilen parçayı kısa sürede bulmak için
🔥 /durdur - Sesli Sohbeti durdurmak için
🔥 /devam - Sesli sohbeti devam ettirir. 
🔥 /atla - Geçerli Ses Atlanır. 
🔥 /son - Sırayı temizler ve Sesli Sohbet Müziklerinin listesini kaldırır.
💡 /asistan - Userbot Grubunuza Katılır.
💡 /asistanby - Userbot Grubunuzdan Ayrılır. 
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Sohbet", url="https://t.me/RakuneCengzerin"

                    ),
                    InlineKeyboardButton(
                        "📣 Kanal", url="https://t.me/Sirigolestan"
                    ),                    
                    InlineKeyboardButton(
                        "🇹🇷 Sahip", url="https://t.me/ormancocuklariylamucadele" 
                    ), 
                ]
            ]
        )
    )
    

