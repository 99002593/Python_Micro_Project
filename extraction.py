
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
class test:

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
class test2(test):

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

