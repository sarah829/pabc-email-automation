"""
File name: ranks_process_data.py
@author: Sarah Youngquist
Purpose: Contains the functions that read from the csv file and creates a list of member objects of only the members
who have achieved a new rank.
Revision history:
Date         Editor          Action
2021-12-03   SY              Initial creation, fully functional
"""

import csv

# Reads the csv file at the given address and makes a list of member objects of the members who achieved a new rank.
"""
def make_members(csv_file_address):
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
    members = []
    with open(csv_file_address, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            if line["Transaction Type"].split()[-1] == "Master":
                rank = " ".join(line["Transaction Type"].split()[1:])
                member = member.Member(line["Title"], line["First Name"], line["Last Name"], rank, test_email)
                members.append(member)
    return members
