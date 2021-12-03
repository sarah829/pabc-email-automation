"""
File name: rank_emails.py
@author: Sarah Youngquist
Purpose: Contains functions to create a rank email for a given member given configurations. Contains the function to
send all the emails, which reads the member data from the csv file and sends all emails

Revision history:
Date         Editor          Action
2021-12-03   SY              Initial creation, fully functional
"""

import send_emails
import ranks_process_data
from email.message import EmailMessage


# Gets an email given configurations, a member, the template (containing the inline css), and the template for the
# body of the message. Returns an EmailMessage
def get_rank_email(configs, member, template, template_body):
    message_text = configs.get_rank_message_text(member.new_rank.split()[0]).format(**locals())
    msg = EmailMessage()
    msg['Subject'] = configs.subject.format(**locals())
    msg['From'] = send_emails.EMAIL_ADDRESS
    msg['To'] = member.email
    body = template_body.format(**locals())
    msg.set_content(template.replace("---template_body---", body), subtype='html')
    return msg


# Reads member data and sends all emails. This is the main function in the program.
"""
def send_all_rank_emails(configs_file):
    configs = send_emails.retrieve_configs(configs_file)
    members = process_data.make_members(configs.csv_file)
    with open(configs.email_texts_path + "/template.html", 'r') as template_file:
        template = template_file.read()
    with open(configs.email_texts_path + "/body.html", 'r') as template_body_file:
        template_body = template_body_file.read()
    for m in members:
        email = get_rank_email(configs, m, template, template_body)
        send_emails.send_email(email)
"""


# Same as above except all emails are sent to the given test_email.
def send_all_rank_emails_testing(configs_file, test_email):
    configs = send_emails.retrieve_configs(configs_file)
    members = ranks_process_data.make_members_testing(configs.csv_file, test_email)
    with open(configs.email_texts_path + "/template.html", 'r') as template_file:
        template = template_file.read()
    with open(configs.email_texts_path + "/body.html", 'r') as template_body_file:
        template_body = template_body_file.read()
    for m in members:
        email = get_rank_email(configs, m, template, template_body)
        send_emails.send_email(email)
