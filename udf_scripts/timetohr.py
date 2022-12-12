import fileinput

for line in fileinput.input():
	line=line.strip("\n\r")
	#sr_no,date,name,chats,avg_resp,avg_res,avg_rating,feedback= line.split('\t')
	name,date,week,dur = line.split('\t')
	h,m,s= dur.split(':')
	timeinhr= round((int(h) + (int(m)/60) + (int(s)/3600)),2)
	#month,da,year=date.split('/')
	#newdate='-'.join([year,month,da])
	#result='\t'.join([sr_no,newdate,name,chats,str(timeinsec),avg_res,avg_rating,feedback])
	result ='\t'.join([name,date,week,str(timeinhr)])
	print(result)
