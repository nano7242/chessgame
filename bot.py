from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Ссылка на страницу с игрой на GitHub Pages
url = 'https://nano7242.github.io/chessgame/index.html'

# Функция обработчика команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Играть", url=url)]  # Здесь подставляем правильную ссылку
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Привет, я шахматный бот! Нажми на кнопку, чтобы начать игру.', reply_markup=reply_markup)

def main():
    # Установите свой токен, полученный от BotFather
    token = '7587621615:AAHtRHgqAtXsfFLr1FSkHrXjFBvFtC9rgtE'

    # Создаем объект Application
    application = Application.builder().token(token).build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()

