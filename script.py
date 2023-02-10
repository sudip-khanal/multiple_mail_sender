from SMTPEmail import smtplib as m

obj = m.SMTP('smtp.gmail.com',587)
obj.ehlo()
obj.starttls()
obj.login('','') # enter the mail id and passwod from which mail will be
subject= 'test'
body = 'testing code'
message ="subject:{}\n\n{}".format(subject,body)
list_of_mailId=['',''] # this is list of receving Email adress 
obj.sendmail('',list_of_mailId,message)#sending mail address
print("mail send succeesfully")
obj.quit()

