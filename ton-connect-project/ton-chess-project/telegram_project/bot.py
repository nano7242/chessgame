from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Токен вашего бота
TOKEN = '7587621615:AAHtRHgqAtXsfFLr1FSkHrXjFBvFtC9rgtE'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправка сообщения с кнопкой для открытия веб-страницы"""
    
    # Создаем кнопку с ссылкой
    keyboard = [
        [InlineKeyboardButton("Открыть веб-страницу", url='https://yourwebsite.com')]  # Замените на нужную ссылку
    ]
    
    # Создаем разметку с кнопкой
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Отправляем сообщение с кнопкой
    await update.message.reply_text('Привет! Нажми на кнопку ниже, чтобы открыть веб-страницу:', reply_markup=reply_markup)

def main() -> None:
    """Запуск бота"""
    # Создаем приложение с новым API
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Токен вашего бота
TOKEN = '7587621615:AAHtRHgqAtXsfFLr1FSkHrXjFBvFtC9rgtE'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправка приветственного сообщения при старте"""
    await update.message.reply_text('Привет! Я ваш бот.')

def main() -> None:
    """Запуск бота"""
    # Создаем приложение с новым API
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
