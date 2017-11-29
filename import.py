import csv
from register.models import userinfo

with open('exceldata2.csv','rb') as csvfile:
	with open('error.csv','wb') as csvfile1:
		spamwriter = csv.writer(csvfile1)
		details=csv.reader(csvfile)
		for row in details:
			Exid =''
			Exid+=row[2]
			if row[3]=="CS":
				Exid+='1'
			elif row[3]=="EC":
				Exid+='2'
			elif row[3]=="EE":
				Exid+='3'
			elif row[3]=="EB":
				Exid+='4'
			if row[4]=="A":
				Exid+='1'
			else:
				Exid+='2'
			if(int(row[5])<10):
				Exid+='0'
				Exid+=row[5]
			else:
				Exid+=row[5]
			print(row[1]+":"+Exid)
			if userinfo.objects.filter(excelid=Exid).exists() or userinfo.objects.filter(email=row[7]).exists():
				spamwriter.writerow(row)
			else:
				userinfo.objects.get_or_create(excelid=Exid,name=row[1],college="Model Engineering College",email=row[7],phone=row[6],present=True,stay=False)
		
