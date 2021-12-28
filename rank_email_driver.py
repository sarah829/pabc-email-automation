"""
File name: rank_email_driver.py
@author: Sarah Youngquist
Purpose: Calls the email sender function.
Revision history:
Date         Editor          Action
2021-12-03   SY              Initial creation
2021-12-27   SY              Rank specification added, printed output added
"""

import rank_emails

if __name__ == "__main__":
    rankings = ["Club", "Sectional", "Regional", "NABC"]
    failed = rank_emails.send_all_rank_emails("configs.txt", rankings)
    print("Finished sending emails.", failed, "messages failed to send.")
