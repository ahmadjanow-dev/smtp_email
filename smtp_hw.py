from dotenv import load_dotenv
from email.message import EmailMessage
import smtplib
import os, random

load_dotenv() 

def email_confirmation(to_email: str, nums: int) -> bool:
    sender = os.environ.get('smtp_email')
    password = os.environ.get('smtp_password')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)

        msg = EmailMessage()
        msg['Subject'] = 'Код для подтверждения аккаунта'
        msg['From'] = sender
        msg['To'] = to_email
        msg.set_content(str(nums))  

        server.send_message(msg)
        return True  

    except Exception as error:
        return False  
def main():
    attempts = 3
    while attempts > 0:  
        to_email = input('Введите вашу электронную почту: ')
        confirmation = int(input(f"Введите 6-значный код, который отправлен на почту {to_email}: "))

        nums = random.randint(100000, 999999)

        if email_confirmation(to_email, nums):
            if confirmation == nums:
                print("Поздравляю, вы успешно подтвердили аккаунт.")
                break
            else:
                print(f"Цифры не совпадают. У вас осталось {attempts - 1} попыток.")
        else:
            print("Ошибка при отправке сообщения. Попробуйте еще раз.")

        attempts -= 1

if __name__ == "__main__":
    load_dotenv()  
    main()
