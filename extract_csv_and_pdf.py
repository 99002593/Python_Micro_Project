import re
import os
import textract
import pandas as pd
################################################################################################take all resume (pdf) from folder

files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.pdf')]


################################################################################################From csv file extract all gmails
col_list = ["Email"]
df = pd.read_csv("data.csv", usecols=col_list)
all_mail_csv=list(df["Email"])
print("all_mail_csv:",all_mail_csv)############################################################store all the emails from csv in a list
###############################################################################################Sending automated mails 
sender="pythonprojsns@gmail.com"
password="veertanu"
message="""Dear Candidate,
 
			Greetings from PQB,
 
			We are glad to inform that you are selected for the online interview process. Kindly respond to this with your CV's within the next 24 hours.
 
			Regards
			Dr.F.Torres"""
for dest in all_mail_csv:
	try:
	   conn=smtplib.SMTP('smtp.gmail.com',587)
	   conn.starttls()
	   conn.ehlo()
	   conn.login(sender,password)
	   conn.ehlo()
	   conn.sendmail(sender, dest, message)         
	   print("Successfully sent email")
	except smtplib.SMTPException:
	   print("Error: unable to send email")
	finally:
		conn.quit()
