import sys
import fileinput
#csvfile = open('/home/cloudera/project_1/files/AgentPerformance.csv')
# row ="1	agent_name	date	avg_resp	feedback"
for line in fileinput.input():
	line=line.strip("\n\r")
	sr_no,date,name,chats,avg_resp,avg_res,avg_rating,feedback= line.split('\t')
	num=int(sr_no)
	#num+=5
	month,da,year=date.split('/')
	newdate='-'.join([year,month,da])
	result='\t'.join([str(num),newdate,name,chats,avg_resp,avg_res,avg_rating,feedback])
	print(result)
