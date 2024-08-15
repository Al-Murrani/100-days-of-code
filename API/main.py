import smtplib
import time

import requests
from datetime import datetime

MY_LAT = 51.507
MY_LANG = -0.1277


def is_iss_overhead():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()

    data = response_iss.json()
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]
    iss_position = (longitude, latitude)
    print(iss_position)

    if MY_LANG - 5 <= longitude <= MY_LANG + 5 and MY_LAT - 5 <= latitude >= MY_LAT - 5:
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LANG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data_sr_ss = response.json()
    # To get the hour
    sunrise = int(data_sr_ss["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_sr_ss["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_dark():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look up"
        )

# I recommend python-dotenv module
# .env
# MY_EMAIL=example@mail.com
# PASSWORD=MySecurePassword1234
# SMTP=smtp.mymail.com
# PORT=999
# TARGET_EMAIL=target@mail.com
