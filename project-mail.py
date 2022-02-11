import smtplib
try:
    sender_email = input("Enter your email address :")
    sender_password = input("enter your password :")
    receiver_email = input("enter the email to send :")

    subject = input("Enter the subject :")
    body = input("Enter the message of your mail")
    message = """\
    Subject:
    {}
    {}""".format(subject, body)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, receiver_email, message)
        print("Email Sent Successfully")
except:
    print("Invalid UserId or Password")
