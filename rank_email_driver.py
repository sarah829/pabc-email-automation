"""
File name: rank_email_testing_driver.py
@author: Sarah Youngquist
Purpose: Calls the email sender function.
Revision history:
Date         Editor          Action
2021-12-03   SY              Initial creation
"""

from ranks_emails import rank_emails

if __name__ == "__main__":
    rank_emails.send_all_rank_emails("configs.txt")
