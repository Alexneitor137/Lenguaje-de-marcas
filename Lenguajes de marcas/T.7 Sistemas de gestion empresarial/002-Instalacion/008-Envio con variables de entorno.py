import smtplib
from email.message import EmailMessage
import os

SMTP_SERVER = os.environ.get("EMAIL_SERVIDOR")
SMTP_PORT = 465
SMTP_USER = os.environ.get("EMAIL_USUARIO")
SMTP_PASS = os.environ.get("EMAIL_CONTRASENA")

print("DEBUG:", SMTP_SERVER, SMTP_PORT, SMTP_USER)

msg = EmailMessage()
msg["From"] = SMTP_USER
msg["To"] = "Alexcalderonsanchez@gmail.com"
msg["Subject"] = "Esto es un ejercicio de clase"
msg.set_content("Hola esto es una prueba desde Python.\n")

with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, timeout=10) as smtp:
    smtp.ehlo()
    smtp.login(SMTP_USER, SMTP_PASS)
    smtp.send_message(msg)

print("Email sent")


