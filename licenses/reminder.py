import models
import smtplib

smtp_server = "smtp.gmail.com"
mail_from = "fromesomeemail@gmail.com"
mail_to = "someemail@gmail.com"
now = models.datetime.date.today()
licenses = []

def send_email(host, subject, to_addr, from_addr, body_text):
    BODY = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % to_addr,
        "Subject: %s" % subject ,
        "",
        body_text
    ))
    server = smtplib.SMTP(host)
    server.sendmail(from_addr, [to_addr], BODY)
    server.quit()

def get_renew_list():
    for row in models.XLicenses.select():
        if row.end_date:
            end = row.end_date
            delta = end - now
            if delta.days == 30:
                licenses.append(row.software_name)
                print("Please renew license\n" + "Software_name=" + row.software_name + "\nRenew date=" + row.end_date.strftime("%d.%m.%Y") + "\nUser=" + row.user)
    return(set(licenses))

if __name__ == '__main__':
    licenses = list(get_renew_list())
    for i in licenses:
        subject = i + "renew needed"
        body = "Please request license renewal for " + i
        send_email(smtp_server, subject, mail_to, mail_from, body)
