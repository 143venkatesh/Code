import csv
#import pandas as pd 
import requests
import json
import MySQLdb
#import pdb;pdb.set_trace()
#import self



class Blackbuck:
	headers = { 
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'http://boss.blackbuck.com/dashboard',
            'Authorization': 'Token :6d2ec4190d34eb89441492a6518f58132de8b31f',
            'Content-Type': 'application/json',
            'Origin': 'http://boss.blackbuck.com',
            'Proxy-Authorization': 'Basic aHJAaGVhZHJ1bi5jb206aGRybl4xMjMh',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'TE': 'Trailers',
                 }
        
        numbers = ['7305606056','9839455640']
        field_names = ['phone_no','status','address_status']
        status = ['REQUESTED','APPROVED','ACTIVATED','IN_TRANSIT','DELIVERED,FIRST_RECHARGE_DONE','REJECTED']
	with open('employee_file2.csv', mode='w+') as csv_file:
            csv_file =  open('blackbug1.csv', 'w')
	    writer = csv.DictWriter(csv_file, fieldnames = field_names)

        #import pdb;pdb.set_trace()
        with open('blackbug1.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    line_count += 1
        
        #csv1=csv.reader(open('blackbug1.csv','r'))  
        for number in numbers:
            for statu in status:
                params = ( 
                ('status', statu),
		        ('type', '1'),
		        ('content', number),
		        ('page', '1'),
		        ('offset', '25'),
                        )
                response = requests.get('https://api-fms.blackbuck.com/fmstoll/api/v1/fastag/list', headers=headers, params=params)
	        ress= json.loads(response.text)
	        tracking = ress.get('data','').get('content','')
                csvdata={}
	        for track in tracking:
                    csvdata1 = []
                    name = track.get('name','')
		    address_status = track.get('address','').get('verification_status','')
		    truck_status = track.get('address','').get('status','')
                    csvdata['phone_no'] = number 
                    csvdata['status']=truck_status
                    csvdata['address_status']=address_status
                    csvdata1.append(csvdata)
                    writer.writerows(csvdata1)
                    print (truck_status)
		#csv_file.close()
