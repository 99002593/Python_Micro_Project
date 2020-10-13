
import re
import os
import textract
import pandas as pd
################################################################################################take all resume (pdf) from folder

files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.pdf')]

###############################################################################################extract gmail from resume

all_mail=[]
for i in files:
	text = textract.process(i)
	res=str(text)
	result=re.findall('[\w+][\w+\.]+@[\w+][\w+\.]+[a-z A-Z 0-9]',res)                       #regular expression for extracting gmail
	all_mail.extend(result)
#print(result)
print("all_mail:",all_mail)     								   #store all the emails in a list

################################################################################################From csv file extract all gmails
col_list = ["Email"]
df = pd.read_csv("data.csv", usecols=col_list)
all_mail_csv=list(df["Email"])
print("all_mail_csv:",all_mail_csv)############################################################store all the emails from csv in a list

