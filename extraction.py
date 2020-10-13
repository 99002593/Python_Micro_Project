import extract_csv_and_pdf
import re
import os
import csv
import smtplib
import textract
import pandas as pd

################################################################################################take all resume (pdf) from folder

files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.pdf')];

###############################################################################################extract gmail from resume
global all_mail;
global finalcall;
all_mail=[];
finalcall=[];

class Resume:

	def resumegmail(self):
		for i in files:
			text = textract.process(i);
			res =	str(text);
			result = re.findall('[\w+][\w+\.]+@[\w+][\w+\.]+[a-z A-Z 0-9]',res);                      	#regular expression for extracting gmail
			all_mail.extend(result);
		return all_mail;
	#print(result)
	#print("all_mail:",all_mail)     								   																					#store all the emails in a list
################################################################################################From csv file extract all gmails
class CSV(Resume):

	def emailscsv(self):	
		with open('data.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',');
			line_count = 0;
			for row in csv_reader:
				if line_count == 0:
					line_count += 1;
				else:
					for i in range(0,len(all_mail)):
						if all_mail[i]==row[3]:
							#print(all_mail[i])
							finalcall.append(all_mail[i]);
					line_count += 1;
		return finalcall;
			
a = Resume();
print(a.resumegmail());
b = CSV();
list1=b.emailscsv();
print(type(list1))
print(list1)
	
################################################################################################Making a call for Interview

'''a = Resume();
b = CSV();
interested=b.emailscsv();
'''
sender1="pythonprojsns@gmail.com"
password1="veertanu"
message1="""Dear Candidate,
 
			Greetings from PQB,
 
			We are delighted that you have showed us your interest in the company. We would like to schedule an interview with you from any time between 3pm to 5pm on Sunday. The link for teams will be shared with you soon. 
 
			Regards,
			Dr.F.Torres"""
for des in list1:
	try:
	   conn1=smtplib.SMTP('smtp.gmail.com',587)
	   conn1.starttls()
	   conn1.ehlo()
	   conn1.login(sender1,password1)
	   conn1.ehlo()
	   conn1.sendmail(sender1, des, message1)         
	   print("Successfully sent email")
	except smtplib.SMTPException:
	   print("Error: unable to send email")
	finally:
		conn1.quit()		
