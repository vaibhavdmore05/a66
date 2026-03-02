from telegram im port update 
from telegram.ext import applicationbuilder ,commandhandler, contexttypes

async def hello(update:update, context:contexttypes.default-type) -> none:
   await update.message.reply_text(f'hello{update.effective_user.first_name}')



   app = applicationbuilder().token("7940204027:AAH3lTgEM_VGlkqYfq-tyROVL0QcEyg_Ol0")    

app.add_handler(commandhandler("hello", hello))

app.run_polling()
print("our bot is started Oo")