import csv
from receiver import classifier
genre=['adhunik','bhajan','bhojpuri','classical','dohari','gazal','newa','pop','rock','selo']
filename='x.csv'
with open(filename,'r', newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    count=1
    for row in csvreader:
        if count<=1*5:
            send=(genre[0])
        elif count<=2*5:
            send=(genre[1])
        elif count<=3*5:
            send=(genre[2])
        elif count<=4*5:
            send=(genre[3])
        elif count<=5*5:
            send=(genre[4])
        elif count<=6*5:
            send=(genre[5])
        elif count<=7*5:
            send=(genre[6])
        elif count<=8*5:
            send=(genre[7])
        elif count<=9*5:
            send=(genre[8])
        elif count<=10*5:
            send=(genre[9])
        count=count+1
        receive=classifier(row)
        rows=[send,receive]
        with open('result.csv','a',newline='') as file:
            csvwriter=csv.writer(file)
            csvwriter.writerow(rows)
        file.close()
