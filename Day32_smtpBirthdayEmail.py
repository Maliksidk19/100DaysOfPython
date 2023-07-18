import smtplib
from random import randint
import datetime as dt
import pandas as pd

data = pd.read_csv('Files/birthdays.csv')
data_list = data.to_dict(orient="records")


def send_mail(receiver, message):
    connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
    connection.starttls()

    email = 'kabirkapoor265@gmail.com'
    password = 'yyibhmubfytctpcz'

    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs=receiver, msg=f'Subject:Happy Birthday!!\n\n{message}')
    connection.close()


now = dt.datetime.now()
for data in data_list:
    if now.date().day == data['day'] and now.date().month == data['month']:
        with open(f'Files/letter_templates/letter_{randint(1,3)}.txt') as f:
            letter = f.read().replace('[NAME]', data['name'])
            send_mail(receiver=data['email'], message=letter)
