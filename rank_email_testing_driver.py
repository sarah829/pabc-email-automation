"""
File name: rank_email_testing_driver.py
@author: Sarah Youngquist
Purpose: Calls the testing email sender function. Change the email in the doc to the email to be used for testing.
Runs the normal program with real data except all emails are sent to given email.
Revision history:
Date         Editor          Action
2021-12-03   SY              Initial creation
"""

from ranks_emails import rank_emails

YOUR_EMAIL = "youremail@domain.com"


if __name__ == "__main__":
    rank_emails.send_all_rank_emails_testing("configs.txt", YOUR_EMAIL)
