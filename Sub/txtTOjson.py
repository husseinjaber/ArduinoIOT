
# Python program to convert text 
# file to JSON 
  
  
import json 
import time
  
  
# the file to be converted 
filename = 'D:/Program Files (x86)/EasyPHP-Devserver-17/eds-www/Arduino/files/SubAnswersLines.txt'
  
# resultant dictionary 
dict1 = {} 
  
# fields in the sample file  
fields =['Date','Time','ID', 'TotalAmplitude', 'AverageAmplitude', 'MaximumAmplitude','NoofCars'] 
while 1:
	with open(filename) as fh:
		l = 1
		for line in fh:
			description = list( line.strip().split(None, 7))
			sno ='data'+str(l)
			i = 0
			dict2 = {}
			while i<len(fields):
				dict2[fields[i]]= description[i]
				i = i + 1
			dict1[sno]= dict2
			#print(l)
			l = l + 1
	out_file = open("D:/Program Files (x86)/EasyPHP-Devserver-17/eds-www/Arduino/files/test2.json", "w")
	json.dump(dict1, out_file, indent = 4)
	out_file.close() 
	time.sleep(1)