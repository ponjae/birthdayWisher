import pandas
import smtplib
import os
import datetime as dt
from credentials import credentials
from random import choice
from motivation import motivation


birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_data.to_dict(orient="records")
my_email = credentials["email"]
my_password = credentials["password"]

now = dt.datetime.now()
current_month = now.month
current_day = now.day

for birthday in birthday_dict:
    if birthday["month"] == current_month and birthday["day"] == current_day:
        random_letter = choice(os.listdir("letter_templates"))
        with open(f"letter_templates/{random_letter}", "r") as letter:
            lines = letter.read()
            updated_lines = lines.replace(
                "[NAME]", birthday["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday["email"], msg=f"Subject:HAPPY BIRTHDAY!!!\n\n{updated_lines}")

motivation()
