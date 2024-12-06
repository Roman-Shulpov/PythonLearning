from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
import os
import logging
from io import BytesIO
import shutil  # Для создания архивов

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен пользователя и ID администратора
TOKEN_USER = '7596367706:AAHxXabI0K4tb9TVrRtTV7ELMaN8S_LGqVY'  # Убедитесь, что токен действителен
ADMIN_CHAT_ID = '5099059098'  # Убедитесь, что это ваш chat_id

# Проверьте или создайте папку для скриншотов
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "✨ Приветствую вас! ✨\n\n"
        "Чтобы получить нашу программу для обхода ограничений в Discord и YouTube, "
        "пожалуйста, выполните следующие шаги:\n\n"
        "1. Проведите перевод на сумму 250 рублей на номер карты:\n"
        "   2200 7013 4916 7947\n\n"
        "2. После этого отправьте мне скриншот перевода, который подтвердит ваш платеж. "
        "Не забудьте указать ваше ФИО!\n\n"
        "🎉 Как только мы проверим ваш перевод, вы получите доступ к программе. "
        "Благодарим вас за понимание и терпение! 🙏\n"
        "Если будут вопросы — всегда рад помочь! 😊"
    )
    await update.message.reply_text(message)
    logger.info("Стартовое сообщение отправлено.")


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.from_user.id)  # Преобразуем ID в строку
    user_name = update.message.from_user.full_name

    # Получаем ФИО из текста сообщения
    fio = update.message.caption if update.message.caption else "Не указано"

    # Получаем файл скриншота
    file = await update.message.photo[-1].get_file()
    file_stream = await file.download_as_bytearray()

    # Создаем имя файла для сохранения
    screenshot_path = f"screenshots/{user_id}.jpg"  # Изменяем имя на основе user_id

    # Сохраняем файл на диск
    with open(screenshot_path, 'wb') as f:
        f.write(file_stream)

    # Подготовка и отправка уведомления администратору
    admin_message = f"Скриншот перевода от {user_name} (ID: {user_id})\nФИО: {fio}"
    keyboard = [
        [
            InlineKeyboardButton("Одобрить", callback_data=f"approve_{user_id}"),
            InlineKeyboardButton("Отклонить", callback_data=f"reject_{user_id}")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    try:
        await context.bot.send_photo(chat_id=5099059098, photo=open(screenshot_path, 'rb'), caption=admin_message,
                                     reply_markup=reply_markup)
        logger.info(f"Уведомление успешно отправлено админу: {admin_message}")

        # Удаляем файл после успешной отправки
        os.remove(screenshot_path)
        logger.info(f"Скриншот для пользователя {user_id} удален из базы.")

    except Exception as e:
        logger.error(f"Ошибка при отправке уведомления: {e}")

    # Уведомление для пользователя
    await update.message.reply_text("Скриншот принят. Ожидайте ответа администратора.")


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Ответ на вызов коллбэка
    user_id = query.data.split('_')[1]  # Извлекаем ID пользователя из callback_data

    if query.data.startswith('approve'):
        await handle_approval(user_id, query, context)
    elif query.data.startswith('reject'):
        await handle_rejection(user_id, query, context)


async def handle_approval(user_id: str, query, context):
    # Отправка архива пользователю
    archive_path = "general_bypass_By_Kub.rar"  # Убедитесь, что путь верный
    try:
        with open(archive_path, 'rb') as archive_file:
            await context.bot.send_document(chat_id=user_id, document=archive_file, filename="general_bypass_By_Kub.rar")

        # Отправка благодарственного сообщения
        thank_you_message = (
            "Уважаемый пользователь,\n\n"
            "Благодарим вас за покупку программы! 🎉\n\n"
            "Ваш архив успешно отправлен. Мы ценим ваше доверие и надеемся,"
            " что программа окажется полезной для вас.\n\n"
            "Обратите внимание, что инструкция по установке находится в текстовом файле внутри архива."
        )
        await context.bot.send_message(chat_id=user_id, text=thank_you_message)

        await query.edit_message_text(text=f"Заявка от пользователя {user_id} одобрена. Архив отправлен.")
    except Exception as e:
        logger.error(f"Ошибка при отправке архива: {e}")
        await query.edit_message_text(text=f"Не удалось отправить архив пользователю {user_id}.")


async def handle_rejection(user_id: str, query, context):
    reasons = [
        "1) Перевод не был выполнен.",
        "2) Не указаны ФИО.",
        "3) Скриншот может быть не подлинным."
    ]
    rejection_message = (
            "Уважаемый пользователь,\n\n"
            "К сожалению, ваша заявка была отклонена по следующим причинам:\n"
            + "\n".join(reasons) + "\n\n"
                                   "Если вы считаете, что это ошибка, пожалуйста, отправьте заявку еще раз!"
    )

    await context.bot.send_message(chat_id=user_id, text=rejection_message)
    await query.edit_message_text(text=f"Заявка от пользователя {user_id} отклонена.")


def main_user_bot():
    application = ApplicationBuilder().token(TOKEN_USER).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    application.add_handler(CallbackQueryHandler(button_handler))  # Обработчик для кнопок

    application.run_polling()
    logger.info("Бот запущен и работает.")


if __name__ == '__main__':
    main_user_bot()
