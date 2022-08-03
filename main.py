import smtplib
import requests
import time

lat = 42.310879  ### Put in your latitude and longtitude
long = -71.125061

while True:
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()["iss_position"]

    if -5 < float(data['latitude']) - lat < 5 and -5 < float(data['longitude']) - long < 5:
        my_email = "" ### Enter email address here
        password = '' ### ENTER PASSWORD HERE
        message = f"Subject:ISS Notification\nThe ISS is right overhead! The current location of the ISS is {data['latitude']}, {data['longitude']}."

        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='seanw.connolly1@gmail.com',
            msg=message)
        connection.close()

        ### A timer is set so that the message is only sent once each time it flies by.
        time.sleep(200)