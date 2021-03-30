import smtplib
import os

user_name = os.environ.get('sys_user')
pass_word = os.environ.get('sys_pass')

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('user_name','pass_word')




