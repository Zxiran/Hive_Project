import fileinput

for line in fileinput.input():
	line=line.strip("\n\r")
	sr_no,date,name,chats,avg_resp,avg_res,avg_rating,feedback= line.split('\t')
	
	h,m,s=avg_resp.split(':')
	timeinsec= (int(h)*3600) + (int(m)*60) + int(s)	
	month,da,year=date.split('/')
	newdate='-'.join([year,month,da])
	result='\t'.join([sr_no,newdate,name,chats,str(timeinsec),avg_res,avg_rating,feedback])
	print(result)
