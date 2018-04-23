import sys
import datetime
import calendar

if __name__ == "__main__":
	dayofweek = {'Sunday':0,'Monday':0,'Tuesday':0,'Wednesday':0,'Thursday':0,'Friday':0,'Saturday':0}
	timeofday = {'0-2':0,'3-5':0,'6-8':0,'9-11':0,'12-14':0,'15-17':0,'18-20':0,'21-23':0}
	month = {'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0}
	with open(sys.argv[1]) as f:
		first = True
		for line in f:
			if first:
				first = False
				continue
			commasplit = line.rstrip().split(',')
			temp_date = commasplit[2]
			space_split = temp_date.split(' ')
			dash_split = space_split[0].split('/')
			time_split = space_split[1].split(':')
			if space_split[2] == 'PM' and time_split[0] != '12':
				time_split[0] = str(int(time_split[0]) + 12)
			elif space_split[2] == 'AM' and time_split[0] == '12':
				time_split[0] = '0'
			#print(dash_split[2]+" "+dash_split[0]+" "+dash_split[1])
			d = datetime.date(int(dash_split[2]),int(dash_split[0]),int(dash_split[1]))
			dofw = calendar.day_name[d.weekday()]
			dayofweek[dofw] = dayofweek[dofw] + 1
			month[dash_split[0]] = month[dash_split[0]] + 1	
			if int(time_split[0]) < 3:
				timeofday['0-2'] = timeofday['0-2'] + 1
			elif int(time_split[0]) > 2 and int(time_split[0]) < 6:
				timeofday['3-5'] = timeofday['3-5'] + 1
			elif int(time_split[0]) > 5 and int(time_split[0]) < 9:
				timeofday['6-8'] = timeofday['6-8'] + 1
			elif int(time_split[0]) > 8 and int(time_split[0]) < 12:
				timeofday['9-11'] = timeofday['9-11'] + 1
			elif int(time_split[0]) > 11 and int(time_split[0]) < 15:
				timeofday['12-14'] = timeofday['12-14'] + 1
			elif int(time_split[0]) > 14 and int(time_split[0]) < 18:
				timeofday['15-17'] = timeofday['15-17'] + 1
			elif int(time_split[0]) > 17 and int(time_split[0]) < 21:
				timeofday['18-20'] = timeofday['18-20'] + 1
			else:
				timeofday['21-23'] = timeofday['21-23'] + 1
	print(dayofweek)
	print(timeofday)
	print(month)
				
