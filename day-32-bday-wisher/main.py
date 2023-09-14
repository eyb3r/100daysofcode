# #################### Hard Starting Project ######################
from datetime import datetime
import smtplib
import pandas
import random

now = datetime.now()
day, month = now.day, now.month
username = 'dummy'
password = 'dummy'


def pick_a_letter():
    num = random.randint(1, 3)
    with open(f"letter_templates/letter_{num}.txt", 'r') as letter:
        result = letter.readlines()
    return result


data = pandas.read_csv('birthdays.csv')
with smtplib.SMTP('ssl0.ovh.net', 587) as connection:
    connection.starttls()
    connection.login(username, password)

    bday_dates = {(dr.day, dr.month): [dr.nickname, dr.email] for (index, dr) in data.iterrows()}
    print(bday_dates)
    for key, row in bday_dates.items():
        if key == (day, month):
            template = pick_a_letter()
            template = '\n'.join(template)
            template = template.replace('[NAME]', str(row[0]))
            connection.sendmail(from_addr=username,
                                to_addrs=row[1],
                                msg=f"Subject:Happy B-Day!\n\n{template}")
