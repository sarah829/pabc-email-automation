# pabc-email-automation

---

### Purpose
<b>Rank Emails:</b> Automates email sending for members who achieve new ranks each month. This program sends an email to ALL
people who achieve a new rank. If there are not emails for ALL ranks, the program will crash. 

---

### Configuration
<b>1. Setting up your email</b> <br>
To use the program, create an **app password** to go with your email to allow sending emails relatively securely. The app password will be a series of random letters.
<br>
[Instructions for gmail](https://support.google.com/accounts/answer/185833?hl=en), [instructions for Microsoft](https://support.microsoft.com/en-us/account-billing/using-app-passwords-with-apps-that-don-t-support-two-step-verification-5896ed9b-4263-e681-128a-a6f2979a7944)

<b>2. Create a file entitled `.env`</b>
<br>
This file will contain your email and password, which will not appear in the program itself.
<br>The contents of this file should be:

```
email-address = "youremail@domain.com"
email-password = "app password"
```
<b>3. Edit the file `configs.txt`</b>
<br>
`sender` is the name that you would like at the end of the email.<br>
`subject` is the subject of the email. See the section below on inserting specific member information.<br>
`website` is the url that will be displayed at the bottom of the email. <br>
`email_texts_path` is the folder that contains the text for all the emails. 
This should not need to be changed unless you have rearranged the files. <br>
`csv_file_path` is the file path to the data file. This will usually just be the name of the file.

<b>4. Set the text for the emails.</b>
<br>
Body text for the emails is in the folder `ranks_email_texts`. Texts must be named `First-Word-of-Rank.txt`. For example,
`Silver.txt`, `NABC.txt`, and `Life.txt` are correctly named files.

Adjust the style of the email in `template.html` by updating the inline CSS stylesheet.

`body.html` contains the shell of the email with the text that is in all emails regardless of rank. 
This includes the greeting and the closing of the email. 

See the last section on inserting specific member information in text. 

---

### Running the Program

To use, just run the script `rank_email_driver.py`. (Call `python3 rank_email_driver.py` or `python rank_email_driver.py` depending on your Python settings from the command line.)

For testing, use `rank_email_testing_driver.py`. 
In this file, set `YOUR_EMAIL` to your email. 
Testing runs the program as normal except all email addresses are replaced with whatever email you entered,
meaning that all emails are sent to yourself instead of actual recipients. 

---

### Requirements

This program runs on Python 3, so `python3` must be installed. In addition, `python-dotenv` must be installed. 
To install `python-dotenv`, run `pip install python-dotenv` (install `pip` if necessary). 

---

### Formatting Email Text
To reference specific information about a member, use: <br>
`{member.title}`, `{member.first_name}`, `{member.last_name}`, `{member.new_rank}`, and `{member.email}` in place of the
corresponding field.

Use `{configs.sender_name}`, `{configs.subject}`, and `{configs.website}` for the corresponding fields.