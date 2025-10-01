import os 
from dotenv import load_dotenv
from aiosmtplib import SMTP
from email.message import EmailMessage

load_dotenv()

async def send_email(to_email: str, subject: str, body: str) -> bool:
    message = EmailMessage()
    message["From"] = os.getenv("SMTP_USERNAME")
    message["To"] = to_email
    message["Subject"] = subject
    message.set_content(body)


    try:
        smtp = SMTP(hostname=os.getenv("SMTP_HOST"), port=int(os.getenv("SMTP_HOST")),start_tls=True)
        await smtp.connect()
        await smtp.login(os.getenv("SMTP_USERNAME"), os.getenv("SMTP_PASSWORD"))
        await smtp.send_message(message)
        await smtp.quit()
        return True
    except Exception as e:
        print(f"🚨 Error al enviar correo: {e}")  # <-- esto lo veremos en la consola
    return False
