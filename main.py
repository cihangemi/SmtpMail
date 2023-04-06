import smtplib

content="Hi! Hi!"

mail =smtplib.SMTP("smtp.gmail.com",587)

mail.ehlo()

mail.starttls()

mail.login("example@example.com","password")
#Email girişi kendi hesabınızla

mail.sendmail("1@gmail.com","2@example.com",content)
#1 Gönderici mail
#2 Alıcı mail
#içerik-mesaj