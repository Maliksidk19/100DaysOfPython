import requests
from datetime import datetime
import time
import smtplib
from dotenv import dotenv_values

data = dotenv_values("Files/.env")

email = data['email']
password = data['password']
my_lat = 33.784309
my_long = 72.738777


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    if my_lat - 5 <= iss_latitude <= my_lat + 5 and my_long - 5 <= iss_longitude <= my_long + 5:
        return True


def is_night():
    params = {
        "lat": my_lat,
        "lng": my_long,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP(host='smtp.gmail.com')
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=email,
                            msg="Subject:Look Up\n\nThe ISS is above you in the sky.")
