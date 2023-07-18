import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
from dotenv import load_dotenv

load_dotenv() 

def enviar_email(destinatario, asunto, cuerpo, archivo_adjunto):
    remitente = os.getenv("EMAIL_USER") 
    contraseña = os.getenv("EMAIL_CONTRASENIA")  

    # Crear el objeto de correo electrónico
    mensaje = MIMEMultipart()
    mensaje["From"] = remitente
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto

    # Agregar el cuerpo del mensaje
    mensaje.attach(MIMEText(cuerpo, "plain"))

    # Adjuntar el archivo PDF al correo electrónico
    parte_adjunta = MIMEBase("application", "octet-stream")
    parte_adjunta.set_payload(open(archivo_adjunto, "rb").read())
    encoders.encode_base64(parte_adjunta)
    parte_adjunta.add_header("Content-Disposition", "attachment; filename= " + archivo_adjunto)
    mensaje.attach(parte_adjunta)

    # Configurar el servidor SMTP y enviar el correo electrónico
    servidor_smtp = smtplib.SMTP("smtp.gmail.com", 587)
    servidor_smtp.starttls()
    servidor_smtp.login(remitente, contraseña)
    servidor_smtp.sendmail(remitente, destinatario, mensaje.as_string())
    servidor_smtp.quit()
