import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s', level=logging.INFO)

TOKEN = '8146113652:AAGslYn8-P6wSZOAjKiYsE_vbxH_1s72Apo'  # Ваш токен бота

# Словарь для хранения заявок
requests = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Отправьте фотографию с текстом для обработки.')


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Получаем фото и текст
    photo_file = update.message.photo[-1].file_id  # Получаем файл фотографии
    text = update.message.caption if update.message.caption else "Без текста"  # Получаем текст

    # Сохраняем заявку
    request_id = len(requests) + 1
    requests[request_id] = {'photo': photo_file, 'text': text}

    # Создаем кнопки
    keyboard = [
        [InlineKeyboardButton("Лайк", callback_data=f'like_{request_id}'),
         InlineKeyboardButton("Дизлайк", callback_data=f'dislike_{request_id}')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем фото и текст с кнопками
    await update.message.reply_photo(photo=photo_file, caption=text, reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    request_id = int(query.data.split('_')[1])
    if query.data.startswith('like'):
        requests[request_id]['value'] = 1  # Лайк
        await query.edit_message_text(text=f"Заявка {request_id} получила оценку: 1 (Лайк)")
    elif query.data.startswith('dislike'):
        requests[request_id]['value'] = 0  # Дизлайк
        await query.edit_message_text(text=f"Заявка {request_id} получила оценку: 0 (Дизлайк)")


async def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    # Регистрация обработчиков
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    application.add_handler(CallbackQueryHandler(button))

    await application.run_polling()


# Запуск бота
if __name__ == '__main__':
    try:
        asyncio.run(main())  # Используем asyncio.run для запуска основной функции
    except RuntimeError as e:
        if 'This event loop is already running' in str(e):
            print("Обнаружен уже работающий цикл событий. Возможно, бот уже запущен.")
        else:
            raise
