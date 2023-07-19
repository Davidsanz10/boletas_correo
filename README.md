# boletas Correo
Este proyecto es para unir boletas que se mandan en txt y exportarlo como pdf
Lo primero que se necesita es tener los permisos necesarios en el correo para poder hacer envío a través del código python.
1. En entramos a la configuración del correo ![image](https://github.com/Davidsanz10/boletas_correo/assets/54865176/cf6a6bce-3555-4355-9ec2-39006b2b4398)
2. Activamos verificación de 2 pasos: ![image](https://github.com/Davidsanz10/boletas_correo/assets/54865176/6e2746f0-6469-483a-bd02-8fa7e86c0e60)
3. hacemos click en contraseña de aplicación generada (que reemplazaría a la contraseña del correo electronico en el código) ![image](https://github.com/Davidsanz10/boletas_correo/assets/54865176/de8167be-995d-4a14-8b9d-6185d460b3cb)

Una vez se tengamos todo configurado, clonamos el proyecto

Debemos crear el archivo .env y añadir el valor del correo y contraseña que va a mandar el correo automatico:
- EMAIL_CONTRASENIA
- EMAIL_USER
  
Luego Hacemos la importación de las librerías que va a necesitar el proyecto:
- pip install smtplib
- pip install MIMEMultipart
- pip install MIMEBase
- pip install MIMEText
- pip install encoders
- pip install os
- pip install dotenv
- pip install FPDF
- pip install glob

Luego cambiamos el correo destinatario en "boletas_correo.py" y ahí mismo damos  en ejecutar.
