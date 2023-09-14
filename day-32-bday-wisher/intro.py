import smtplib
from datetime import datetime
import random

username = 'notme@redpoll.it'
password = 'kecreW-quvcu0-nybqiz'
today = datetime.now().weekday()

if today == 3:
    with open('quotes.txt','r') as qfile:
        quotes = qfile.readlines()

    todaysquote = random.choice(quotes)


    with smtplib.SMTP("ssl0.ovh.net", 587) as connection:
        connection.starttls()
        connection.login(username, password)
        connection.sendmail(username,
                            'contact@redpoll.it',
                            f"Subject:Don't give up, we must prevail!\n\n{todaysquote}")
        connection.close()
