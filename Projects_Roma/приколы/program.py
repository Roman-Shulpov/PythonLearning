from gtts import gTTS
from twilio.rest import Client
import os


# Функция для преобразования текста в MP3
def text_to_mp3(text, filename):
    tts = gTTS(text=text, lang='ru')
    tts.save(filename)


# Функция для отправки SMS
def send_sms(to, body):
    # Укажите свои учетные данные Twilio
    account_sid = 'ВАШ_ACCOUNT_SID'
    auth_token = 'ВАШ_AUTH_TOKEN'
    from_number = 'ВАШ_TWILIO_НОМЕР'

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=body,
        from_=from_number,
        to=to
    )
    return message.sid


# Основная программа
if __name__ == "__main__":
    # Ввод текста от пользователя
    text = input("Введите текст для преобразования в MP3 и отправки SMS: ")

    # Преобразование текста в MP3
    mp3_filename = "output.mp3"
    text_to_mp3(text, mp3_filename)
    print(f"Текст преобразован в {mp3_filename}")

    # Отправка SMS
    recipient_number = input("Введите номер получателя (в формате +1234567890): ")
    sms_sid = send_sms(recipient_number, text)
    print(f"SMS отправлено с SID: {sms_sid}")

    # Удаление MP3 файла (по желанию)
    os.remove(mp3_filename)