import datetime as dt
import smtplib
from random import choice
from credentials import credentials


def motivation():
    weekday = dt.datetime.now().weekday()
    my_email = credentials["email"]
    my_password = credentials["password"]

    if weekday == 0:
        with open("quotes.txt", "r") as file:
            content = file.readlines()
            quote_of_the_day = choice(content)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="ponjae11@gmail.com", msg=f"Subject:Monday Motivation\n\n{quote_of_the_day}")
            connection.sendmail(from_addr=my_email,
                                to_addrs="johan.jaensson@electra.se", msg=f"Subject:Monday Motivation\n\n{quote_of_the_day}")
