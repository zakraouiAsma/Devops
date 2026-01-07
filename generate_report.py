import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Configurer vos informations
sender_email = "zakraouiasma2019@gmail.com"
receiver_email = "zakraouiasma2019@gmail.com"
password = "helloworld"  # Utiliser un mot de passe spécifique pour l'application si Gmail

# Créer le message
msg = MIMEMultipart()
msg['From zakraouiasma2019@gmail.com'] = sender_email
msg['To zakraouiasma2019@gmail.com'] = receiver_email
msg['Subject'] = "Rapport Pytest Automatique"

# Corps du mail
body = "Bonjour,\n\nVeuillez trouver ci-joint le rapport pytest.\n\nCordialement."
msg.attach(MIMEText(body, 'plain'))

# Attacher le fichier
filename = "report.html"
with open(filename, "rb") as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header(
    'Content-Disposition',
    f'attachment; filename= {filename}',
)
msg.attach(part)

# Envoyer l'email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(msg)
    server.quit()
    print("Email envoyé avec succès !")
except Exception as e:
    print(f"Erreur: {e}")
