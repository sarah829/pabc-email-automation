"""
File name: rank_emails.py
@author: Sarah Youngquist
Purpose: Send emails to PABC players who achieved new ranks.
Contains functions to read member data and send emails to members who
achieved new ranks.

Revision history:
Date         Editor          Action
2021-12-03   SY              Initial creation, fully functional
2021-12-27   SY              Merged 2 files (rank_emails.py and ranks_process_data.py)
"""
from email.message import EmailMessage
import csv

from helper_python_code import member_class, send_emails

"""
def make_members(csv_file_address):
    ""
    This takes a file with member data and creates a list of Member objects. 
    :param csv_file_address: address from home directory for csv w/ member info
    ""
    members = []
    with open(csv_file_address, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            if line["Transaction Type"].split()[-1] == "Master":
                rank = " ".join(line["Transaction Type"].split()[1:])
                member = Member(line["Title"], line["First Name"], line["Last Name"], rank, line["Email Address"])
                members.append(member)
    return members
"""


# Same as above except all email fields are replaced with test_email
def make_members_testing(csv_file_address, test_email):
    """
    This makes a list of Member objects with all emails replaced with test_email
    :param csv_file_address: address from home directory for csv w/ member info
    :param test_email: email address to send messages to instead of the actual
    """
    members = []
    with open(csv_file_address, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            if line["Transaction Type"].split()[-1] == "Master":
                rank = " ".join(line["Transaction Type"].split()[1:])
                member = member_class.Member(line["Title"], line["First Name"], line["Last Name"], rank, test_email)
                members.append(member)
    return members


def get_rank_email(configs, member, template, template_body):
    """
    Gets the email for a certain rank, creates an email using the given configs
    and member.
    Returns an EmailMessage object. If the rank is invalid, none is returned
    :param configs: An EmailConfigs object
    :param member: A Member object, will be the recipient
    :param template: text of the html code for the general structure/style of the email
    :param template_body: Text of the html code for the format of the body of the email
    """
    # get the text for the message with the correct rank
    # file name is the first word of the rank
    file_name = configs.email_texts_path + "/" + member.new_rank.split()[0] + ".txt"
    try:
        with open(file_name, 'r') as f:
            message_text = f.read()
    except IOError:
        return None  # rank was invalid, no message
    message_text = message_text.format(**locals())  # inserts member-specific info
    # build email
    msg = EmailMessage()
    msg['Subject'] = configs.subject.format(**locals())
    msg['From'] = send_emails.EMAIL_ADDRESS
    msg['To'] = member.email
    body = template_body.format(**locals())
    msg.set_content(template.replace("---template_body---", body), subtype='html')
    return msg


"""
def send_all_rank_emails(configs_file):
    ""Reads member data and configurations and sends all emails. This is the
    driver function in the program.
    Returns the number of emails that failed to send
    :param configs_file: name of configs file
    :param ranks: Specifies which ranks emails are to be sent to. This should
      be a **list** of strings unless the word "all".
    ""
    configs = send_emails.retrieve_configs(configs_file)
    members = make_members(configs.csv_file)
    with open("template.html", 'r') as template_file:
        template = template_file.read()
    with open("body.html", 'r') as template_body_file:
        template_body = template_body_file.read()
        # send emails
    failures = 0
    for m in members:
        if ranks == "all" or m.new_rank.split()[0] in ranks:
            email = get_rank_email(configs, m, template, template_body)
            if email is None:
                print("Failed to send an email to", m.first_name, m.last_name, "- Rank of", m.new_rank, "was invalid.")
                failures = failures + 1
            else:
                send_emails.send_email(email)
    return failures
"""


def send_all_rank_emails_testing(configs_file, ranks="all", test_email="email@gmail.com"):
    """
    Reads member data and configurations and sends all emails. This is the
    driver function in the program.
    This version sends emails to a different email address, not actually blasting
    out emails to the members.
    Returns the number of emails that failed to send
    :param configs_file: name of configs file
    :param ranks: Specifies which ranks emails are to be sent to. This should
      be a **list** of strings unless the word "all".
    :param test_email: recipient email address used for testing
    """
    configs = send_emails.retrieve_configs(configs_file)
    members = make_members_testing(configs.csv_file, test_email)  # get a list of members
    # read in the templates for emails
    with open(configs.email_texts_path + "/template.html", 'r') as template_file:
        template = template_file.read()
    with open(configs.email_texts_path + "/body.html", 'r') as template_body_file:
        template_body = template_body_file.read()
    # send emails
    failures = 0
    for m in members:
        if ranks == "all" or m.new_rank.split()[0] in ranks:
            email = get_rank_email(configs, m, template, template_body)
            if email is None:
                print("Failed to send an email to", m.first_name, m.last_name, "- Rank of", m.new_rank, "was invalid.")
                failures = failures + 1
            else:
                send_emails.send_email(email)
    return failures


# main, equivalent to running rank_email_driver or rank_email_testing_driver
# depending on if testing is True or False
if __name__ == "__main__":
    testing = True
    your_email = "sarah.blue47@gmail.com"

    rankings = ["Club", "Sectional", "Regional", "NABC"]
    if testing:
        failed = send_all_rank_emails_testing("configs.txt", rankings, your_email)
    else:
        pass  # failed = send_all_rank_emails("configs.txt", rankings)
    print("Finished sending emails.", failed, "message(s) failed to send.")
