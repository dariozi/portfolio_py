import smtplib, ssl

host = "smtp.gmail.com"
port = 465
username = "intrinsiq.test.iq@gmail.com"

password= "qour youf pftt cfjz"

receiver= "dariozignale@gmail.com"
context = ssl.create_default_context()

message = """\
subject: this is a test
test test"""
with smtplib.SMTP_SSL(host,port,context=context) as server:
    server.login(username,password)
    server.sendmail(username,receiver, message)