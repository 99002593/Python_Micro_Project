#import extract_csv_and_pdf
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
'''		
a = Resume();
print(a.resumegmail());
b = CSV();
print(b.emailscsv());
'''		
################################################################################################Making a call for Interview
'''
a = Resume();
b = CSV();
interested=b.emailscsv();

sender="pythonprojsns@gmail.com"
password="veertanu"
message="""Dear Candidate,
 
			Greetings from PQB,
 
			We are delighted that you have showed us your interest in the company. We would like to schedule an interview with you from any time between 3pm to 5pm on Sunday. The link for teams will be shared with you soon. 
 
			Regards,
			Dr.F.Torres"""
for dest in interested:
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
'''
