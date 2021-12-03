"""
File name: member_data.py
@author: Sarah Youngquist
Purpose: Contains the class definition of Member, which stores the title, first and last name, new rank achieved, and
  email of a player
Revision history:
Date         Editor          Action
2021-12-03   SY              Initial creation
"""


class Member:
    def __init__(self, title=" ", first_name="", last_name="", new_rank="", email=""):
        self.title = title
        if title != " ":
            self.title = title + ". "
        self.first_name = first_name
        self.last_name = last_name
        self.new_rank = new_rank
        self.email = email

    def __str__(self):
        return "Member: title = " + self.title + ", first_name = " + self.first_name + ", last_name = " + self.last_name + ", new_name = " + self.new_rank + ", email = " + self.email