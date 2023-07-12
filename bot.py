import os
from pyrogram import Client, filters
import shutil
from os import system as cmd
bot = Client(
    "vidcomp",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5545470781:AAGjzXBuTOeJ1JulON1Cw0I2ZP8kebs2Alk"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت ضغط الفيديوهات , فقط أرسل الفيديو  هنا\n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 ",disable_web_page_preview=True)
    
@bot.on_message(filters.private & filters.incoming & filters.document | filters.video )
def _telegram_file(client, message):

  user_id = message.from_user.id 
  sent_message = message.reply_text('جار الضغط ', quote=True)
  file = message.voice
  file_path = message.download(file_name="./downloads/")
  filename = os.path.basename(file_path)
  cmd(f'mkdir workdir')
  res = "./workdir/"+filename
  cmd(f'ffmpeg -i {file_path} -vcodec libx265 -crf 28 {res}')
  with open(res, 'rb') as f:
        bot.send_video(message.chat.id, f)
  shutil.rmtree('./workdir/')
  shutil.rmtree('./downloads/')

 
 

bot.run()
