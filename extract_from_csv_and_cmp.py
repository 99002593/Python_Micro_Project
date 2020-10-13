import csv
comp=['rahulrathod95982@gmail.com', 'maneeshdani@gmail.com', 'pg199gowda@gmail.com', 'lakshmishagowda99@gmail.com', 'kulkarniadi555@gmail.com', 'gagan15nan@gmail.com', 'pavanbunny65@gmail.com', 'lokanath.reddy.c1999@gmail.com', 'shekarjk.mec@gmail.com']
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            for i in range(0,len(comp)):
            	if comp[i]==row[3]:
            		print(comp[i])
            line_count += 1
            
