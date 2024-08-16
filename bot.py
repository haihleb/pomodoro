from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import CommandHandler, ApplicationBuilder, CallbackContext

# Токен вашего бота
TOKEN = '7183366630:AAFJ2oGRRkQ61Diy-hZDsrFbjCyQuO67PQ0'

# Обработчик команды /start
async def start(update: Update, context: CallbackContext) -> None:
    # URL вашего Pomodoro таймера
    web_app_url = "https://t.me/be_focused_bot/pomodoro"
    
    # Создаем кнопку для открытия Web App
    keyboard = [
        [InlineKeyboardButton("Запустить Pomodoro", web_app=WebAppInfo(url=web_app_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Отправляем сообщение с кнопкой
    await update.message.reply_text('Нажмите на кнопку ниже, чтобы запустить Pomodoro таймер:', reply_markup=reply_markup)

# Основная функция для запуска бота
def main() -> None:
    # Создаем приложение
    application = ApplicationBuilder().token(TOKEN).build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота и начинаем прослушивание сообщений
    application.run_polling()

if __name__ == '__main__':
    main()
