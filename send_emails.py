"""
File name: send_emails.py
@author: Sarah Youngquist
Purpose: General email related functionalities. Defines class EmailConfigs to get general info for all emails sent and
contains methods to get configurations from a file and to send a given email.

Revision history:
Date         Editor          Action
2021-12-03   SY              Initial creation, fully functional
"""

from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

EMAIL_ADDRESS = os.environ.get("email-address")
EMAIL_PASSWORD = os.environ.get("email-password")
TEXTS_PATH = "ranks_email_texts"


# general information about the sender, to be used for all emails created with this config
class EmailConfigs:
    def __init__(self, sender_name="", subject="", website="", csv_file="", email_texts_path="ranks_email_texts"):
        self.sender_name = sender_name
        self.subject = subject
        self.website = website
        self.csv_file = csv_file
        self.email_texts_path = email_texts_path

    # retrieves the text for a rank message given the file name (which is FirstWordOfRank)
    def get_rank_message_text(self, rank_name):
        file_name = self.email_texts_path + "/" + rank_name + ".txt"
        with open(file_name, 'r') as msg:
            return msg.read()


# sends any email
def send_email(msg):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


# retrieves configs from a given text file. File should be formatted as configs.txt is.
def retrieve_configs(configs_file_address):
    with open(configs_file_address, 'r') as configs_file:
        params = []
        for i in range(4):
            params.append(" ".join(configs_file.readline().split()[1:]))
        return EmailConfigs(*params, TEXTS_PATH)