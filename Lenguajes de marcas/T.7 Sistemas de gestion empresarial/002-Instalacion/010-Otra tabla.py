import smtplib
from email.message import EmailMessage
import os

SMTP_SERVER = "smtp.resend.com"
SMTP_PORT = 465

SMTP_USER = "resend"
SMTP_PASS = os.environ.get("RESEND_API_KEY")

if not SMTP_PASS:
    raise ValueError("RESEND_API_KEY no está definida")

msg = EmailMessage()
msg["From"] = "onboarding@resend.dev"
msg["To"] = "andresruiztorres782@gmail.com"
msg["Subject"] = "Esto es un ejercicio de clase"
msg.set_content("Hola, prueba SMTP con Resend.")

with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.login(SMTP_USER, SMTP_PASS)
    smtp.send_message(msg)

print("Email sent")