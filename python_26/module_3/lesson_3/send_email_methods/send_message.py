import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "absaitovdev@gmail.com"
receiver_email = "absaitovdev@gmail.com"
password = "zigntrldavncsspa"
message = """Hello Polatdjorayev"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)