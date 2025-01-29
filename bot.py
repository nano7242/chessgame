from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Функция обработчика команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Играть", url='https://ваш_репозиторий.github.io/your_project/index.html')]
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

