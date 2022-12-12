import fileinput

for line in fileinput.input():
	line=line.strip("\n\r")
	h=0
	m=0
	s=0
	agent,avg_weekly_res_time,week= line.split('\t')
	if float(avg_weekly_res_time)>=60:
		h=int(int(float(avg_weekly_res_time))/60)
		m=int(float(avg_weekly_res_time))%60
		decival = float(avg_weekly_res_time) - int(float(avg_weekly_res_time)) 
		s=int((decival*60).__round__(0))
	elif float(avg_weekly_res_time)<1:
		s=int(float(avg_weekly_res_time) *60) 
	else:
				
		intofloat=float(avg_weekly_res_time)		
		m=int(intofloat)
		decival = float(avg_weekly_res_time) - m
		s=int((decival*60).__round__(0))
	
	time=':'.join([str(h),str(m),str(s)])
	result='\t'.join([agent,time,week])
	print(result)
